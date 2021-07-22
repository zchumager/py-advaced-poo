from entities.User import User
from entities.Collection import Collection


def params_unpacking(username='default', email=''):
    return username, email


def dict_unpacking(obj):
    return {**obj}


def constructor_unpacking(obj):
    return User(**obj)


def generic_list_to_type_list(l):
    return Collection(l)