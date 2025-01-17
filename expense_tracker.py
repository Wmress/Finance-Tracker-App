from expense import Expense

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    
    #Get user to input their expense

    expense = get_user_expense()
    print(expense)

    #write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    #Read file and summarize Expenses
    summarize_expense(expense_file_path)
    

def get_user_expense():
    print(f"🎯Getting Users Expense ")
    expense_name = input("Enter expense name: ")
    amount_expense = float(input("Enter expense amount: "))
    print(f"Your entered: {expense_name}, {amount_expense}")

    expense_categories = [
        "🥙 Food",
        "🏡 Home", 
        "😊 Fun",
        " Misc"
    ]


    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"

        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        #for loop - iterate through
        if i in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, 
                category=selected_category, 
                amount= amount_expense
                )
            return new_expense
        else:
            print("Invaid category: Please try again.")

        break


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯Saving Users Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")
    

def summarize_expense(expense_file_path):
    print(f"🎯Getting users expense")
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)

if __name__ == "__main__":
    main()