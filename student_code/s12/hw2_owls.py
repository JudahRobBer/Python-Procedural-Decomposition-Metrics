
# Generating Random Number
import random
n=random.randint(5,21)

# Define functions for all features
def print_crown() -> None:
    crown='  .-"-.  '
    space=' ' * n
    print(crown+space+crown)

def print_eyes() -> None:
    eyes=' / 4 4 \\ '
    space=' ' * n
    print(eyes+space+eyes)
          
def print_beak() -> None:
    beak=' \\_ v _/ '
    space=' ' * n
    print(beak+space+beak)

def print_chest() -> None:
    chest=' //   \\\\ '
    space=' ' * n
    print(chest+space+chest)

def print_belly() -> None:
    belly='((     ))'
    space=' ' * n
    print(belly+space+belly)

def print_feet() -> None:
    feet='''=""===""='''
    branch='='* n
    print(feet+branch+feet)

def print_tail() -> None:
    tail='   |||   '
    space=' ' * n
    print(tail+space+tail)

# Putting all features together
def print_two_owls() -> None:
    print_crown()
    print_eyes()
    print_beak()
    print_chest()
    print_belly()
    print_feet()
    print_tail()

# Define main function
def main():
    print_two_owls()

# Call main function
main()
