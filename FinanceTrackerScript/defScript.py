import tkinter as tk
from tkinter import messagebox
from dataHandling import load_data, save_data
from utils import add_transaction, check_budget_status, reset_budget, add_to_budget

class FinanceTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")

        self.data = load_data()
        self.budget = self.data.get('budget', 0)
        self.transactions = self.data.get('transactions', [])

        self.create_widgets()
        if self.budget <= 0:
            self.prompt_budget()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Finance Tracker", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.stats_frame = tk.Frame(self.root)
        self.stats_frame.pack(side=tk.RIGHT, padx=20)

        self.budget_label = tk.Label(self.stats_frame, text=self.get_budget_info(), font=("Arial", 16))
        self.budget_label.pack(pady=(20, 5))

        self.amount_used_label = tk.Label(self.stats_frame, text=f"Amount Used: ${self.get_amount_used():.2f}", font=("Arial", 14))
        self.amount_used_label.pack(pady=(5, 5))

        self.percent_used_label = tk.Label(self.stats_frame, text=f"% Used: {self.get_percent_used():.2f}%", font=("Arial", 14))
        self.percent_used_label.pack(pady=(5, 5))

        self.amount_remaining_label = tk.Label(self.stats_frame, text=f"Amount Remaining: ${self.get_amount_remaining():.2f}", font=("Arial", 14))
        self.amount_remaining_label.pack(pady=(5, 20))

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.LEFT, padx=20)

        self.add_transaction_button = tk.Button(self.button_frame, text="Add Transaction", command=self.add_transaction)
        self.add_transaction_button.pack(pady=5)

        self.show_transactions_button = tk.Button(self.button_frame, text="Show Transactions", command=self.show_transactions)
        self.show_transactions_button.pack(pady=5)

        self.add_to_budget_button = tk.Button(self.button_frame, text="Add to Budget", command=self.add_to_budget)
        self.add_to_budget_button.pack(pady=5)

        self.change_budget_button = tk.Button(self.button_frame, text="Change Budget", command=self.change_budget)
        self.change_budget_button.pack(pady=5)

        self.reset_budget_button = tk.Button(self.button_frame, text="Reset Budget", command=self.reset_budget)
        self.reset_budget_button.pack(pady=5)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=20)

    def prompt_budget(self):
        def submit_budget():
            try:
                amount = float(amount_entry.get())
                if amount < 0:
                    raise ValueError("Amount must be positive")
                self.budget = amount
                save_data({'budget': self.budget, 'transactions': self.transactions})
                self.budget_label.config(text=self.get_budget_info())
                messagebox.showinfo("Success", f"Budget set to ${amount:.2f}.")
                budget_window.destroy()
            except ValueError as e:
                messagebox.showerror("Invalid Input", str(e))

        budget_window = tk.Toplevel(self.root)
        budget_window.title("Set Budget")
        tk.Label(budget_window, text="Enter your budget amount:").pack(pady=10)
        amount_entry = tk.Entry(budget_window)
        amount_entry.pack(pady=5)
        tk.Button(budget_window, text="Submit", command=submit_budget).pack(pady=10)
        tk.Button(budget_window, text="Back", command=budget_window.destroy).pack(pady=5)

    def add_transaction(self):
        def submit_transaction():
            try:
                amount = float(amount_entry.get())
                if amount < 0:
                    raise ValueError("Amount must be positive")
                description = description_entry.get()
                if not description:
                    raise ValueError("Description cannot be empty")
                if check_budget_status(amount, self.budget, self.transactions) == 'exceeds':
                    messagebox.showwarning("Warning", "Transaction exceeds budget.")
                else:
                    add_transaction(self.transactions, description, amount)
                    save_data({'budget': self.budget, 'transactions': self.transactions})
                    self.budget_label.config(text=self.get_budget_info())
                    messagebox.showinfo("Success", f"Added transaction: {description}, Amount: ${amount:.2f}")
                    transaction_window.destroy()
            except ValueError as e:
                messagebox.showerror("Invalid Input", str(e))

        transaction_window = tk.Toplevel(self.root)
        transaction_window.title("Add Transaction")
        tk.Label(transaction_window, text="Enter amount:").pack(pady=10)
        amount_entry = tk.Entry(transaction_window)
        amount_entry.pack(pady=5)
        tk.Label(transaction_window, text="Enter description:").pack(pady=10)
        description_entry = tk.Entry(transaction_window)
        description_entry.pack(pady=5)
        tk.Button(transaction_window, text="Submit", command=submit_transaction).pack(pady=10)
        tk.Button(transaction_window, text="Back", command=transaction_window.destroy).pack(pady=5)

    def show_transactions(self):
        transactions_window = tk.Toplevel(self.root)
        transactions_window.title("Transactions")
        tk.Label(transactions_window, text="Transactions:", font=("Arial", 16)).pack(pady=10)

        if not self.transactions:
            tk.Label(transactions_window, text="No transactions found.").pack(pady=10)
        else:
            for txn in self.transactions:
                txn_text = f"{txn['description']}: ${txn['amount']:.2f}"
                tk.Label(transactions_window, text=txn_text).pack(pady=5)

    def reset_budget(self):
        def confirm_reset():
            self.budget = 0
            self.transactions.clear()
            save_data({'budget': self.budget, 'transactions': self.transactions})
            self.budget_label.config(text=self.get_budget_info())
            self.amount_remaining_label.config(text=f"Amount Remaining: ${self.get_amount_remaining():.2f}")  # Update amount remaining
            messagebox.showinfo("Budget Reset", "Budget has been reset.")
            reset_window.destroy()

        reset_window = tk.Toplevel(self.root)
        reset_window.title("Reset Budget")
        tk.Label(reset_window, text="Are you sure you want to reset the budget?").pack(pady=10)
        tk.Button(reset_window, text="Confirm", command=confirm_reset).pack(pady=10)
        tk.Button(reset_window, text="Cancel", command=reset_window.destroy).pack(pady=5)

    def add_to_budget(self):
        def submit_addition():
            try:
                amount = float(amount_entry.get())
                if amount < 0:
                    raise ValueError("Amount must be positive")
                self.budget += amount
                save_data({'budget': self.budget, 'transactions': self.transactions})
                self.budget_label.config(text=self.get_budget_info())
                messagebox.showinfo("Success", f"Added ${amount:.2f} to the budget.")
                add_window.destroy()
            except ValueError as e:
                messagebox.showerror("Invalid Input", str(e))

        add_window = tk.Toplevel(self.root)
        add_window.title("Add to Budget")
        tk.Label(add_window, text="Enter amount to add:").pack(pady=10)
        amount_entry = tk.Entry(add_window)
        amount_entry.pack(pady=5)
        tk.Button(add_window, text="Submit", command=submit_addition).pack(pady=10)
        tk.Button(add_window, text="Back", command=add_window.destroy).pack(pady=5)

    def change_budget(self):
        def submit_change():
            try:
                amount = float(amount_entry.get())
                if amount < 0 or amount > self.budget:
                    raise ValueError("Amount must be positive and cannot exceed the current budget")
                self.budget -= amount
                save_data({'budget': self.budget, 'transactions': self.transactions})
                self.budget_label.config(text=self.get_budget_info())
                messagebox.showinfo("Success", f"Subtracted ${amount:.2f} from the budget.")
                change_window.destroy()
            except ValueError as e:
                messagebox.showerror("Invalid Input", str(e))

        change_window = tk.Toplevel(self.root)
        change_window.title("Change Budget")
        tk.Label(change_window, text="Enter amount to subtract:").pack(pady=10)
        amount_entry = tk.Entry(change_window)
        amount_entry.pack(pady=5)
        tk.Button(change_window, text="Submit", command=submit_change).pack(pady=10)
        tk.Button(change_window, text="Back", command=change_window.destroy).pack(pady=5)

    def get_budget_info(self):
        return f"Budget: ${self.budget:.2f}"

    def get_amount_used(self):
        return sum(txn['amount'] for txn in self.transactions)

    def get_percent_used(self):
        if self.budget == 0:
            return 0
        return (self.get_amount_used() / self.budget) * 100

    def get_amount_remaining(self):
        return self.budget - self.get_amount_used()
