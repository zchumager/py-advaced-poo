from utils import unpack
from entities.User import User
from entities.Collection import Collection
from utils.parse import create_runtime_user


def test_unpack():
    users = []

    obj = {'username': 'pmachado', 'email': 'pmachado@email.com'}
    username, email = unpack.params_unpacking(**obj)

    assert username == obj['username'] and email == obj['email']

    user = unpack.constructor_unpacking(obj)
    assert type(user) == User

    runtime_user = create_runtime_user(obj)

    assert runtime_user.username == obj['username'] and runtime_user.email == obj['email']

    users.append(user)
    users_list = unpack.generic_list_to_type_list(users)
    assert type(users_list) == Collection
