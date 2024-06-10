
import random

def print_crown() -> None:
    print("  .-\"-.         .-\"-.")

def print_eyes() -> None:
    print(" / 4 4 \\       / 4 4 \\")
          
def print_beak() -> None:
    print(" \\_ v _/       \\_ v _/")

def print_chest() -> None:
    print(" //   \\\\       //   \\\\")

def print_belly() -> None:
    print("((     ))     ((     ))")

def print_feet() -> None:
    print("=\"\"===\"\"=======\"\"===\"\"=")

def print_tail() -> None:
    print("   |||           |||")

def print_two_owls() -> None:
    distance = random.randint(5, 20)
    print(" " * distance, end='')
    print_crown()
    print(" " * distance, end='')
    print_eyes()
    print(" " * distance, end='')
    print_beak()
    print(" " * distance, end='')
    print_chest()
    print(" " * distance, end='')
    print_belly()
    print(" " * distance, end='')
    print_feet()
    print(" " * distance, end='')
    print_tail()
    print()
    print()
    print(" " * distance, end='')
    print_crown()
    print(" " * distance, end='')
    print_eyes()
    print(" " * distance, end='')
    print_beak()
    print(" " * distance, end='')
    print_chest()
    print(" " * distance, end='')
    print_belly()
    print(" " * distance, end='')
    print_feet()
    print(" " * distance, end='')
    print_tail()

def main():
    print_two_owls()

main()
