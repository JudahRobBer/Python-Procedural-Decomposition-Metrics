

# The spire function prints the top of the tower and calls both repeat functions which prints the repeated elements
def spire() -> None:
    repeats_1()
    repeats_2()
    print(" (_)()()()()(_)")
    print("   (_)()()(_)")
# The repeats_1 function prints repeated elements seen thorugh out each structure of the tower

def repeats_1() -> None:
    print("       ||   ")
    print("       ||   ")
# The repeats_2 function prints repeated elements seen thorugh out each structure of the tower 
def repeats_2() -> None:
    print("    __{{}}__")
    print(" __{::::::::}__")
    print(" ||||||||||||||")
    
# The middle function prints the middle of the tower and calls the repeats_1 function which prints the repeated elements
def middle() -> None:
    print("   ____][____")
    print("    ___][___ ")
    repeats_1()
  
    
# The base functions prints the base of the tower by calling the repeats_2 function which prints the repeated elements
def base() -> None:
    print("    |%%%%%%| ")
    print("    |%%%%%%| ")
    print("    |%%%%%%| ")
    print("    |%%%%%%| ")
    repeats_2()
    
# The main function calls the spire, middle, and base function in order to print the entire tower
def main() -> None:
    spire()
    middle()
    base()
    
main()