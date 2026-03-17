expenses = []

def export_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(expense["name"] + " - " + expense["Amount"] + "\n")

def main():
    while True:
        print("1. Add Expenses")
        print("2. View Expense")
        print("3. Export to File")
        print("4. Exit \n")

        choice = input("Enter Choice : ")

        if choice == "1":
            name = input("Enter Expense Name : ")
            Amount = input("Enter Amount : ")

            expenses.append({'name': name, 'Amount': Amount})

        elif choice == "2":
            for expense in expenses:
                print(expense["name"], "-", expense["Amount"])
                print("\n")

        elif choice == "3":
            export_expenses(expenses)
            print("Expenses exported successfully!")

        elif choice == "4":
            print("Exiting the program")
            break

        else:
            print("Invalid choice, Try Again")

main()

