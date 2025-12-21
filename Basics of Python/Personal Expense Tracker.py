import json
import os

# File where data will be stored
Expenses =[]
Budget = 0

DATA_FILE = "logging_expenses.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
        Expenses = data["Expenses"]
        Budget = data["Budget"]

categories = ["Food", "Travel", "Entertainment", "Shopping", "Bills", "Others"]

def save_data():
    """Save all data to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump({"Expenses": Expenses, "Budget": Budget}, file, indent=4)
        


def Menu():
    print("=" * 40)
    print("PERSONAL EXPENSE TRACKER".center(40))
    print("=" * 40)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Set/Check Budget")
    print("5. Search Expenses")
    print("6. Delete an Entry")
    print("7. Exit")
    print("=" * 40)


print("Welcome to Personal Expense Tracker!!")
while True:
    Menu()
    choice = (input("Enter your choice (1-7): "))
    print("\n")


    if choice == "1":
        print("Add new Expense".upper().center(50, "-"))

        print(f'Available Categories: {", ".join(categories)}')
        category = input("Enter Category: ")
        if category in categories:
            pass
        else:
            print('Category you have entered is does not exist in the list,Hence we will make the entry in "Others" Category.\n')
            category="Others"
        amount = float(input("Enter Amount: ₹"))
        Desc = input("Enter Description: ")
        Expense = dict()
        Expense["Category"] = category
        Expense["Amount"] = amount
        Expense["Desc"] = Desc
        Expenses.append(Expense)
        print("Expense Added Successfully".upper().center(40,"-"))
        print("\n")
        save_data()


    elif choice == "2":
        count = 1
        Total_Expense = 0
        print("All Expenses".upper().center(67, "-"))
        print(f"|{'Sr No.':^14}|{'Categories':^20}|{'Amount':^14}|{'Description':^14}|")
        for i in Expenses:
            print(f"|{'#'+str(count):^14}|{i['Category']:^20}|{'₹'+str(i['Amount']):^14}|{i['Desc']:^14}|")
            count += 1
            Total_Expense = Total_Expense + i['Amount']
        print("-" * 67)
        print(f"Total Expense: ₹{Total_Expense}")
        print("\n")
        save_data()
    elif choice == "3":
        summary_cat = {}
        for i in categories:
            summary_cat[i] = 0
        for i in Expenses:
            item = i["Category"].title()
            amount = i["Amount"]
            summary_cat[item] += amount
        print("Category Summary".center(33, "-").upper())
        print(f"|{'Category'.upper():^20}|{'Amount'.upper():^10}|")
        for i in summary_cat:
            if summary_cat[i] == 0:
                pass
            else:
                print(f"|{i:^20}|{'₹' + str(summary_cat[i]):^10}|")
        print("-" * 33)
        Total_Expense = 0
        for i in summary_cat:
            Total_Expense += summary_cat[i]
        print("-" * 33)
        print(f"Total Expenses are :₹{Total_Expense}")
        print("\n")
        save_data()
    elif choice == "4":
        if Budget == 0:
            print("Set Budget".upper().center(40, "-"))
            Budget = float(input("Enter your Budget: ₹"))
            print("✓ Budget Set Successfully".center(40, "-"))
            print("\n")
        else:
            print("Checking Budget".upper().center(40,"-"))
            Total_Expense=0
            for i in Expenses:
                Total_Expense +=i["Amount"]
            print(f"Your Initial Budget was ₹{Budget}")
            print(f"You have spent a total of ₹{Total_Expense}")
            print(f"Your Budget is ₹{Budget - Total_Expense}")
            if Budget - Total_Expense > 0:
                print("You still have money to spend. Good Job!!😁")
                print("\n")
            else:
                print("You are over budget, Please Reduce expenses.😐")
                print("\n")
        save_data()
    elif choice == "5":
        user_input = input("What category's Expenses do you want?: ")
        summary_cat = {}
        for i in categories:
            summary_cat[i] = 0
        for i in Expenses:
            item = i["Category"].title()
            amount = i["Amount"]
            summary_cat[item] += amount
        print("Here is what you searched for.....")
        print("Category Wise Summary".center(54, "-").upper())
        print(f"|{'Category'.upper():^20}|{'Amount'.upper():^10}|{'Description'.upper():^20}|")
        sum_expense=0
        for i in Expenses:
            if i["Category"].lower()==user_input.lower():
                print(f"|{i['Category']:^20}|{'₹'+str(i['Amount']):^10}|{i['Desc']:^20}|")
                sum_expense+=i["Amount"]
        print("-" * 54)
        print(f"Total Expense: {'₹'+str(sum_expense):^10}|")
        print("\n")
        save_data()

    elif choice == "6":
        print("Delete an Entry".upper().center(40,"-"))
        print(f"|{'Sr No.':^14}|{'Categories':^20}|{'Amount':^14}|{'Description':^14}|")
        count=1
        for i in Expenses:
            print(f"|{'#'+str(count):^14}|{i['Category']:^20}|{'₹'+str(i['Amount']):^14}|{i['Desc']:^14}|")
            count += 1
            Total_Expense = Total_Expense + i['Amount']
        print("-" * 67)
        del_item=input("Enter the index number of the Item to be deleted:")
        if 0<int(del_item)<=len(Expenses):
            deleted_expense=Expenses.pop(int(del_item)-1)
            save_data()
            print("Item Deleted Successfully".center(40,"-"))
            print("\n")
        else:
            print("That Index is not available".center(40,"-"))
            print("\n")
        save_data()


    elif choice == "7":
        print("")
        print("I have saved your accounts.")
        print("Thank You For Visiting!! Come again tomorrow!!")
        print("GoodBye👋")
        print("\n")
        save_data()
        break
    else:
        print("Invalid Option, Please try Again")
        print("\n")        
"""This is a Personal Expense Tracker which helps you to keep a track of your daily expenses and budget.
It allows you to add, view, delete and search expenses by category. It also provides a summary of expenses 
by category and helps you to set and check your budget.
It Retains all memory of your expenses and budget by saving it in a JSON file."""