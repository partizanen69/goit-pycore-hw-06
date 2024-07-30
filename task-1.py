def input_error(func):
    def inner(*args, **kwargs):
        try:
          return func(*args, **kwargs)
        except ValueError:
          return "Enter the argument for the command"
        except KeyError:
          return "Contact does no exist"
        except IndexError as e:
          return f"I have no idea where this error can occur in the existing code, but here is the error: {e}"

    return inner

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts: dict):
    name, phone = args
    if not name or not phone:
      raise ValueError()
    
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts: dict):
  name, phone = args
  if not name or not phone:
    raise ValueError()

  existing_phone = contacts.get(name)
  if not existing_phone:
    return f"contact with name {name} does not exist"
  
  contacts[name] = phone
  return "Contact updated."

@input_error
def show_phone(args, contacts: dict):
  [name] = args
  if not name:
    raise ValueError()
  
  return contacts[name]

def show_all(contacts: dict):
  if not contacts.keys():
    return "There is no contacts in the list"
  
  result = []
  for name, phone in contacts.items():
    result.append(f"{name} {phone}")
  return "\n".join(result)


def main():
  print("Welcome to the assistant bot!")
  contacts = {}

  while True:
    user_input = input().strip()
    command, *args = parse_input(user_input)

    if command in ["close", "exit"]:
      print("Good bye!")
      break
    elif command == 'hello':
      print('How can I help you?')
    elif command == 'add':
      print(add_contact(args, contacts))
    elif command == 'change':
      print(change_contact(args, contacts))
    elif command == 'phone':
      print(show_phone(args, contacts))
    elif command == 'all':
      print(show_all(contacts))
    else:
      print("Invalid command.")

      
if __name__ == '__main__':
  main()


# Enter a command: add
# Enter the argument for the command
# Enter a command: add Bob
# Enter the argument for the command
# Enter a command: add Jime 0501234356
# Contact added.
# Enter a command: phone
# Enter the argument for the command
# Enter a command: all
# Jime: 0501234356 
# Enter a command:
