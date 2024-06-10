
import random

def print_crown(spaces: str) -> None:
    print(f"  .-\"-.  {spaces}  .-\"-.  ")

def print_eyes(spaces: str) -> None:
    print(f" / 4 4 \ {spaces} / 4 4 \ ") 
          
def print_beak(spaces: str) -> None:
    print(f" \_ v _/ {spaces} \_ v _/ ")

def print_chest(spaces: str) -> None:
    print(f" //   \\\\ {spaces} //   \\\\ ")

def print_belly(spaces: str) -> None:
    print(f"((     )){spaces}((     ))")

def print_feet(branchLen: str) -> None:
    print(f"=\"\"===\"\"={branchLen}=\"\"===\"\"=")

def print_tail(spaces) -> None:
    print(f"   |||   {spaces}   |||   ")

def print_two_owls(spaces: str, bran: str) -> None:
    print_crown(spaces)
    print_eyes(spaces)
    print_beak(spaces)
    print_chest(spaces)
    print_belly(spaces)
    print_feet(bran)
    print_tail(spaces)
    
def main():
    rand = random.randrange(5, 20)
    numSpaces = rand*" "
    branch = rand*"="
    print_two_owls(numSpaces, branch)

main()

