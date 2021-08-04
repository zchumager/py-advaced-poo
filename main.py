from utils.parse import create_runtime_user

from pprint import pprint
from utils import unpack


def main():
    users = []

    obj = {'username': 'pmachado', 'email': 'pmachado@tripwire.com'}

    username, email = unpack.params_unpacking(**obj)
    print(username, email)

    user = unpack.constructor_unpacking(obj)
    pprint(user)

    runtime_user = create_runtime_user(obj)
    pprint(runtime_user)

    users.append(user)
    user_list = unpack.generic_list_to_type_list(users)
    pprint(user_list)

    lang = "Python"
    string_format = "fstring"
    subject = "you"
    letter = "f"

    msg = (f"this is the way how {lang} "
           f"can handle multiple {string_format} lines, "
           f"so in this way {subject} can type as many lines "
           f"as {subject} need with a proper format"
           f"given by {string_format} just using the "
           f"{letter} preffix")
    print(msg)

# create a project called advaced python topic to add all you have learn these days


if __name__ == "__main__":
    main()
