

# Devide the whole text-art pattern to four parts: spire, topshell, base, and middle.
def spire() -> None:
    print("      ||      ")
   
def bottomshell() -> None:
    print("   __{{}}__   ")
    print("__{::::::::}__")
    print("||||||||||||||")
    
def base() -> None:
    print("(_)()()()()(_)")
    print("  (_)()()(_)  ")
    print("  ____][____  ")
    print("   ___][___   ")
    
def middle() -> None:
    print("   |%%%%%%|   ")

# Now, by calling different parts with the sequence of output, we are able to get the pattern.
def main() -> None:
    spire()
    spire()
    bottomshell()
    base()
    spire()
    spire()
    middle()
    middle()
    middle()
    middle()
    bottomshell()
    
main()