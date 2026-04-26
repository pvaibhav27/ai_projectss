# EXPENSE TRACKER APP

expenses = []

def show_menu():
    print("\n==========================")
    print("     EXPENSE TRACKER      ")
    print("==========================")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. View by category")
    print("5. Exit")
    print("==========================")

def add_expense():
    print("\nCategories: Food | Transport | Shopping | Bills | Other")
    category = input("Enter category: ")
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount (INR): "))
        expenses.append({
            "category": category.title(),
            "description": description,
            "amount": amount
        })
        print(f"✅ ₹{amount} added under {category.title()}!")
    except ValueError:
        print("❌ Please enter a valid amount!")

def view_all():
    if len(expenses) == 0:
        print("\n📋 No expenses yet!")
    else:
        print("\n📋 ALL EXPENSES:")
        print("-" * 40)
        for i, exp in enumerate(expenses, 1):
            print(f"{i}. {exp['category']} | {exp['description']} | ₹{exp['amount']}")
        print("-" * 40)

def view_total():
    if len(expenses) == 0:
        print("\n📋 No expenses yet!")
    else:
        total = sum(exp["amount"] for exp in expenses)
        print(f"\n💰 Total Spent: ₹{total}")

def view_by_category():
    if len(expenses) == 0:
        print("\n📋 No expenses yet!")
    else:
        category_totals = {}
        for exp in expenses:
            cat = exp["category"]
            if cat in category_totals:
                category_totals[cat] += exp["amount"]
            else:
                category_totals[cat] = exp["amount"]

        print("\n📊 SPENDING BY CATEGORY:")
        print("-" * 40)
        for cat, total in category_totals.items():
            print(f"{cat}: ₹{total}")
        print("-" * 40)
        highest = max(category_totals, key=category_totals.get)
        print(f"🔥 Most spent on: {highest}")

# Main program
print("💰 Welcome to Expense Tracker!")

while True:
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_all()
    elif choice == "3":
        view_total()
    elif choice == "4":
        view_by_category()
    elif choice == "5":
        print("\n👋 Goodbye! Spend wisely!")
        break
    else:
        print("❌ Invalid choice! Enter 1 to 5.")