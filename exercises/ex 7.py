import csv

class Contact:
    def __init__(self, name, phone):
        if not phone.isdigit():
            raise ValueError("Phone number should digit")
        self.name = name
        self.phone = phone

class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        new_contact = Contact(name, phone)
        self.contacts.append(new_contact)

    def save_to_csv(self, filename="contacts.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone"])
            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone])

    def load_from_csv(self, filename="contacts.csv"):
        self.contacts = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    try:
                        self.add_contact(row[0], row[1])
                    except ValueError:
                        continue
        except FileNotFoundError:
            pass

def run():
    phonebook = Phonebook()
    while True:
        print("\nChoose:")
        print("1. Add contact")
        print("2. Show all contacts")
        print("3. Save to file")
        print("4. Load from file")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            while True:
                phone = input("Enter phone number: ")
                try:
                    phonebook.add_contact(name, phone)
                    print(f"Contact {name} with phone {phone} added.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid phone number.")
        
        elif choice == '2':
            print("\nAll contacts:")
            for contact in phonebook.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")
        
        elif choice == '3':
            phonebook.save_to_csv("contacts.csv")
            print("Data saved to file.")
        
        elif choice == '4':
            phonebook.load_from_csv("contacts.csv")
            print("Data loaded from file.")
        
        elif choice == '5':
            print("Exiting the program...")
            break
        
        else:
            print("Please enter a valid choice.")

run()
