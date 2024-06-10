

# Generating Random Number
import random
n=random.randint(5,21)

# Define functions for all features
def print_crown() -> None:
    crown='  .-"-.  '
    sleep_crown='  .---.  '
    space=' ' * n
    print(crown+space+sleep_crown+space+crown)

def print_eyes() -> None:
    eyes=' / 4 4 \\ '
    sleep_eyes=' / _ _ \\ '
    side_eyes=' /   6_6 '
    space=' ' * n
    print(eyes+space+sleep_eyes+space+side_eyes)
          
def print_beak() -> None:
    beak=' \\_ v _/ '
    side_beak=' \\_  (__\\'
    space=' ' * n
    print(beak+space+beak+space+side_beak)

def print_chest() -> None:
    chest=' //   \\\\ '
    space=' ' * n
    print(chest+space+chest+space+chest)

def print_belly() -> None:
    belly='((     ))'
    space=' ' * n
    print(belly+space+belly+space+belly)

def print_feet() -> None:
    feet='''=""===""='''
    sleep_feet='========='
    branch='='* n
    print(feet+branch+sleep_feet+branch+feet)

def print_tail() -> None:
    tail='   |||   '
    space=' ' * n
    print(tail+space+tail+space+tail)

# Putting all features together
def print_three_owls() -> None:
    print_crown()
    print_eyes()
    print_beak()
    print_chest()
    print_belly()
    print_feet()
    print_tail()

# Define main function
def main():
    print_three_owls()

# Call main function
main()