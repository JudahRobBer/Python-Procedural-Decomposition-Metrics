

import random

def print_crown(spaces: int) -> None:
    print('  .-"-.  '," " * spaces,'  .---.  '," " * spaces,'  .-"-.')  # crowns

def print_eyes(spaces: int) -> None:
    print(" / 4 4 \\ "," " * spaces," / _ _ \\ ", " " * spaces," /   6_6") # eyes
          
def print_beak(spaces: int) -> None:
    print(" \\_ v _/ "," " * spaces," \\_ v _/ ", " " * spaces," \\_  (__\\")  # beaks

def print_chest(spaces: int) -> None:
    print(" //   \\\\ "," " * spaces," //   \\\\ ", " " * spaces, " //   \\\\") # chests

def print_belly(spaces: int) -> None:
    print("((     ))"," " * spaces,"((     ))", " " * spaces,"((     ))") # bellies

def print_feet(spaces: int) -> None:
    print('=""===""==', "=" * spaces,'============', "=" * spaces,'=""===""==', sep='') # feet
    
def print_tail(spaces: int) -> None:
    print("   |||   ", " " * spaces,"   |||   ", " " * spaces,"   |||  ") # tails

def print_two_owls() -> None:   # function calls
    spaces = random.randint(5,20) # define variable
    print_crown(spaces)
    print_eyes(spaces)
    print_beak(spaces)
    print_chest(spaces)
    print_belly(spaces)
    print_feet(spaces)
    print_tail(spaces)
    
def main():
    print_two_owls()

main()
