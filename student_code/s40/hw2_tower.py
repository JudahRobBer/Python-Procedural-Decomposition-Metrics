

# function that prints the spire of the tower
def spire() -> None:
    print("      ||      ")
    print("      ||      ")

# function that prints the topshell of the tower
def topshell() -> None: 
    print("   __{{}}__   ")
    print("__{::::::::}__")
    print("||||||||||||||")

# function that prints the middle part of the tower
def middle() -> None:
    print("(_)()()()()(_)")
    print("  (_)()()(_)  ")
    print("  ____][____  ")
    print("   ___][___   ")

# function that prints the bottom part of the tower
def bottom() -> None:
    print("   |%%%%%%|   ")

# function that assembles and prints the entire tower
def main() -> None:
    spire()
    topshell()
    middle()
    spire()
    bottom()
    bottom()
    bottom()
    bottom()
    topshell()

# execute the main function when the program is run
main()