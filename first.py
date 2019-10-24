#My first python program!
class User:
    #User has name and id number
    name = ""
    uid = 0

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def print_user(self):
        print("\nUser name: " + self.name)
        print("User ID: " + str(self.uid) + "\n")

#main
name = input("Howdy!\nInput your name: ")
user1 = User(name, 1)
user1.print_user()


