
# the function prints the spire section of the tower
def spire() -> None:
    print("      ||      ")
    print("      ||      ")
    
# the function prints the topshell section of the tower
def topshell() ->None:
    print("   __"+"{{"+"}}"+"__   ")
    print("__{::::::::}__")
    print("||||||||||||||")

# the function prints the middle section of the tower
def middle() -> None:
    print("(_)()()()()(_)")
    print("  (_)()()(_)  ")
    print("  ____][____  ")
    print("   ___][___   ")
    spire()
    
# the function prints the bottom of the tower
def bottom() -> None:
    print("   |%%%%%%|   ")

# the main function will process the functions below once it's called
def main() -> None:
    spire()
    topshell()
    middle()
    bottom()
    bottom()
    bottom()
    bottom()
    topshell()

# function call  
main()