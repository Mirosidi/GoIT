contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added.")

def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def parse_input(input_str):
    parts = input_str.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main():
    print("How can I help you?")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command == "exit" or command == "close" or command == "stop":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                add_contact(args[0], args[1])
            else:
                print("Invalid command format. Use: add [name] [phone]")
        elif command == "change":
            if len(args) == 2:
                change_contact(args[0], args[1])
            else:
                print("Invalid command format. Use: change [name] [new_phone]")
        elif command == "phone":
            if len(args) == 1:
                show_phone(args[0])
            else:
                print("Invalid command format. Use: phone [name]")
        elif command == "all":
            show_all()
        else:
            print("Invalid command. Type 'hello' for help.")

if __name__ == "__main__":
    main()