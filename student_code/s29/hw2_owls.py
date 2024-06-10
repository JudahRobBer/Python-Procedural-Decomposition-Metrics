
import random

def print_crown(a) -> None:
    print('   .-"-.   ' + (" "*a) + '  .-"-.   ')

def print_eyes(a) -> None:
    print("  / 4 4 \\  " + (" "*a) + " / 4 4 \\  ") #backslash
          
def print_beak(a) -> None:
    print("  \\_ v _/  " + (" "*a) + " \\_ v _/  ") #backslash

def print_chest(a) -> None:
    print("  //   \\\\ " + (" "*a) + "  //   \\\\ ") #backslash

def print_belly(a) -> None:
    print(" ((     )) " + (" "*a) + "((     )) ")

def print_feet(a) -> None:
    print(' =""===""=' + ("="*a) + '==""===""= ') #bench

def print_tail(a) -> None:
    print("    |||   " + (" "*a) + "    |||    ")

def print_two_owls(a) -> None:
    print_crown(a)
    print_eyes(a)
    print_beak(a)
    print_chest(a)
    print_belly(a)
    print_feet(a)
    print_tail(a)

def main():
    a = random.randint(5,20) #Select random number, establish in main so it stays constant throughout program
    print_two_owls(a)

main()
