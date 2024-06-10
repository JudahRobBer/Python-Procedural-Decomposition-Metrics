
import random #Imports a built in module that can generate various random number functions
z = random.randrange(5,20,1) #Assign to z a random integer between 5-20 with a step size of one in order to generate the branch length

def print_crown()-> str: #These defined functions return string values
    x=(('  .-"-.  ')+z*" "+('  .-"-.  ')) #The line of code from the first owl is multiplied by the previously defined random int z
    return x #By defining the body parts of the owl separately, the code becomes more organized and concise

def print_eyes() -> str: 
    x= ((" / 4 4 \ ")+z*" "+(" / 4 4 \ ")) #The same line of code for the first owl is added after rand int z to make another owl 
    return x

def print_beak() -> str:
    x= ((" \_ v _/ ")+z*" "+(" \_ v _/ ")) #Z is multiplied by spaces, rather than =, because the output should show a branch only at the owl's feet
    return x

def print_chest() -> str:
    x= ((" //"+" "*3+"\\\ ")+z*" "+(" //"+" "*3+"\\\ ")) #I had to use 3 backslashes here bc python uses them to print special characters
    return x

def print_belly() -> str:
    x= ("(("+" "*5+"))"+z*" "+"(("+" "*5+"))")
    return x

def print_feet() -> str:
    x= (('=""===""=')+z*"="+'=""===""=') #Now, instead of multiplying z by " ", I multiplied by "=" because the branch is in between the feet
    return x

def print_tail() -> str:
    x= ((" "*3+"|||"+" "*3)+z*" "+(" "*3+"|||"+" "*3))
    return x

def print_two_owls() -> None:
    print(print_crown())
    print(print_eyes())
    print(print_beak())
    print(print_chest())
    print(print_belly())
    print(print_feet())
    print(print_tail())
    
def main():
    print_two_owls()   

main()
