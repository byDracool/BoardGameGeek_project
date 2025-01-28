from user import User

#Vars
USER = []


def create_user(username: str):
    user = User(username)
    global USER
    USER.append(user)
    print(USER)


create_user("byDracool")