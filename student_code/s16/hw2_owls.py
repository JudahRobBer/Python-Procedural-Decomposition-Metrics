
import random
spaces = (random.randint(5,20))

def print_crown() -> None:
    print('  .-"-.' + " "*(spaces+1) + '  .-"-.' + " "*(spaces+1) + '  .-"-.')

def print_eyes() -> None:
    print(" / 4 4 \\" + " "*(spaces) + " / 4 4 \\" + " "*(spaces) + " / _ _ \\" )
          
def print_beak() -> None:
    print(" \\_ v _/" + " "*(spaces) + " \\_ v _/" + " "*(spaces) + " \\_ v _/")

def print_chest() -> None:
    print(" //   \\\\" + " "*(spaces) + " //   \\\\" + " "*(spaces) + " //   \\\\")

def print_belly() -> None:
    print("((     ))" + " "*(spaces-1) + "((     ))" + " "*(spaces-1) + "((     ))")

def print_feet() -> None:
    print('=""===""=' + '='*(spaces-1) + '=""===""=' + '='*(spaces-1) + '=========')

def print_tail() -> None:
    print("   |||" + " "*(spaces+2) + "   |||" + " "*(spaces+2) + "   |||")


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
