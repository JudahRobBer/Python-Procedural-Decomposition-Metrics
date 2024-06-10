

def spire(): #This is called twice: once in beginning and once in the middle
    x = 0
    for x in range(2): #Repeated twice
        print("      ||      ")
        x+=1
    
def topshell_base(): #This is called twice as well
    print("   __{{}}__   ")
    print("__{::::::::}__")
    print("||||||||||||||")

def middle(): #Makes up majority of tower structure
    print("(_)()()()()(_)")
    print("  (_)()()(_)  ")
    print("  ____][____  ")
    print("   ___][___   ")
    spire()
    x = 0
    for x in range(4):
        print("   |%%%%%%|   ") #Repeated 4 times
        x+=1

def main():
    spire()
    topshell_base()
    middle()
    topshell_base()
    
    
main() #One main function