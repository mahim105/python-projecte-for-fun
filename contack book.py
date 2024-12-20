contact_book = {}

def create_contact():
    name = input('Enter your name: ')
    if name in contact_book:
        print(f'Contact name {name} already exists.')
    else:
        age = int(input('Enter your age: '))
        email = input('Enter your email: ')
        mobile = input('Enter your mobile number: ')  # Keep as a string
        
        contact_book[name] = {
            'age': age,
            'email': email,
            'mobile': mobile
        }
        print(f'Contact {name} has been created successfully.')

def view_contacts():
    if not contact_book:
        print('No contacts found.')
    else:
        print('Contacts:')
        for name, details in contact_book.items():
            print(f'Name: {name}, Age: {details["age"]}, Email: {details["email"]}, Mobile: {details["mobile"]}')

def update_contact():
    name = input('Enter the name of the contact to update: ')
    if name in contact_book:
        age = int(input('Enter the new age: '))
        email = input('Enter the new email: ')
        mobile = input('Enter the new mobile number: ')
        contact_book[name] = {
            'age': age,
            'email': email,
            'mobile': mobile
        }
        print(f'Contact {name} updated successfully.')
    else:
        print(f'Contact {name} not found.')

def delete_contact():
    name = input('Enter the name of the contact to delete: ')
    if name in contact_book:
        del contact_book[name]
        print(f'Contact {name} deleted successfully.')
    else:
        print(f'Contact {name} not found.')

def search_contact():
    name = input('Enter the name of the contact to search: ')
    if name in contact_book:
        details = contact_book[name]
        print(f'Contact found: Name: {name}, Age: {details["age"]}, Email: {details["email"]}, Mobile: {details["mobile"]}')
    else:
        print(f'Contact {name} not found.')

def count_contacts():
    print(f'Total contacts: {len(contact_book)}')

def main():
    while True:
        print('\nContact Book App')
        print('1. Create Contact')
        print('2. View Contacts')
        print('3. Update Contact')
        print('4. Delete Contact')
        print('5. Search Contact')
        print('6. Count Contacts')
        print('7. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            create_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            update_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            search_contact()
        elif choice == 6:
            count_contacts()
        elif choice == 7:
            print('Exiting the program.')
            break
        else:
            print('Invalid input. Please enter a number between 1 and 7.')

if __name__ == "__main__":
    main()
