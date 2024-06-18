

import random

def print_crown(spaces) -> str:
    crown=(('  .-"-.  ') + (spaces * ' ') + ('  .-"-.  '))
    return crown

def print_eyes(spaces) -> str:
    eyes = ((" / 4 4 \ ") + (spaces * ' ') + (" / 4 4 \ "))
    return eyes
        
def print_beak(spaces) -> str:
    beak = ((" \_ v _/ ") + (spaces * ' ') + (" \_ v _/ "))
    return beak

def print_chest(spaces) -> str:
    chest= ((" //" + (" " * 3) + "\\\ ") + (spaces * ' ') + (" //"+ (" " * 3) + "\\\ "))
    return chest

def print_belly(spaces) -> str:
    belly = ("((" + (" " * 5) + "))" + (spaces * ' ') + "((" + (" " * 5) + "))")
    return belly

def print_feet(spaces) -> str:
    feet = (('=""===""=') + (spaces * '=') + '=""===""=')
    return feet

def print_tail(spaces) -> str:
    tail = (((" " * 3) + "|||" + (" " *3)) + (spaces * " ") +((" " * 3) + "|||" + (" " * 3)))
    return tail
# instead of printing in the function, it returns the string which is printed from a different function 
        
def print_two_owls() -> None:
    spaces = random.randrange(5,20,1)
    # set random value for spaces in this function to avoid a global variable
    print(print_crown(spaces))
    print(print_eyes(spaces))
    print(print_beak(spaces))
    print(print_chest(spaces))
    print(print_belly(spaces))
    print(print_feet(spaces))
    print(print_tail(spaces))

def main() -> None:
    print_two_owls()

main()
