

#To use as the spire or stem
def tip() -> None:
    print("      ||   ")
    print("      ||   ")

#To use as both the topshell/base and the bottomshell
def dome() -> None: 
    print("   __{{}}__")
    print("__{::::::::}__")
    print("||||||||||||||")

#To use as the middle/body of the tower
def body() -> None:
    print("(_)()()()()(_)")
    print("  (_)()()(_)")
    print("  ____][____")
    print("   ___][___")
    tip()
    print("   |%%%%%%|")
    print("   |%%%%%%|")
    print("   |%%%%%%|")
    print("   |%%%%%%|")
       
#Calling of all of the functions to construct the tower
def main() -> None:
   tip()
   dome() 
   body()
   dome()
    
main()