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


if __name__ == "__main__":
    main()
