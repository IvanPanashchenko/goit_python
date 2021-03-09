def input_error(func):
    def inner(data):
        try:
            result = func(data)
            return result
        except KeyError:
            print("No user with such name")
        except ValueError:
            print("Give me name and phone ")
        except IndexError:
            print("Give me name and phone")
    return inner


def hello_bot(_):
    print("can I help you?")

USERS = {}


@input_error
def add_phone(data):
    name, phone = data[0], data[1]
    USERS[name] = phone
    print(f'{name} was added!')


@input_error
def change_phone(data):
    name, phone = data[0], data[1]
    for key in USERS.keys():
        if key == name:
            USERS[key] = phone
    print(f'The phone number for {name} was changed!')


@input_error
def show_phone(data):
    print(USERS[data[0]])


def show_all(_):
    for name, phone in USERS.items():
        print(f'{name} - {phone}')


def good_bye_bot(_):
    print("Good bye!")

def unknown_action(_):
    print('There is no such command!')

COMMANDS = {
    "hello" : hello_bot,
    "good bye": good_bye_bot,
    "close": good_bye_bot,
    "exit": good_bye_bot,
    "add" : add_phone,
    "change" : change_phone,
    "show" : show_phone,
    "show_all" : show_all
}


def input_handler(user_input):
    action = user_input.split(' ')[0]
    action = action.lower()
    data = user_input.split(' ')[1:]
    try:
        handler = COMMANDS[action]
    except KeyError:
        handler = unknown_action
        if not action or action == '.':
            handler = good_bye_bot

    return handler, data


def main():
    while True:
        cmd = input("Please type a command: ")
        handler, data = input_handler(cmd)
        try:
            handler(data)
        except KeyError:
            print('There is no such command')
main()