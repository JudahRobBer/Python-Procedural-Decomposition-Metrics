

#indiviudal parts of the tower: spire, topshell, bottomshell, and middle
def spire()->None:
    print("      ||")
    print("      ||")
    
def topshell()->None:
    print("   __{{}}__")
    print("__{::::::::}__")
    print("||||||||||||||")
    
def bottomshell()->None:
    print("(_)()()()()(_)")
    print("  (_)()()(_)")
    print("  ____][____")
    print("   ___][___")
    
def middle()->None:
    print("   |%%%%%%|")
    

#tower put together
def tower()->None:
    spire()
    topshell()
    bottomshell()
    spire()
    middle()
    middle()
    middle()
    middle()
    topshell()

#main function to act as entry point into program
def main()-> None:
    tower()
    
main()
