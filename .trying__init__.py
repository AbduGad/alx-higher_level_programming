#!/usr/bin/python3
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

            
user = User()
user.is_new = True
print(user.is_new)
print(user.id)
integer = int(1)
print(integer.__dict__)
print(int.__dict__)