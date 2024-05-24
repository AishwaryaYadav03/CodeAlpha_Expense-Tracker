class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({'amount': amount, 'category': category})

    def categorize_expense(self, index, category):
        if 0 <= index < len(self.expenses):
            self.expenses[index]['category'] = category
        else:
            print("Invalid expense index")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            for i, expense in enumerate(self.expenses):
                print(f"{i+1}. Amount: {expense['amount']}, Category: {expense['category']}")

    def get_summary(self):
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            summary[category] = summary.get(category, 0) + amount
        return summary

    def get_insights(self):
        total_spent = sum(expense['amount'] for expense in self.expenses)
        categories = [expense['category'] for expense in self.expenses]
        most_common_category = max(set(categories), key=categories.count)
        return total_spent, most_common_category

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Categorize Expense")
        print("3. View Expenses")
        print("4. View Summary")
        print("5. View Insights")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            tracker.add_expense(amount, category)
            print("Expense added successfully!")

        elif choice == '2':
            index = int(input("Enter expense index: ")) - 1
            category = input("Enter expense category: ")
            tracker.categorize_expense(index, category)
            print("Expense updated successfully!")

        elif choice == '3':
            tracker.view_expenses()

        elif choice == '4':
            summary = tracker.get_summary()
            print("\nExpense Summary:")
            for category, amount in summary.items():
                print(f"{category}: {amount}")
        
        elif choice == '5':
            total_spent, most_common_category = tracker.get_insights()
            print(f"\nTotal Amount Spent: {total_spent}")
            print(f"Most Common Category: {most_common_category}")


        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
