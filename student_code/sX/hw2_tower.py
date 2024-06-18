

def spire() -> None:
    print("      ||")
    print("      ||")
    
def topshell_base() -> None:
    print ("   __{{}}__")
    print("__{::::::::}__")
    print("||||||||||||||")    
        
def middle() -> None:
    print("(_)()()()()(_)")
    print("  (_)()()(_)")
    print("  ____][____")
    print("   ___][___")

def bottomshell() -> None:
    for i in [1,2,3,4]:
        print("   |%%%%%%|")
    #using a for loop to iterate this line mutliple times..
    #...instead of manually printing multiple lines of code

def main() -> None:
    spire()
    topshell_base()
    middle()
    spire()
    bottomshell()
    topshell_base()

main()
#fixed the issue (I had global code)
#now, all of the function calls are contained within main()