
# I'm from seattle, and this looks like the space needle, so I
# may name some things as parts of the space needle

def vertical_bars():
    print("|"*15)
def needle():
    print(" "*6 + "||")
    
def viewing_deck():
    print("   __{{}}__")
    print("__{::::::::}__")
    vertical_bars()
    print("(_)()()()()(_)")
    print("  (_)()()(_)")
    print("  ____][____")
    print("   ___][___")


def lower_deck():
    i = 0
    while i < 4:
        print("   |" + "%"*6 + "|")
        i += 1

def base():
    print("   __{{}}__")
    print("__{::::::::}__")
    vertical_bars()

needle()
viewing_deck()
lower_deck()
base()
