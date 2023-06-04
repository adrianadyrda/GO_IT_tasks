DATA = {}


def input_error(func):
    def inner_func(command):
        try:
            result = func(command)
            return result
        except KeyError:
            print('No such key')
        except ValueError:
            print('No such value')
        except IndexError:
            print('Wrong command')
    return inner_func


@input_error
def add_name(command):
    info = command.split()
    name = info[1]
    phone = info[2]
    DATA[name] = phone


@input_error
def change_name(command):
    info = command.split()
    name = info[1]
    phone = info[2]
    if DATA.get(name) is None:
        print('No such name')
    else:
        DATA[name] = phone


@input_error
def get_phone(command):
    name = command.split()[1]
    phone = DATA[name]
    return phone


def main():

    while True:
        command = input().lower()
        if command in ["good bye", "close", "exit"]:
            print('Good bye')
            break
        elif command == 'hello':
            print("How can I help you?")
        elif command.startswith('add'):
            add_name(command=command)
        elif command.startswith('change'):
            change_name(command=command)

        elif command.startswith('phone'):
            print(get_phone(command=command))

        elif command == 'show all':
            if len(DATA.keys()) == 0:
                print('No data')
            for key in DATA.keys():
                value = DATA[key]
                print(f'{key}: {value}')
        else:
            print('Sorry, no such command')


if __name__ == '__main__':
    main()

