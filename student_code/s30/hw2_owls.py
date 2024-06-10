

import random                  

def print_crown(spaces: int) -> None:   # crowns
    print('  .-"-.  '," " * spaces,'  .-"-.')

def print_eyes(spaces: int) -> None:  # eyes
    print(" / 4 4 \\ "," " * spaces," / 4 4 \\")
          
def print_beak(spaces: int) -> None: # beaks
    print(" \\_ v _/ "," " * spaces," \\_ v _/")

def print_chest(spaces: int) -> None:  # chests
    print(" //   \\\\ "," " * spaces," //   \\\\")

def print_belly(spaces: int) -> None: # bellies
    print("((     ))"," " * spaces,"((     ))")

def print_feet(spaces: int) -> None: # feet
    print('=""===""==', "=" * spaces,'==""===""=', sep='')
    
def print_tail(spaces: int) -> None:  # tails
    print("   |||   ", " " * spaces,"   |||   ")

def print_two_owls() -> None: # function calls
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
