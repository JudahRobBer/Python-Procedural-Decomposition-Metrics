
import random                              #the "import" should always be at the beginning. Not within any function.
def print_crown() -> None:
    print ('  .-"-.  ',end='')             #end='' to stay on the same line

def print_eyes() -> None:
    print (" / 5 5 \\ ", end='')
          
def print_beak() -> None:
    print (" \\_ v _/ ", end='')

def print_chest() -> None:
    print (" //   \\\\ ", end='')

def print_belly() -> None:
    print ("((     ))", end='')

def print_feet() -> None:
    print ('=""===""=', end='')

def print_tail() -> None:
    print ("   |||   ", end='')
    
def print_two_owls() -> None:
    result = random.randint(5,20)
    print_crown()
    print_spaces(result)
    print_crown()
    print()
    print_eyes()
    print_spaces(result)
    print_eyes()
    print()
    print_beak()
    print_spaces(result)
    print_beak()
    print()
    print_chest()
    print_spaces(result)
    print_chest()
    print()
    print_belly()
    print_spaces(result)
    print_belly()
    print()
    print_feet()
    print_branch(result)
    print_feet()
    print()
    print_tail()
    print_spaces(result)
    print_tail()

def print_branch(result:int)-> None:
    print ("=" * result, end='')

def print_spaces(result:int)-> None:          #Both print_branch and print_spaces work the same way; they add the same number of spaces (or, when it comes to the owl's feet, branch pieces) in the gap between the two owls.
    print (" " * result, end='')
    
def main()-> None:
    print_two_owls()

main()
    