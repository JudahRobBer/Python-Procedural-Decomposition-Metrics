
import random
space = random.randint(5,21)

def print_crown() -> None:
    print('  .-"-.' + space*" " + '.-"-.')

def print_eyes() -> None:
    print(" / 4 4 \\" + (space-2)*" " + "/ 4 4 \\")
          
def print_beak() -> None:
    print(" \_ v _/" + (space-2)*" " + "\_ v _/")

def print_chest() -> None:
    print(" //   \\\\" + (space-2)*" " + "//   \\\\")

def print_belly() -> None:
    print("((     ))" + (space-4)*" " + "((     ))")

def print_feet() -> None:
    print('=""===""=' + (space-4)*"=" + '=""===""=')

def print_tail() -> None:
    print("   |||" + (space+2)*" " + "|||")

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
