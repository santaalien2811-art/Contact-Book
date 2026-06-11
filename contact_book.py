contacts = []
def show_menu():
    print("\n*******************************Contacts Book*******************************")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete contact")
    print("6. Exit")

def add_contact():
 name = input("Enter name: ")
 number = input("Enter number: ")
 email = input("Enter email: ")
 for contact in contacts:
     if contact['name'].lower() == name.lower() or contact['number'] == number:
         print("Contact already exist")
         return

 contact = {
     "name":name,
     "number":number,
     "email":email
 }        

 contacts.append(contact)
 print(f"Contact {contact['name']} has been added ")

def view_contact():
    if not contacts:
        print("No contacts yet!")
        return
    
    print(f"\n============You have total of {len(contacts)} contacts ============")
    for index, contact in enumerate(contacts, start=1):
        print(f"\n{index}. {contact['name']}")    
        print(f"Phone: {contact['number']}")
        print(f"Email: {contact['email']}")

def search_contact():
    if not contacts:
        print("No contacts yet!")
        return
    name_number = input("Enter contact name or number: ").lower()        
    found = False
    for contact in contacts:
         if name_number == contact['name'].lower() or name_number == contact['number']:
            print("\nContact Found!")
            print(f"name: {contact['name']}")
            print(f"Phone: {contact['number']}")
            print(f"Email: {contact['email']}")
            found = True
            break
    if not found:
     print("Contact not found!")   

def edit_contact():
   view_contact()
   if not contacts:
      return
   try:
        index = int(input("Choose contact number: ")) -1
        if 0<= index < len(contacts):
            new_name = input("Enter new name: ")
            new_number = input("Enter new number: ")
            new_email = input("Enter new email: ")
            contacts[index]["name"] = new_name
            contacts[index]["number"] = new_number
            contacts[index]["email"] = new_email
            print("Contact updated!")
        else:
         print("Contact does not exist!")
   except ValueError:
      print("Invalid number!")
            

def delete_contact():
    view_contact()
    if not contacts:
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
     choice = int(input("Enter an option (1-6): "))
    
     if choice == 1:
        add_contact()
     elif choice == 2:
        view_contact()
     elif choice == 3:
        search_contact()
     elif choice == 4:
        edit_contact()
     elif choice == 5:
        delete_contact()
     elif choice == 6:
        print("Goodbye!")
        break
     else:
        print("Invalid choice!")
    except ValueError:
        print("Invalid choice!")

        
        
        


            
