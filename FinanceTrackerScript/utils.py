def load_data():
    """Load data from a file (placeholder function)."""
    # Implement your loading logic here
    return {'budget': 0, 'transactions': []}

def save_data(data):
    """Save data to a file (placeholder function)."""
    # Implement your saving logic here
    pass

def check_budget_status(amount, budget, transactions):
    """
    Check the status of the budget based on the transaction amount.
    Returns 'within', 'close', or 'exceeds'.
    """
    total_spent = sum(txn['amount'] for txn in transactions)
    if total_spent + amount > budget:
        return 'exceeds'
    elif total_spent + amount > budget * 0.9:
        return 'close'
    return 'within'

def add_transaction(transactions, description, amount):
    """
    Add a transaction to the list of transactions.
    Each transaction is a dictionary with description and amount.
    """
    transactions.append({'description': description, 'amount': amount})
def reset_budget():
    """Reset the budget to zero."""
    return 0

def add_to_budget(current_budget, amount):
    """
    Adds an amount to the current budget.
    Returns the new budget.
    """
    return current_budget + amount

def change_budget(current_budget, amount):
    """
    Changes the current budget by subtracting the specified amount.
    Ensures that the budget does not go below zero.
    """
    new_budget = current_budget - amount
    return max(new_budget, 0)  # Prevent budget from going negative
