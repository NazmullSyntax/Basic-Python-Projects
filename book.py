import json

contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
    save_contacts()

def search_contact():
    name = input("Search name: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Not found")

def save_contacts():
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def load_contacts():
    try:
        with open('contacts.json', 'r') as f:
            return json.load(f)
    except:
        return {}

contacts = load_contacts()
while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == '1': add_contact()
    elif choice == '2': search_contact()
    elif choice == '3': break