import random

def print_crown() -> None:
    print('  .-"-.  ', end="")

def print_eyes() -> None:
    print(" / 4 4 \\ ", end="")
          
def print_beak() -> None:
    print(" \\_ v _/ ", end="")

def print_chest() -> None:
    print(" //   \\\\ ", end="")

def print_belly() -> None:
    print("((     ))", end="")

def print_feet() -> None:
    print('=""===""=', end="")

def print_tail() -> None:
    print('   |||   ', end="")

def print_two_owls() -> None:
    distance = random.randint(5, 20)
    print_crown()
    print(' '*distance, end="")
    print_crown()
    print()
    print_eyes()
    print(' '*distance, end="")
    print_eyes()
    print()
    print_beak()
    print(' '*distance, end="")
    print_beak()
    print()
    print_chest()
    print(' '*distance, end="")
    print_chest()
    print()
    print_belly()
    print(' '*distance, end="")
    print_belly()
    print()
    print_feet()
    print('='*distance, end="")
    print_feet()
    print()
    print_tail()
    print(' '*distance, end="")
    print_tail()
    print()
