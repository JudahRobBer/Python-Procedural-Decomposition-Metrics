

def pole() -> None:
    print("      ||      ")
    print("      ||      ")

def middle() -> None:
    print("(_)()()()()(_)")
    print("  (_)()()(_)  ")
    print("  ____][____  ")
    print("   ___][___   ")

def bottomShell() -> None:
    for x in range(4):
        print("   |%%%%%%|   ")

def base() -> None:
    print("   __{{}}__   ")
    print("__{::::::::}__")
    print("||||||||||||||")
    
def tower() -> None:
    pole()
    base()
    middle()
    pole()
    bottomShell()
    base()

tower()