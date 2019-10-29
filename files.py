#File IO practice

#functions
def createFile(fileName):
    file = open(fileName + ".txt", "w")
    print("Output file: ", file.name, " created!")
    file.close()
    return file

def writeFile(file):
    file = open(file.name, "a+")
    lineCount = 1
    print("Type \"!quit\" to stop writing.\n")
    while 1:
        line = input("Line " + str(lineCount) + ": ")
        if line == "!quit":
            print("You wrote ", str(lineCount - 1), " lines!\n")
            break
        else:
            line += "\n"
            file.write(line)
            lineCount += 1
    file.close()
    return

def readFile(file):
    file = open(file.name, "r")
    print(file.name, ": \n")
    for line in file:
        print(line)
    file.close()
    return

def clearFile(file):
    file = open(file.name, "w")
    file.close()
    print("Output file: ", file.name, " cleared.\n")
    return


#main
file1 = createFile("output")
clearFile(file1)
writeFile(file1)
readFile(file1)
