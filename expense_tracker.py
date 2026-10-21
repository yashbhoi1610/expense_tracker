
import csv
import os
from datetime import datetime
from collections import defaultdict

FILE_NAME = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]


def initialize_file():
    """Create the CSV file if it does not exist."""
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def get_valid_date():
    """Read a valid date in YYYY-MM-DD format."""
    while True:
        date_text = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("Invalid date! Example: 2026-10-21")


def get_valid_amount():
    """Read a positive expense amount."""
    while True:
        try:
            amount = float(input("Enter amount (Rs.): "))
            if amount > 0 and amount != float("inf"):
                return round(amount, 2)
            print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid amount! Enter a number.")


def read_expenses():
    """Read expense records from the CSV file."""
    initialize_file()
    expenses = []

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != FIELDS:
            print("Error: CSV file has an invalid header.")
            return []

        for row in reader:
            try:
                datetime.strptime(row["date"], "%Y-%m-%d")
                amount = float(row["amount"])

                if (
                    not row["category"].strip()
                    or not row["description"].strip()
                    or amount <= 0
                    or amount == float("inf")
                ):
                    continue

                row["amount"] = amount
                expenses.append(row)
            except (ValueError, TypeError, KeyError):
                print("Warning: Skipping an invalid CSV row.")

    return expenses


def add_expense():
    """Add a new expense to the CSV file."""
    print("\n--- ADD EXPENSE ---")
    date = get_valid_date()

    while True:
        category = input("Enter category: ").strip()
        if category:
            break
        print("Category cannot be empty.")

    while True:
        description = input("Enter description: ").strip()
        if description:
            break
        print("Description cannot be empty.")

    amount = get_valid_amount()
    initialize_file()

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow({
            "date": date,
            "category": category,
            "description": description,
            "amount": f"{amount:.2f}"
        })

    print("Expense saved successfully!")


def display_expenses(expenses):
    """Display a list of expenses."""
    if not expenses:
        print("No expenses found.")
        return

    print("\nDate        Category       Description              Amount")
    print("-" * 68)

    for expense in expenses:
        print(
            f"{expense['date']:<12}"
            f"{expense['category']:<15}"
            f"{expense['description']:<25}"
            f"Rs. {expense['amount']:.2f}"
        )

    total = sum(expense["amount"] for expense in expenses)
    print("-" * 68)
    print(f"Total: Rs. {total:.2f}")


def view_expenses():
    """Display all saved expenses."""
    print("\n--- ALL EXPENSES ---")
    display_expenses(read_expenses())


def filter_expenses():
    """Filter expenses by category or date."""
    expenses = read_expenses()

    print("\n--- FILTER EXPENSES ---")
    print("1. Filter by category")
    print("2. Filter by date")
    print("3. Filter by month (YYYY-MM)")

    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        category = input("Enter category: ").strip().casefold()
        filtered = [
            e for e in expenses
            if e["category"].casefold() == category
        ]

    elif choice == "2":
        date = get_valid_date()
        filtered = [e for e in expenses if e["date"] == date]

    elif choice == "3":
        while True:
            month = input("Enter month (YYYY-MM): ").strip()
            try:
                datetime.strptime(month, "%Y-%m")
                break
            except ValueError:
                print("Invalid month! Example: 2026-10")

        filtered = [e for e in expenses if e["date"].startswith(month)]

    else:
        print("Invalid choice!")
        return

    display_expenses(filtered)


def category_summary():
    """Calculate and display totals per category."""
    expenses = read_expenses()
    totals = defaultdict(float)

    for expense in expenses:
        category = expense["category"].strip().title()
        totals[category] += expense["amount"]

    print("\n--- CATEGORY SUMMARY ---")

    if not totals:
        print("No expenses available.")
        return

    for category, total in sorted(
        totals.items(), key=lambda item: item[1], reverse=True
    ):
        print(f"{category:<20} Rs. {total:.2f}")

    grand_total = sum(totals.values())
    print("-" * 35)
    print(f"{'Grand Total':<20} Rs. {grand_total:.2f}")


def main():
    initialize_file()

    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()
