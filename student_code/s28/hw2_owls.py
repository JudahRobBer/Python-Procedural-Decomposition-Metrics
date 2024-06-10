
from random import randrange

def print_crown(n: int) -> None:
    print('  .-"-.  ', " "*n, '  .-"-.  ')

def print_eyes(n: int) -> None:
    print (" / 4 4 \\ ", " "*n, " / 4 4 \\ ")
          
def print_beak(n: int) -> None:
    print(" \\_ v _/ ", " "*n, " \\_ v _/ ")

def print_chest(n: int) -> None:
    print(" //   \\\\ ", " "*n, " //   \\\\ ")

def print_belly(n: int) -> None:
    print("((     ))", " "*n, "((     ))")

def print_feet(n: int) -> None:
    print('=""===""=', "="*n, '=""===""=')

def print_tail(n: int) -> None:
    print("   |||   ", " "*n, "   |||   ")

def print_two_owls() -> None:
    random = (randrange(5,20))
    print_crown(random)
    print_eyes(random)
    print_beak(random)
    print_chest(random)
    print_belly(random)
    print_feet(random)
    print_tail(random)
    
def nocrest(n: int) -> None:
    print("  .---.  ", " "*n, "  .---.  ")
    
def sleeping_eyes(n: int) -> None:
    print(" / _ _ \\ ", " "*n, " / _ _ \\ ")
    
def tucked_feet(n: int) -> None:
    print("=========", "="*n, "=========")
    
def sleeping():
    random = (randrange(5,20))
    nocrest(random)
    sleeping_eyes(random)
    print_beak(random)
    print_chest(random)
    print_belly(random)
    tucked_feet(random)
    print_tail(random)
    
def sideways_eyes(n: int) -> None:
    print(" /   6_6 ", " "*n, " /   6_6 ")
    
def sideways_beak(n: int) -> None:
    print(" \\_  (__\\", " "*n, " \\_  (__\\")
    
    
def sideways():
    random = (randrange(5,20))
    print_crown(random)
    sideways_eyes(random)
    sideways_beak(random)
    print_chest(random)
    print_belly(random)
    print_feet(random)
    print_tail(random)

def main():
    print_two_owls()
    sleeping()
    sideways()

main()
