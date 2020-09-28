from time import sleep

cmds = {
    "calcs": ["calcs", "calc", "cal", "calclist", "calcli", "calculations", "calculate"],
    "printfile" : ["printfile", "read", "print", "file", "readfile"],
    "slots": ["slots", "slot", "sl"],
    "help": ["help", "h", "?", "commands", "cmds", "commandlist", "commandli", "cmdlist", "cmdli"],
    "exit": ["exit", "quit", "end"]
    }


def typewrite(value, delay=0.05, end="\n"):
    """typewrite(value, delay, end)

Type a given value with a delay between each character.
This creates a nice typewrite effect.

    value: the value you want to have typed out
    delay: the delay between each character in seconds, default: 0.05
    end: string appended after the last value, default: a newline"""

    for c in str(value):
        sleep(delay)
        print(c, end="")
    sleep(delay)
    print(end=end)



def cmdline():
    cmdstr = input("> ").lower().strip()

    # how do i turn this into one line
    try:
        cmd = cmdstr.split()[0]
    except:
        pass

    if cmdstr is "":
        pass
    elif cmd in cmds["calcs"]: listcalcs(args)
    elif cmd in cmds["printfile"]: printfile(args)
    elif cmd in cmds["slots"]: slots(cmdstr)
    elif cmd in cmds["help"]: help(cmdstr.split())
    elif cmd in cmds["quit"]:
        typewrite("Goodbye!", 0.1)
        sleep(1)
        return
    else:
        print("I'm sorry, I don't know what you want. Try 'help'.")

    cmdline()


def whatcmd():
    pass


def listcalcs(l):
    """all four main calculations with two numbers"""
    try:
        print(x, "+", y, "=", x + y)
        print(x, "-", y, "=", x - y)
        print(x, "*", y, "=", x * y)
        print(x, "/", y, "=", x / y)
    except:
        typewrite("something went wrong")


# {"printfile", "read", "print", "file", "readfile"}
def printfile(args):
    exts = ["csv", "txt"]
    if path.split(".")[-1] not in exts:
        print("""Please only""", " / ".join(ext), """files!
I have no Idea what harmful things could happen,
if the program tried to open other file types.""")
        printfile()
        return

    #if (diese datei existiert):
    print("opening...")
    file = open(path, "r")
    if file.mode == "r":
        print("reading...")
        file.content = file.read()
        print(file.content)
        print("That's it... That's all it can do so far...")
    #else:
        #print("This file does not exist")

# Guthaben
bal = 1000
def slots(args):
    try:
        amt = args[1]
    except:
        print("How credits would you like to use?")
    try:
        if int(amt) > bal:
            typewrite("You don't have enough credits")
            return
    except:
        try:
            float(amt)
            print("Amount must be a whole number")
        except:
            print("Amount is not a number")
    from random import randint
    symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "$", "%", "&", "?", "#"]
    print("--- S - L - O - T - S ---\n")
    print("    ╔═══╤═══╤═══╗")
    for i in range(0, randint(12, 15)):
        sleep(.1)
        a = b = c = symbols[randint(0, len(symbols)-1)]
        print("\r    ║", a, "│", b, "│", c, "║", end="")
    for j in range(0, randint(12, 15)):
        sleep(.1)
        b = c = symbols[randint(0, len(symbols)-1)]
        print("\r    ║", a, "│", b, "│", c, "║", end="")
    for k in range(0, randint(12, 15)):
        sleep(.1)
        c = symbols[randint(0, len(symbols)-1)]
        print("\r    ║", a, "│", b, "│", c, "║", end="")
    if a == b and b == c:
        print("BIG WIN, Pog MOMENT\n")
    elif a == b or a == c or b == c:
        sleep(1)
        print("uno momento de bruh\n")
    else:
        bal -= amt
        typewrite("You spent", amt, "and lost everything.")
        typewrite("Dumbass\r       \r", 0.01)


def help(args):
    if " ".join(args) in cmds["help"]:
        print("\n--- H - E - L - P ---\n")
        sleep(0.1)
        print("help (this message):")
        print("              calcs:")
        print("                    ")
        print("            readcsv:")
        print("               quit:")
        print()
    else:
        about = args[1]
        print("help about", about)




# start the program

typewrite("Hello.", end=" ")
sleep(0.2)

typewrite("What would you like to do?", 0.02)
sleep(0.2)

typewrite("Type 'help' for a list of commands.", 0.02)

cmdline()
