
import random
x = random.randint (1, 16)

def print_crown() -> None:
    print ('  .-"-.    ' + " " * x + '    .-"-.')

def print_eyes() -> None:
    print (" / 4 4 \   " + " " * x + "   / 4 4 \\")
          
def print_beak() -> None:
    print (" \_ v _/   " + " " * x + "   \_ v _/")

def print_chest() -> None:
    print (" //   \\\   " + " " * x + "   //   \\\\")

def print_belly() -> None:
    print ("((     ))  " + " " * x + "  ((     ))")

def print_feet() -> None:
    print ('=""===""===' + "=" * x + '===""===""=')

def print_tail() -> None:
    print ("   |||     " + " " * x + "     |||")

def print_two_owls() -> None:
    print_crown()
    print_eyes()
    print_beak()
    print_chest()
    print_belly()
    print_feet()
    print_tail()

def main():
    print_two_owls()

main()
