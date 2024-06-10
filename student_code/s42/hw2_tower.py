

# This function creates the code necessary to print the topshell and base in the tower
def topshell_base ():
    print("   __{{}}__")
    print("__{::::::::}__")
    print("||||||||||||||")
    
# spire is used for printing the spire in the tower    
def spire ():
    print("      ||")
    print("      ||")
    
# bottomshell creates code for printing the bottomshell in the tower    
def bottomshell ():
    print("(_)()()()()(_)")
    print("  (_)()()(_)")
    print("  ____][____")
    print("   ___][___")
    
# middle creates code for printing the middle of the tower
def middle ():
    print("   |%%%%%%|")
    print("   |%%%%%%|")
    print("   |%%%%%%|")
    print("   |%%%%%%|")
    
def main ():
    spire()
    topshell_base()
    bottomshell()
    spire()
    middle()
    topshell_base()
    
main()
    

