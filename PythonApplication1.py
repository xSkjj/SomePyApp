calcsli = ["cal", "calc", "calcs", "calculator", "calculation", "calculations", "calculate", "1"]
readcsvli = ["csv", "readcsv", "2"]
slotsli = ["sl", "slt", "slts", "slot", "slots", "take my money", "shut up and take my money", "take my money bitch", "take my money, bitch"]
symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "$", "%", "&", "?", "#"]
helpli = ["h", "help", "what", "?", "what?", "cmd", "cmds", "cmdlist", "commands", "commandlist"]
quitli = ["end", "exit", "quit", "bye", "godbye", "goodbye", "cya", "no", "fuck off"]

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
        print(y, "-", x, "is", y - x)
    else:
        print(x, "-", y, "is", x - y)
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
        print("That's it... That's all it can do so far...")


def slots():
    from random import randint
    from time import sleep
    print("\n--------- S - L - O - T - S ---------\n")
    print('Welcome to "Slots", try "help", if you dont know what to do.\n')
    slinput = input("slots > ").lower().strip()
    if slinput in slotsli:
        print("    ┏━━━┳━━━┳━━━┓")
        for i in range(0, randint(12, 15)):
            sleep(.1)
            a = b = c = symbols[randint(0, len(symbols)-1)]
            #b = symbols[randint(0, len(symbols)-1)]
            #c = symbols[randint(0, len(symbols)-1)]
            print("    ┃", a, "┃", b, "┃", c, "┃", end="\r")
        for j in range(0, randint(12, 15)):
            sleep(.1)
            b = c = symbols[randint(0, len(symbols)-1)]
            #c = symbols[randint(0, len(symbols)-1)]
            print("    ┃", a, "┃", b, "┃", c, "┃", end="\r")
        for k in range(0, randint(12, 15)):
            sleep(.1)
            c = symbols[randint(0, len(symbols)-1)]
            print("    ┃", a, "┃", b, "┃", c, "┃", end="\r")
        print("\n", i)
        if a == b and b == c:
            print("loool\n")
        elif a == b or a == c or b == c:
            sleep(1)
            print("lool\n")
    elif slinput in helpli:
        print("    slots:", slotsli[:5])
        print("    slots [amount] to use the slot machine")
    elif slinput in quitli:
        return
    else:
        print("""I'm sorry, I don't know what you want. Try 'help',
or exit out of slots with 'exit' or 'quit'""")


def help():
    print("--- H - E - L - P ---")
    print("help (this message):", helpli)
    print("              calcs:", calcsli[:7])
    print("                    ", calcsli[7:])
    print("            readcsv:", readcsvli)
    print("               quit:", quitli[:-1])


def terminal():
    uinput = input("> ").lower().strip()

    if uinput is "":
        pass
    elif uinput in calcsli:
        calcs()
    elif uinput in readcsvli:
        readcsv()
    elif uinput in slotsli:
        slots()
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



# start the program

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
    print("3", end="")
    sleep(1)
    print("\r2", end="")
    sleep(1)
    print("\r1", end="")
    sleep(1)
    print("\r ", end="\r")