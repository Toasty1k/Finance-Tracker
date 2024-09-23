import json
from FinanceTrackerScript.dataHandling import load_transactions, save_transactions
from utils import (
    get_category_choices,
    get_user_choice,
    prompt_and_validate_amount,
    prompt_for_category,
    prompt_for_budget
)

# Initialize the budget and transactions list
budget = 0
transactions = []
previous_step = None

def add_transaction(amount, description, category):
    """Add a transaction to the list and save it to a file."""
    transactions.append({
        "amount": amount,
        "description": description,
        "category": category
    })
    save_transactions(transactions)
    print(f"Added transaction: {description}, Amount: {amount}, Category: {category}")

def show_transactions():
    """Display all transactions."""
    if not transactions:
        print("No transactions available.")
        return
    for transaction in transactions:
        print(f"{transaction['description']}: {transaction['amount']} (Category: {transaction['category']})")

def calculate_totals():
    """Calculate and display the total of all transactions."""
    total = sum(transaction['amount'] for transaction in transactions)
    remaining = budget - total
    if remaining < 0:
        print(f"Total: {total}. Oh no! You are over budget by {-remaining}.")
    else:
        print(f"Total: {total}. Remaining budget: {remaining}")

def check_budget(budget):
    """Check if the total transactions exceed the budget."""
    total_spent = sum(transaction['amount'] for transaction in transactions)
    remaining = budget - total_spent
    if total_spent > budget:
        print(f"Warning! You have exceeded your budget by {total_spent - budget}.")
    else:
        print(f"You're within your budget. You have {remaining} left.")
    return remaining

def prompt_for_budget_input():
    global budget
    try:
        budget = prompt_and_validate_amount("Set your budget: ")
    except ValueError:
        print("Invalid input. Budget must be a number.")
        exit()

def add_money_to_budget():
    """Add money to the budget."""
    amount = prompt_and_validate_amount("Enter the amount to add to your budget: ")
    global budget
    budget += amount
    print(f"New budget: {budget}")

def handle_transaction():
    """Handle the transaction process."""
    global previous_step
    amount = prompt_and_validate_amount("Enter the amount: ")
    previous_step = 'amount'
    description = input("Enter the description: ")
    previous_step = 'description'
    category = prompt_for_category("Enter the category (1. Food, 2. Rent, 3. Entertainment, 4. Utilities, 5. Other): ")
    if category == '5':  # Special case for 'Other'
        category = input("Other: ")
    add_transaction(amount, description, category)

def main():
    global previous_step
    transactions = load_transactions()
    prompt_for_budget_input()

    while True:
        print("\n1. Add Transaction")
        print("2. Show Transactions")
        print("3. Show Total")
        print("4. Check Budget")
        print("5. Add Money to Budget")
        print("6. Reset Budget and Clear Transactions")
        print("7. Exit")
        choice = get_user_choice()
        
        if choice == "1":
            previous_step = None
            handle_transaction()
        elif choice == "2":
            show_transactions()
        elif choice == "3":
            calculate_totals()
        elif choice == "4":
            remaining = check_budget(budget)
            if remaining < 0:
                print("Oh no! You are over budget. Refrain from spending.")
        elif choice == "5":
            add_money_to_budget()
        elif choice == "6":
            reset = input("Are you sure you want to reset your budget and clear all transactions? (yes/no): ")
            if reset.lower() == 'yes':
                transactions.clear()
                save_transactions(transactions)
                prompt_for_budget_input()
                print("Budget reset and transactions cleared.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 7.")

if __name__ == "__main__":
    main()
