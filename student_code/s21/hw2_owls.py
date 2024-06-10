

#random is imported, and randint() to generate a pseudorandom number which determines the spacing of the owls.
import random

#randint(5, 21) as the spaces are from 5 to 20, inclusive.
number = random.randint(5,21)

#the following functions print out each part of the owl, and are used by print_two_owls()
def print_crown() -> None:
    print('  .-"-.'+ " "*number+ '    .-"-.' )

def print_eyes() -> None:
    print(" / 4 4 \\" + " "*number+ '  / 4 4 \\')
          
def print_beak() -> None:
    print(" \_ v _/" + " "*number+ '  \_ v _/')

def print_chest() -> None:
    print(" //   \\\\" + " "*number+   '  //   \\\\')
    
def print_belly() -> None:
    print("((     ))" + " "*number+"((     ))")

def print_feet() -> None:
    print('=""===""=' +"="*number+ '=""===""=')

def print_tail() -> None:
    print("   |||    " + " "*number+'  ||| ')   
    

#this function is called by main, and prints the two owls.
#It bring together all the parts of the owls, to be used in main.
def print_two_owls() -> None:
    print_crown(), 
    print_eyes() 
    print_beak() 
    print_chest() 
    print_belly() 
    print_feet() 
    print_tail()
    
#this is the first function used, and goes back to print_two_owls.
def main():
    print_two_owls()
    
main()
