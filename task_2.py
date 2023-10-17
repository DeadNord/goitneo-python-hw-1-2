def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Need 2 args"


def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact changed."
        else:
            return "Contact not found"
    except ValueError:
        return "Need 2 args"


def phone_contact(username, contacts):
    try:
        if username in contacts:
            return f"Phone of {username}: {contacts[username]}"
        else:
            return "Contact not found"
    except TypeError:
        return "Need only String: UserName"


def all_contact(contacts):
    res = f"\nAll phones:\n"
    for key, value in contacts.items():
        res += f"{key}: {value}\n"
    return res


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args[0], contacts))
        elif command == "all":
            print(all_contact(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
