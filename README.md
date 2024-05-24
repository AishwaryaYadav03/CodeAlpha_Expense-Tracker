ExpenseTracker Class
1. Initialization:

The constructor initializes an empty list expenses.

2. Methods:

add_expense(amount, category): Adds a new expense with the given amount and category.
categorize_expense(index, category): Updates the category of an expense at a given index if valid.
view_expenses(): Prints all recorded expenses or a message if none are recorded.
get_summary(): Returns a dictionary summarizing total expenses by category.
get_insights(): Returns total spending and the most common expense category.

main Function

1. Create Instance:

An instance of ExpenseTracker is created.

2. User Interaction Loop:

Displays a menu with options:
1]Add Expense
2]Categorize Expense
3]View Expenses
4]View Summary
5]View Insights
6]Exit

3. Menu Options:

Add Expense: Prompts for amount and category, then adds the expense.
Categorize Expense: Prompts for expense index and new category, then updates the category.
View Expenses: Displays all recorded expenses.
View Summary: Shows total expenses by category.
View Insights: Shows total spending and the most common category.
Exit: Ends the program.

4. Invalid Input Handling:

Prints an error message for invalid menu choices.

Program Execution
The script runs the main function when executed directly, enabling users to track and manage their expenses through a command-line interface.
