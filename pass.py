import time

class User:
    name = ""
    password = ""
    login_attempts = 0

    def __init__(self, name, password):
        self.name = name
        self.password = password
        login_attempts = 0

    def __str__(self):
        return "User: " + str(self.name)

userList = [] #list of registered users/accounts
currentUser = None #the user currently logged in

#actions
def wait():
    time.sleep(2)
    print("\n\n\n")
    
def createAccount():
    name = str(input("User name: "))
    password = str(input("Password: "))
    userList.append(User(name, password))
    print("User ", name, " created!")

def printUsers():
    print("Registered users: ")
    count = 1
    for user in userList:
        print(count, " ", user)
        count += 1

def login():
    name = str(input("User name: "))
    for user in userList:
        if name == user.name:
            #ask for password three times before breaking
            attempt = 0
            while attempt < 3:
                password = str(input("Password: "))
                if password == user.password:
                    print("Login success!")
                    global currentUser
                    currentUser = user
                    return 1
                else:
                    print("Incorrect password. Try again.")
                    attempt += 1
    print("User: ", name, "does not exist!")


#main input loop
while 1:
    #check if user is logged in
    if currentUser == None: 
        instring = "Guest > "
    else:
        instring = currentUser.name + " > "

    #input prompt    
    print("Would you like to... \n1) Create account\n2) Log in\n3) Print users\n4) Quit")
    request = input(instring)

    if request == "1": #create account
        createAccount()
        wait()

    elif request == "2": #log in
        login()
        wait()

    elif request == "3": #print users
        printUsers()
        wait()

    elif request == "4": #quit
        print("Exiting...")

        quit()
    else: #invalid input
        print("Invalid input\n")
        wait()
