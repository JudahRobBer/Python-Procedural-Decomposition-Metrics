

def spire()-> None: #prints two line columns
    i = 0
    while i < 2:
        print(6*(" ") + "||")
        i += 1

def top_shell()->None: #creates top shell and bottom for the pic
    print("   __{{}}__")
    print("__{" + 8*":" + "}__")
    print(14*"|")

def bottom_shell()->None: #makes bottom shell 
    print("(_)()()()()(_)")
    print("  (_)()()(_)")
    print("  ____][____")
    print("   ___][___")
    
def middle()->None: #creates middle section
    i=0
    while i < 4:
        print("   |%%%%%%|")
        i+=1
    
def main()->None: #runs functions to create picture
    spire()
    top_shell()
    bottom_shell()
    spire()
    middle()
    top_shell()

main()
