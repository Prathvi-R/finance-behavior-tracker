def total_spending(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total Spending: ₹{total}")


def category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]

        if category not in summary:
            summary[category] = 0

        summary[category] += expense["amount"]

    print("\nCategory Summary:")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount}")