import tkinter as tk
from tkinter import messagebox
from dataHandling import load_data, save_data
from utils import add_transaction, check_budget_status, reset_budget, add_to_budget
from defScript import FinanceTrackerApp

def main():
    root = tk.Tk()
    app = FinanceTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
