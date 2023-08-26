import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

def create_expenses_file():
    with open('financial.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])


if not os.path.isfile('financial.csv'):
    create_expenses_file()


def load_expenses():
    with open('financial.csv', 'r') as file:
        reader = csv.reader(file)
        financial = list(reader)
    return financial


def save_expenses(expenses):
    with open('financial.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)


def show_all():
    expenses = load_expenses()

    choice=input('Do you want to use current month enter yes ')
    if choice == 'yes':
        current_month = datetime.now().strftime('%Y-%m')
    else:
        current_month = input('Month in (yyyy-MM):')
    if expenses:
        print('Monthly expenses')
        header = expenses[0]
        print(", ".join(header))
        found_expenses = False
        for i, expense in enumerate(expenses):
            if i == 0:  # Skip the header row
                continue
            # Check if the expense belongs to the present month
            expense_date = datetime.strptime(expense[0], '%Y-%m-%d')
            if expense_date.strftime('%Y-%m') == current_month:
                print(str(i) + ' -> ' + '  '.join(expense))
                found_expenses = True
        print()
        if not found_expenses:
            print('No expenses found.')
    else:
        print('No expenses found.')


def add_expense(expense):
    expenses = load_expenses()
    expenses.append(expense)  # Append the expense directly
    save_expenses(expenses)
    print("expense added successfully.")
    print()


def del_expense(index):
    expenses = load_expenses()
    if index < 0 or index >= len(expenses):
        print("Invalid index.")
    else:
        expense = expenses.pop(index)
        save_expenses(expenses)
        print("expense", expense[0], "deleted successfully.")
    print()


def clear_console():
    # Clear the console screen
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/Mac


def monthly_graph():
    x = []
    y = []

    expenses = load_expenses()
    choice = input('To show graph for current month enter yes ')
    if choice == 'yes':
        current_month = datetime.now().strftime('%Y-%m')
    else:
        current_month = input('Month in (yyyy-MM):')
    if expenses:
        for i, expense in enumerate(expenses):
            if i == 0:  # Skip the header row
                continue
            expense_date = datetime.strptime(expense[0], '%Y-%m-%d')

            if expense_date.strftime('%Y-%m') == current_month:
                # print(str(i) + ' -> ' + '  '.join(expense))
                x.append(expense[1])
                y.append(float(expense[2]))

    plt.bar(x, y, color='g', width=0.72, label="Amount")
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.title('Monthly Expenses for ' + current_month)
    plt.legend()
    plt.show()


while True:
    print("1. Show monthly expenses")
    print("2. Add expense")
    print("3. Delete expense")
    print('4. Clear screen')
    print('5. Show monthly graph')
    print("0. Exit")

    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        show_all()

    elif choice == 2:
        print("Enter expense details here")
        choice = input('To use todays date enter yes ')
        if choice == 'yes':
            date = datetime.now().strftime('%Y-%m-%d')
            print(date)
        else:
            date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = input("Enter amount: ")
        description = input("Enter description: ")
        expense = [date, category, amount, description]
        add_expense(expense)

    elif choice == 3:
        show_all()
        index = int(input("Enter the index of the expense to delete: "))
        print()
        del_expense(index)

    elif choice == 4:
        clear_console()

    elif choice == 5:
        monthly_graph()

    elif choice == 0:
        print("Exiting")
        break
