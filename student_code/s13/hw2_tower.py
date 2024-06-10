

def spire()-> None: #Defined as a function for reusibility in building the tower
    for i in range(2): #I didn't necessarily need a for loop to repeat the same line twice, but I'm having fun practicing
        print(" "*5,"||")
        i+=1
    
def topshell_and_base()-> None: #Define as a function in order to reuse in the main function while building the tower
    print(" "*3+"__{{}}__")
    print("__{"+":"*8+"}__")
    print("|"*14)
    
def bottomshell()-> None:
    print("(_)"+"()"*4+"(_)")
    print(" "*2+"(_)"+"()"*2+"(_)")
    print(" "*2+"_"*4+"]["+"_"*4)
    print(" "*3+"_"*3+"]["+"_"*3)
          
def middle()-> None: #I used a for loop to reduce repetition of the same print statement
    for i in range(4):
        print("   |%%%%%%|")
        i+=1

def main()-> None:
    spire()
    topshell_and_base()
    bottomshell()
    spire()
    middle()
    topshell_and_base()

main()


