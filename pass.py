class User:
    name = ""
    password = ""
    login_attempts = 0

    def __init__(self, name, password):
        self.name = name
        self.password = password
        login_attempts = 0

userList = []

def createAccount():
    name = str(input("User name: "))
    password = input("Password: ")
    userList.append(User(name, password))
    print("User ", name, " created!")

#main
createAccount()
print(userList)
