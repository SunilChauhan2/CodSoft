print("         CONTACT BOOK        ")

class ContactBook:    #class defining
    
    def __init__(self):   #function for self_contact
        self.contacts = {}

    def add(self):   #function for add option
        name = input("Enter name: ")
        self.contacts[name] = {
            "phone": input("Enter phone number: "),
            "email": input("Enter email: "),
            "address": input("Enter address: ")
        }

    def view(self):    #function for view option
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

    def search(self):    #function for search option
        term = input("Enter name or phone: ")
        for name, details in self.contacts.items():
            if term.lower() in name.lower() or term in details["phone"]:
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def update(self):    #function for updating a contact option
        name = input("Enter name to update: ")
        if name in self.contacts:
            self.contacts[name]["phone"] = input("Enter new phone: ")
            self.contacts[name]["email"] = input("Enter new email: ")
            self.contacts[name]["address"] = input("Enter new address: ")

    def delete(self):    #function for delete option
        name = input("Enter name to delete: ")
        if name in self.contacts:
            del self.contacts[name]

def main():
    book = ContactBook()
    while True:
        print("\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
        choice = input("Enter choice: ")    #choice for user 
        if choice == "1":
            book.add()
        elif choice == "2":
            book.view()
        elif choice == "3":
            book.search()
        elif choice == "4":
            book.update()
        elif choice == "5":
            book.delete()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()