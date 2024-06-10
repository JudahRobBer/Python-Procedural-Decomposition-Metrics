

#Functions breaks tower into different parts, to be called later.
def spire():
    print("       ||   ")
    print("       ||   ")
    print("    __{{}}__")
    
def top():
    print(" __{::::::::}__")
    print(" ||||||||||||||")
    print(" (_)()()()()(_)")
    print("   (_)()()(_)")
    print("   ____][____")
    print("    ___][___")
    
def middle():
    print("       ||")
    print("       ||")
    print("    |%%%%%%|")
    print("    |%%%%%%|")
    print("    |%%%%%%|")
    print("    |%%%%%%|")

def bottom():
    print("    __{{}}__")
    print(" __{::::::::}__")
    print(" ||||||||||||||")
    
#main() calls the 4 functions in order to print the tower
def main():
    spire()
    top()
    middle()
    bottom()
   
main()