from expense_manager import add_expense, view_expenses
from analytics import total_spending, category_summary

expenses = []

while True:
    print("\n===== Finance Behavior Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        total_spending(expenses)

    elif choice == "4":
        category_summary(expenses)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")