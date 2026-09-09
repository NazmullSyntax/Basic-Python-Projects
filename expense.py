import json
from datetime import datetime

expenses = []

def add_expense():
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = datetime.now().strftime("%Y-%m-%d")
    expenses.append({"amount": amount, "category": category, "date": date})
    save_expenses()

def view_summary():
    total = sum(e['amount'] for e in expenses)
    print(f"Total: ${total}")
    
    categories = {}
    for e in expenses:
        categories[e['category']] = categories.get(e['category'], 0) + e['amount']
    for cat, total in categories.items():
        print(f"{cat}: ${total}")

def save_expenses():
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)

# Main loop
while True:
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == '1': add_expense()
    elif choice == '2': view_summary()
    elif choice == '3': break