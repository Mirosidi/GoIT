def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: add username phone"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: change username phone"
    name, phone = args
    if name not in contacts:
        return "Invalid command.Contact not found."
    contacts[name] = phone
    return "Contact updated"


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Usage: phone username"
    name = args[0]
    if name not in contacts:
        return "Invalid command. Contact not found"
    return f"The phone number for {name} is {contacts[name]}."


def show_all(contacts):
    if not contacts:
        return "Invalid command.No contacts found"
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}

    while True:
        user_input = input("Enter command: ").strip().lower()
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "close" or command == "exit":
            print("Good bye!")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
