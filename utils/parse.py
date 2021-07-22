def create_runtime_user(obj):
    exec("from entities.User import User")
    return eval("User")(**obj)
