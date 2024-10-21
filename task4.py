def input_error(func):
    # decorator to handle input errors
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such contact found."
        except IndexError:
            return "Enter the correct number of arguments."
    return inner

@input_error
def add_contact(args, contacts):
    # function to add a contact
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    # function to get the phone number of a contact
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def show_all(args, contacts):
    # function to show all contacts
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    # main function to run the bot
    contacts = {}
    commands = {
        "add": add_contact,
        "phone": get_phone,
        "all": show_all
    }

    while True:
        command = input("Enter a command: ").strip().lower()
        if command in ("exit", "close", "goodbye"):
            print("Goodbye!")
            break
        elif command in commands:
            args = input("Enter the argument for the command: ").split()
            handler = commands[command]
            print(handler(args, contacts))
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()