# Finance-Tracker

#Description:
Finance Tracker is a simple and efficient application designed to help users track their personal finances. With this tool, users can set a budget, add and manage transactions, and monitor their spending to stay within their financial limits. The intuitive user interface makes it easy to visualize your current budget, the amount used, and the remaining balance.

#Features:
Set Budget: Users can set their budget and update it anytime.
Add Transaction: Record individual transactions with descriptions and amounts.
View Transactions: Display all transactions with detailed breakdowns.
Modify Budget: Add or subtract amounts from the budget as needed.
Reset Budget: Completely reset the budget and transaction history to start fresh.
Interactive User Interface: All actions are available through a clean and intuitive Tkinter-based GUI.

#Installation
To run this project, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the Repository: Open a terminal or command prompt, and run:
    git clone git clone https://github.com/Toasty1k/Finance-Tracker.git


2. Navigate to the Project Directory:
   cd finance-tracker/FinanceTrackerScript

3. Create a Virtual Environment (Optional but recommended): In the project directory, create a virtual environment to manage dependencies:
python -m venv venv

4. Activate it:
   - Windows: venv\Scripts\activate
   - macOS/Linux: source venv/bin/activate

5. Install Dependencies: Install the required Python libraries:
   pip install -r requirements.txt

#Usage
After installing the dependencies, you can start using the Finance Tracker application!
Run the Application: Run the following command from the project directory to launch the Tkinter GUI:
python financeTracker.UI.py

#Main Functions:
Add Transaction: Enter transaction details, such as description and amount.
View Transactions: Check a list of all recorded transactions.
Modify Budget: Add or subtract amounts from the current budget.
Reset Budget: Reset all budget and transaction data.

#Folder Structure
The project is organized as follows:
Fin Tracker/
│
├── FinanceTrackerScript/          # Main application folder
│   ├── dataHandling.py            # Script for handling data storage/retrieval
│   ├── financeTracker.UI.py       # Main script containing the Tkinter GUI
│   ├── defScript.py               # Script containing all function definitions
│   └── utils.py                   # Script for utility functions like budget calculations
│
├── data/                          # Folder containing transaction data
│   └── finance_data.json          # Stores transaction and budget data
│
├── README.md                      # Project documentation (this file)
├── requirements.txt               # Python dependencies
└── .vscode/                       # VSCode settings (not uploaded)

#Data
ALL transaction and budget information is stored in the data/finance_data.json file. You can modify or delete this file to reset the application’s data.


