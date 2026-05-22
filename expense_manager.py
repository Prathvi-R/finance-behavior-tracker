def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    note = input("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. ₹{expense['amount']} | "
            f"{expense['category']} | "
            f"{expense['note']}"
        )