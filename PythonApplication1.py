calcsli = ["c", "cal", "calc", "calcs", "calculator", "calculation", "calculations", "calculate", "1", "calcs()"]
readcsvli = ["csv", "readcsv", "2", "readcsv()"]
helpli = ["h", "help", "what", "?", "help()", "cmd", "cmds", "cmdlist"]
quitli = ["exit", "quit", "bye", "godbye", "goodbye", "cya", "fuck off"]

def calcs():
    """plus and minus with two numbers"""
    for i in range(3):
        try:
            x = float(input("Please enter a number: "))
            break
        except ValueError:
            print("Please input a valid number")
    try:
        z = x
        del z
    except NameError:
        return
    for i in range(3):
        try:
            y = float(input("Please enter a second number: "))
            break
        except ValueError:
            print("Please input a valid number")
    try:
        print("Your numbers:", x, "and", y)
    except NameError:
        return

    print(x, "+", y, "=", x + y)
    if x < y:
        print(x, "<- distance ->", y, "is", y - x)
    else:
        print(x, "<- distance ->", y, "is", x - y)
    print(x, "/", y, "=", x / y)
    print(x, "*", y, "=", x * y)

def readcsv():
    path = input("Please enter the path to your file > ").strip(' \'"')
    print(path)
    if path in quitli:
        return
    elif path in helpli:
        print("""To save your file path,
just right click your file while holding down shift
then click on 'Copy as path' and paste it in here.
Or type 'exit' to leave""")
        readcsv()
    elif path[-4:] != ".csv":
        print("""Please only csv files!
I have no Idea what harmful things could happen,
if the program tried to open other file types.""")
        print(path)
        readcsv()
        return
    print("opening...")
    file = open(path, "r")
    if file.mode == "r":
        print("reading...")
        file.content = file.read()
        print(file.content)

def help():
    print("--- H - E - L - P ---")
    print("help (this message):", helpli)
    print("              calcs:", calcsli[:7])
    print("                    ", calcsli[7:])
    print("            readcsv:", readcsvli)
    print("               quit:", quitli[:-1])

def terminal():
    print(">", end=" ")

    uinput = input().lower().strip()

    if uinput is "":
        pass
    elif uinput in calcsli:
        calcs()
    elif uinput in readcsvli:
        readcsv()
    elif uinput in helpli:
        help()
    elif uinput in quitli:
        print("Goodbye!\nPress ENTER...", end="")
        input()
        return
    else:
        print("I'm sorry, I don't know what you want. Try 'help'.")
    terminal()



def intro():
    print("Hello, would you like to calculate numbers or read a CSV file?")

    terminal()

if True:
    intro()
else:
    from time import sleep
    sleep(1)
    print(".", end=" ")
    sleep(.5)
    print(".", end=" ")
    sleep(.5)
    print(".", end="")
    sleep(.5)
    print()
    sleep(1)
    print("if you see this, something went horribly wrong")
    sleep(2)
    print("initiating self destruct...")
    sleep(2)
    print(3)
    sleep(1)
    print(2)
    sleep(1)
    print(1)
    sleep(1)