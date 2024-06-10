
import random

#define different part of the owls
def print_crown(space) -> None:
    print('   .-"-.   '+space*" "+' .-"-.' )
    
def print_eyes(space) -> None:
    print("  / 4 4 \\  "+space*" "+"/ 4 4 \\  ")
         
def print_beak(space) -> None:
    print("  \\_ v _/  "+space*" "+"\\_ v _/  ")

def print_chest(space) -> None:
    print("  //   \\\\  "+space*" "+"//   \\\\")

def print_belly(space) -> None:
    print(" ((     ))"+space*" "+"((     )) ")

def print_feet(space) -> None:
    print(' =""===""='+space*"="+'=""===""=')

def print_tail(space) -> None:
    print("    |||  "+space*" "+"    |||")

def print_two_owls() -> None:
    n=random.randint(5,20)
    print_crown(n)
    print_eyes(n)
    print_beak(n)
    print_chest(n)
    print_belly(n)
    print_feet(n)
    print_tail(n)


def main():
    print_two_owls()
#print two owls
main()


