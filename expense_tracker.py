import csv
from datetime import datetime
import matplotlib.pyplot as plt


class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        """Initialize the Expense Tracker with a CSV filename."""
        self.filename = filename  
        self.expenses = []        # Initialize an empty list to hold expenses
        self.load_expenses()      

    def load_expenses(self):
        """Load expenses from a CSV file."""
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                self.expenses = [row for row in reader]  # Read all rows into the expenses list
        except FileNotFoundError:
            self.expenses = []  # If the file doesn't exist, initialize expenses as an empty list

    def save_expenses(self):
        """Save expenses to a CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.expenses)  # Write the expenses list to the CSV file

    def add_expense(self, category, amount, date):
        """Add a new expense to the tracker."""
        self.expenses.append([category, float(amount), date])  # Append the new expense to the list
        self.save_expenses()  # Save updated expenses to the CSV file
        print(f"Added expense: {category} - £{amount} on {date}")  # Confirmation message

    def view_expenses(self):
        """Print all recorded expenses."""
        if not self.expenses:
            print("No expenses recorded yet.")  # Check if there are any expenses
            return

        print("\nAll Expenses:")
        for expense in self.expenses:
            print(f"{expense[0]}: £{expense[1]} on {expense[2]}")  # Display each expense

    def filter_expenses_by_category(self, category):
        """Filter and display expenses by a specific category."""
        filtered = [expense for expense in self.expenses if expense[0].lower() == category.lower()]  # Filter expenses
        self.display_filtered_expenses(filtered)  # Show filtered results

    def filter_expenses_by_date(self, date):
        """Filter and display expenses by a specific date."""
        filtered = [expense for expense in self.expenses if expense[2] == date]  # Filter expenses by date
        self.display_filtered_expenses(filtered)  # Show filtered results

    def display_filtered_expenses(self, filtered):
        """Display the filtered expenses."""
        if not filtered:
            print("No matching expenses found.")  # Notify if no matching expenses
        else:
            print("\nFiltered Expenses:")
            for expense in filtered:
                print(f"{expense[0]}: £{expense[1]} on {expense[2]}")  # Display each filtered expense

    def visualize_expenses(self):
        """Visualize expenses by category in a pie chart."""
        categories = {}
        for expense in self.expenses:
            # Aggregate expenses by category
            if expense[0] in categories:
                categories[expense[0]] += expense[1]
            else:
                categories[expense[0]] = expense[1]

        if categories:
            # Create a pie chart for visual representation of expenses
            labels = categories.keys()  # Categories as labels
            sizes = categories.values()  # Corresponding amounts
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')  # Create pie chart with percentages
            plt.title('Expenses by Category')  # Title of the chart
            plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular
            plt.show()  # Display the pie chart
        else:
            print("No expenses to visualize.")  # Notify if no expenses are available for visualization

    def clear_expenses(self):
        """Clear all expenses from the tracker."""
        self.expenses = []  # Reset the expenses list to empty
        self.save_expenses()  # Save the cleared state to the CSV file
        print("All expenses have been cleared.")  # Confirmation message

# Main program function
def main():
    print("Expense Tracker is Running...")  # Notify user that the tracker is active
    tracker = ExpenseTracker()  # Create an instance of the Expense Tracker

    while True:
        # Display the menu options to the user
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Filter by Date")
        print("5. Visualize Expenses")
        print("6. Clear All Expenses")  
        print("7. Exit")  

        choice = input("Choose an option: ")  # Get user choice

        if choice == '1':
            # Prompt user for expense details
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, '%Y-%m-%d')  # Validate date format
                tracker.add_expense(category, amount, date)  # Add the expense
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")  # Error handling for invalid date

        elif choice == '2':
            tracker.view_expenses()  # View all recorded expenses

        elif choice == '3':
            category = input("Enter category to filter by: ")
            tracker.filter_expenses_by_category(category)  # Filter by category

        elif choice == '4':
            date = input("Enter date to filter by (YYYY-MM-DD): ")
            tracker.filter_expenses_by_date(date)  # Filter by date

        elif choice == '5':
            tracker.visualize_expenses()  # Visualize expenses

        elif choice == '6':
            # Confirm with the user before clearing all expenses
            confirm = input("Are you sure you want to clear all expenses? (yes/no): ")
            if confirm.lower() == 'yes':
                tracker.clear_expenses()  # Clear all expenses
            else:
                print("Clearing of expenses canceled.")  # User canceled the clearing

        elif choice == '7':  # Exit option
            print("Goodbye!")  # Farewell message
            break  # Exit the loop

        else:
            print("Invalid option. Please try again.")  # Error message for invalid option

if __name__ == "__main__":
    main()  # Run the main function
# python3 expense_tracker.py  == runs the program from terminal