

#define parts of the tower
def base() -> None:
    print("   __{{}}__")
    print("__{::::::::}__")
    print("||||||||||||||")
def spire() -> None:
    print("      ||")
    print("      ||")
def lowermiddle() -> None:
    print("   |%%%%%%|")
    print("   |%%%%%%|")
    print("   |%%%%%%|")
    print("   |%%%%%%|")
def uppermiddle() -> None:
    print("(_)()()()()(_)")
    print("  (_)()()(_)")
    print("  ____][____")
    print("   ___][___")

#define the main function for building the tower out of parts
def main() -> None:
    spire()
    base()
    uppermiddle()
    spire()
    lowermiddle()
    base()
    
#run the main function
main()