def main():
    print(f"Running Expense Tracker!")
    
    #Get user to input their expense

    get_user_expense()

    #write their expense to a file
    save_expense_to_file()

    #Read file and summarize Expenses
    summarize_expense()
    

def get_user_expense():
    print(f"🎯Getting Users Expense ")
    expense_name = input("Enter expense name: ")
    amount_expense = float(input("Enter expense amount; "))
    print(f"Your entered: {expense_name}, {amount_expense}")

    expense_categories = [
        "🥙 Food",
        "🏡 Home", 
        "😊 Fun",
        "😏 Misc"
    ]


    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        slected_index = input("Enter a category number {value_range}: ")

        break


def save_expense_to_file():
    print(f"🎯Saving Users Expense")
    

def summarize_expense():
    print(f"🎯Getting users expense")

if __name__ == "__main__":
    main()