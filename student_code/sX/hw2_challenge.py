

import random
spaces = random.randrange(5,20,1)

def print_crown() -> str:
    crown3=(('  .-"-.  ') + (spaces * ' ') + ('  .-"-.  ') + (spaces * ' ') +  ('  .---.  '))
    return crown3

def print_eyes() -> str:
    eyes3 =((" /   7_7 ") + (spaces * ' ') + (" / * * \ ") + (spaces * ' ') + (" /-0-0-\ "))
    return eyes3
        
def print_beak() -> str:
    beak3 = ((" \_  (__\ ") + ((spaces-1) * ' ') + (" \_ v _/ ") + (spaces * ' ') + (" \_ v _/ "))
    return beak3

def print_chest() -> str:
    chest3= ((" //" + (" " * 3) + "\\\ ") + (spaces * ' ') + (" //"+ (" " * 3) + "\\\ ") + (spaces * ' ') + (" //"+ (" " * 3) + "\\\ "))
    return chest3

def print_belly() -> str:
    belly3 = ("((" + (" " * 5) + "))" + (spaces * ' ') + "((" + (" " * 5) + "))" + (spaces * ' ') + "((" + (" " * 5) + "))")
    return belly3

def print_feet() -> str:
    feet3 = (('=""===""=') + (spaces * '=') + '=""===""='  + (spaces * '=') + '=========')
    return feet3

def print_tail() -> str:
    tail3 = (((" " * 3) + "|||" + (" " *3)) + (spaces * " ") +((" " * 3) + "|||" + (" " * 3)) + (spaces * " ") +((" " * 3) + "|||" + (" " * 3)))
    return tail3
        
def print_two_owls() -> None:
    print(print_crown())
    print(print_eyes())
    print(print_beak())
    print(print_chest())
    print(print_belly())
    print(print_feet())
    print(print_tail())

def main() -> None:
    print_two_owls()

main()

