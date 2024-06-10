

# Importing Random Package
import random


# Define functions for all features
def print_crown(n:int) -> None:
    crown='  .-"-.  '
    space=' ' * n
    print(crown+space+crown)

def print_eyes(n:int) -> None:
    eyes=' / 4 4 \\ '
    space=' ' * n
    print(eyes+space+eyes)
          
def print_beak(n:int) -> None:
    beak=' \\_ v _/ '
    space=' ' * n
    print(beak+space+beak)

def print_chest(n:int) -> None:
    chest=' //   \\\\ '
    space=' ' * n
    print(chest+space+chest)

def print_belly(n:int) -> None:
    belly='((     ))'
    space=' ' * n
    print(belly+space+belly)

def print_feet(n:int) -> None:
    feet='''=""===""='''
    branch='='* n
    print(feet+branch+feet)

def print_tail(n:int) -> None:
    tail='   |||   '
    space=' ' * n
    print(tail+space+tail)

# Putting all features together
def print_two_owls(n:int) -> None:
    print_crown(n)
    print_eyes(n)
    print_beak(n)
    print_chest(n)
    print_belly(n)
    print_feet(n)
    print_tail(n)

# Define main function
def main():
    n=random.randint(5,21)
    print_two_owls(n)

# Call main function
main()
