
import random
def print_crown(distance) -> None:
    print(' .-"-.' + (" " * (distance + 2)) + '.-"-.')

def print_eyes(distance) -> None:
    print("/ 4 4 \\" + (" " * (distance)) + "/ 4 4 \\")
          
def print_beak(distance) -> None:
    print("\_ v _/" + (" " * (distance)) + "\_ v _/")

def print_chest(distance) -> None:
    print("//   \\\\" + (" " * distance) + ("//   \\\\"))
        

def print_belly(distance) -> None:
    print("((   ))" + (" " * (distance - 2)) + "  ((   ))")

def print_feet(distance) -> None:
    print('="===""' + ("=" * distance) + '""===""=')

def print_tail(distance) -> None:
    print("  |||   " + (" " * distance) + " |||   ")

def print_two_owls(distance) -> None:
    print_crown(distance)
    print_eyes(distance)
    print_beak(distance)
    print_chest(distance)
    print_belly(distance)
    print_feet(distance)
    print_tail(distance)

def main():
    distance = random.randint(5, 20)
    print_two_owls(distance)
    

main()
