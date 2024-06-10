

import random

#print functions to be called in the print_two_owls functions
#individual parts of the owl drawing
#concated the print_feet function to prevent space between strings
def print_crown(x: int) -> None:
    print('  .-"-.  ',' '*(x),'  .-"-.')

def print_eyes(x: int) -> None:
    print(' / 4 4 \\ ',' '*(x),' / 4 4 \\') 
          
def print_beak(x: int) -> None:
    print(' \\_ v _/ ',' '*(x),' \\_ v _/')

def print_chest(x: int) -> None:
    print(' //   \\\\ ',' '*(x),' //   \\\\')  

def print_belly(x: int) -> None:
    print('((     ))',' '*x,'((     ))')

def print_feet(x: int) -> None:
    print('=""===""=='+'='*(x)+'==""===""=')

def print_tail(x: int) -> None:
    print('   |||  ',' '*(x),'    |||')

#called random.randint to assign x to random intenger between 5 and 20 
#function to put all of the individual parts of the owl together

def print_two_owls() -> None:
    x = random.randint(5,20)
    print_crown(x)
    print_eyes(x)
    print_beak(x)
    print_chest(x)
    print_belly(x)
    print_feet(x)
    print_tail(x)

#final function to act as the entry point into the program
def main()-> None:
    print_two_owls()
   
main()
