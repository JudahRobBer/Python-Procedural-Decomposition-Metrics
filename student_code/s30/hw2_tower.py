

def spire() -> None:     #spire design     
    print("      ||")
    print("      ||")

def middle() -> None:  #middle design
    print("(_)()()()()(_)")
    print("  (_)()()(_)")
    print("  ____][____")
    print("   ___][___")
    
def bottom() -> None: #bottomshell
    for x in range(4):
        print("   |%%%%%%|")

def base() -> None:  #base
    print("   __{{}}__")
    print("__{::::::::}__")
    print("||||||||||||||")

def main() -> None:  #call functions
    spire()
    base()
    middle()
    spire()
    bottom()
    base()
    
main()