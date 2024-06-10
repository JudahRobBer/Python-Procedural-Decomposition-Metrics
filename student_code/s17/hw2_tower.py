
#Begin by breaking up the tower into different parts
#create a function for each part of the tower

def middle() -> None:
    print("      ||      ")
    print("      ||      ")
    
def spire() -> None:
    print("   __{{}}__   ")
    print("__{::::::::}__")
    print("||||||||||||||")
    
def topshell() -> None:
    print("(_)()()()()(_)")
    print("  (_)()()(_)  ")
    print("  ____][____  ")
    print("   ___][___   ")
    
def bottomshell() -> None:
    print("   |%%%%%%|   ")
    print("   |%%%%%%|   ")
    print("   |%%%%%%|   ")
    print("   |%%%%%%|   ")
    
def main():
    middle()
    spire()
    topshell()
    middle()
    bottomshell()
    spire()
    
main()
    

    

    
   
    
    