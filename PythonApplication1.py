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

    print("The sum is", x + y)
    if x < y:
        print("The difference is", y - x)
    else:
        print("The difference is", x - y)
    print("Division:", x / y)
    print("Multiplication:", x * y)

def readcsv():
    print("open stuff...\nDo stuff...\ninsert bugs.........")

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

intro()