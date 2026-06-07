contacts = []
def show_menu():
    print("\n*******************************Contacts Book*******************************")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    email = input("Enter Email: ")

    contact = {
        "name":name,
        "number":number,
        "email":email
    }
    contacts.append(contact)
    print(f"Added contact: {contact['name']}")

def view_contact():
    if not contacts:
        print("No contacts yet!")
        return
    print("\n============Your Contacts============")
    for index, contact in enumerate(contacts, start=1):
        print(f"\n{index}. {contact['name']}")    
        print(f"Phone: {contact['number']}")
        print(f"Email: {contact['email']}")

def search_contact():
    if not contacts:
        print("There is no contacts!")
        return
    name = input("Enter contact name: ").lower()
    found = False
    for contact in contacts:
        if name == contact['name'].lower():
            print("\nContact Found!")
            print(f"name: {contact['name']}")
            print(f"Phone: {contact['number']}")
            print(f"Email: {contact['email']}")
            found = True
            break
        if not found:
            print("Contact not found!")   

def delete_contact():
    view_contact()
    if not contacts:
        print("No contacts to delete!")
        return
    try:
        index = int(input("Enter contact number to delete: ")) -1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Deleted contact {removed['name']}")
        else:
            print("Contact does not exist!")
    except ValueError:
        print("Invalid number!")

while True:
    show_menu()
    try:
     choice = int(input("Enter an option (1-5): "))
    
     if choice == 1:
        add_contact()
     elif choice == 2:
        view_contact()
     elif choice == 3:
        search_contact()
     elif choice == 4:
        delete_contact()
     elif choice == 5:
        print("GoodBye!")
        break
     else:
        print("Invalid choice!")
    except ValueError:
        print("Invalid choice!")
        


            