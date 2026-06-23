contacts = {}
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print("Contact added successfully!")
    elif choice == '2':
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, details in contacts.items():
                print("Name:", name)
                print("Phone:", details["Phone"])
                print("-" * 20)
    elif choice == '3':
        search = input("Enter name or phone number: ")
        found = False
        for name, details in contacts.items():
            if search == name or search == details["Phone"]:
                print("\nContact Found")
                print("Name:", name)
                print("Phone:", details["Phone"])
                print("Email:", details["Email"])
                print("Address:", details["Address"])
                found = True
                break
        if not found:
            print("Contact not found.")
    elif choice == '4':
        name = input("Enter name of contact to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contacts[name]["Phone"] = phone
            contacts[name]["Email"] = email
            contacts[name]["Address"] = address
            print("Contact updated successfully!")
        else:
            print("Contact not found.")
    elif choice == '5':
        name = input("Enter name of contact to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")
    elif choice == '6':
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please try again.")