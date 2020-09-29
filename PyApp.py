from time import sleep

cmds = {
    "calcs": ["calcs", "calc", "cal", "calclist", "calcli", "calculations", "calculate"],
    "printfile" : ["printfile", "read", "print", "file", "readfile"],
    "slots": ["slots", "slot", "sl"],
    "help": ["help", "h", "?", "commands", "cmds", "commandlist", "commandli", "cmdlist", "cmdli"],
    "exit": ["exit", "quit", "end"]
    }

cmdesc = {
    "calcs": ["This command prints the calculations' +, -, * and / ' between two numbers",
              ["calcs", "calc", "cal", "calclist", "calcli", "calculations", "calculate"]],

    "printfile" : ["This command prints the content of a file with a given path",
                   ["printfile", "read", "print", "file", "readfile"]],

    "slots": ["You can play slots with this command (WIP)", ["slots", "slot", "sl"]],

    "help": ["""This command shows the aliases of either all commands
    or more detailed help on a single command, if you provide the name""",
             ["help", "h", "?", "commands", "cmds", "commandlist", "commandli", "cmdlist", "cmdli"]],

    "exit": ["Guess what this command does...", ["exit", "quit", "end"]]
    }

ver = "'beta 1.0'"

bal = 1000



def typewrite(*value, delay=0.015, sep=" ", end="\n"):
    r"""typewrite(value, delay=0.02, sep=" ", end="\n")

Prints the given values with a delay between each character.
This creates a nice typewriter effect.

    value: the value you want to have typed out
    delay: the delay between each character in seconds, default: 0.02 seconds
    sep: string inserted between values, default: a space
    end: string appended after the last value, default: a newline"""

    for elm in value:
        for c in str(elm):
            sleep(delay)
            print(c, end="")
        if elm != value[-1]:
            print(end=sep)
    sleep(delay)
    print(end=end)



def cmdline():
    return input("> ").lower().strip()

def whatcmd(cmdstr):
    if cmdstr is not "":
        args = cmdstr.split()
        cmd = args[0]
        
        # if cmd is in the list of x, run function for x
        if   cmd in cmds["calcs"]:    declicalcs(args)
        elif cmd in cmds["printfile"]: printfile(args)
        elif cmd in cmds["slots"]:         slots(args)
        elif cmd in cmds["help"]:           help(args)
        elif cmd == "info": (print("Version:", ver, end="\n> "), sleep(2), typewrite("\rMaybe I'll be a discord bot one day..."), sleep(0.5), typewrite("...", delay=0.3), sleep(0.5), typewrite("WAIT THATS BAD..."), sleep(0.5), typewrite("or is it?", delay=0.1, end="\n\n"))
        elif cmd in cmds["exit"]:
            return (typewrite("Goodbye!", delay=0.1), sleep(1))

        else: 
            typewrite("I'm sorry, I don't know what you want. Try 'help'.")

    whatcmd(cmdline())



def declicalcs(args):
    if len(args) == 1:
        typewrite("Which numbers would you like to use?")
        (cmdline()).split().insert(0, "calcs")
    elif len(args) == 2:
        typewrite("You need to use two numbers.")
    else:
        try:
            listcalcs(int(args[1]),int(args[2]))
        except:
            try:
                listcalcs(float(args[1].replace(",", ".")), float(args[2].replace(",", ".")))
            except:
                typewrite("Invalid input")

def listcalcs(x, y):
    """the four normal calculations with two numbers"""
    print(x, "+", y, "=", round(x + y, 12))
    print(x, "-", y, "=", round(x - y, 12))
    print(x, "*", y, "=", round(x * y, 12))
    print(x, "/", y, "=", round(x / y, 12))
    print()



def printfile(args):
    path = " ".join(args[1:])
    exts = ["csv", "txt"]
    if path.split(".")[-1] not in exts:
        print("""Please only""", " & ".join(ext), """files!
I have no Idea what harmful things could happen,
if the program tried to open other file types.""")
        return

    try:
        print("opening...")
        file = open(path, "r")
    except:
        print("something went wrong")

    if file.mode == "r":
        print("reading...")
        file.content = file.read()
        print(file.content)
        print("That's it... That's all it can do so far...")



def slots(args):
    global bal
    amt = None
    # did user specify an amount?
    try:
        args[1]
    except:
        typewrite("How much credits would you like to use?")
        args.append(cmdline().split()[0])
    # check if amt can be an int. if True, assign the value to amt
    # don't if user doesn't have enough credits
    try:
        amt = int(args[1])
        if amt > bal:
            return typewrite("You don't have enough credits.")
    except:
        try:
            float(amt)
            return print("Amount must be a whole number")
        except:
            return print("Amount is not a number")
    from random import randint

    symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "$", "%", "&", "?", "#"]

    print("--- S - L - O - T - S ---\n")
    bal -= amt
    print("Balance:", bal)
    print("    ╔═══╤═══╤═══╗")
    for i in range(0, randint(12, 15)):
        a = b = c = symbols[randint(0, len(symbols)-1)]
        print("\r    ║", a, "│", b, "│", c, "║", end="")
        #print("\r    ╚═══╧═══╧═══╝", end="")
        sleep(0.1)
    for j in range(0, randint(12, 15)):
        b = c = symbols[randint(0, len(symbols)-1)]
        print("\r    ║", a, "│", b, "│", c, "║", end="")
        #print("\r    ╚═══╧═══╧═══╝", end="")
        sleep(0.1)
    for k in range(0, randint(12, 15)):
        c = symbols[randint(0, len(symbols)-1)]
        print("\r    ║", a, "│", b, "│", c, "║", end="")
        #print("\r    ╚═══╧═══╧═══╝", end="")
        sleep(0.1)
    print("\n    ╚═══╧═══╧═══╝")

    if a == b and b == c:
        print("BIG WIN, Pog MOMENT")
        bal += amt*100
        typewrite("You spent", amt, "and won", amt*100, "!!!")
    elif a == b or a == c or b == c:
        typewrite("POGGERS", delay=0.03)
        bal += amt*10
        typewrite("You spent", amt, "and won", amt*10, "!", delay=0.03)

    else:
        typewrite("uno momento de bruh", delay=0.05)
        typewrite("You spent", amt, "and lost everything.", delay=0.05)
    typewrite("Your balance is now", bal)



def help(args):
    if len(args) == 1:
        print("\n--- H - E - L - P ---\n")
        sleep(0.1)
        print("Here are all comands and their aliases:")
        sleep(0.1)
        print("     help:", cmds["help"])
        print("    calcs:", cmds["calcs"])
        print("printfile:", cmds["printfile"])
        print("    slots:", cmds["slots"])
        print("     exit:", cmds["exit"])
        print()
    elif args[1] in cmdesc["help"][1]:      helpdesc(cmdesc["help"])
    elif args[1] in cmdesc["calcs"][1]:     helpdesc(cmdesc["calcs"])
    elif args[1] in cmdesc["printfile"][1]: helpdesc(cmdesc["printfile"])
    elif args[1] in cmdesc["slots"][1]:     helpdesc(cmdesc["slot"])
    elif args[1] in cmdesc["exit"][1]:      helpdesc(cmdesc["exit"]) 
    else:
        typewrite("This command does not exist")

def helpdesc(key):
    typewrite(key[0])
    print("Aliases for this command:")
    print("   ", key[1])




# start the program

typewrite("Hello.", delay=0.05, end=" ")
sleep(0.2)

typewrite("What would you like to do?")
sleep(0.2)

typewrite("Type 'help' for a list of commands.")

whatcmd(cmdline())
