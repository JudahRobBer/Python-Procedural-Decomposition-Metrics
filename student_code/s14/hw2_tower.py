
#spire, topshell/base, bottomshell, middle

def spire() -> None:
    print ("      ||")
    print ("      ||")

def middle() -> None:
    spire()
    print ("   |%%%%%%|")
    print ("   |%%%%%%|")
    print ("   |%%%%%%|")
    print ("   |%%%%%%|")
    
def bottomshell() -> None:
    print ("   __{{}}__")
    print ("__{::::::::}__")
    print ("||||||||||||||")

def topshell() -> None:
    bottomshell()
    print ("(_)()()()()(_)")
    print ("  (_)()()(_)")
    print ("  ____][____")
    print ("   ___][___")

def main() -> None:
    spire()
    topshell()
    middle()
    bottomshell()

main()