# Expense Tracker - Python CLI App
import sqlite3
import datetime

# Connect to SQLite database (or create it)
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create expenses table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    date TEXT,
    category TEXT,
    amount REAL,
    description TEXT
)
''')

def add_expense():
    date = datetime.date.today().isoformat()
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    c.execute('INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)',
              (date, category, amount, description))
    conn.commit()
    print("Expense added successfully!\n")

def view_expenses():
    print("\nYour Expenses:")
    for row in c.execute('SELECT * FROM expenses'):
        print(row)
    print("")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
