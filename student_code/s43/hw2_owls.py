
import random

def print_crown(rand_num: int) -> None:
    print("""    .-"-.  """ + (" " * rand_num), """    .-"-.  """)

def print_eyes(rand_num: int) -> None:
    print("   / 4 4 \ " + (" " * rand_num), "   / 4 4 \ ")
          
def print_beak(rand_num: int) -> None:
    print("   \_ v _/ " + (" " * rand_num), "   \_ v _/ ")

def print_chest(rand_num: int) -> None:
    print("   //   \\\ " + (" " * rand_num), "   //   \\\ ")

def print_belly(rand_num: int) -> None:
    print("  ((     )) " + (" " * rand_num), "  ((     )) ")

def print_feet(rand_num: int) -> None:
    print("""  =""===""=""" + ("=" * rand_num) + """====""===""=""")

def print_tail(rand_num: int) -> None:
    print("     ||| "+ (" " * rand_num), "       ||| ")

def print_two_owls() -> None:
    rand_num = random.randint(5, 20)
    print_crown(rand_num)
    print_eyes(rand_num)
    print_beak(rand_num)
    print_chest(rand_num)
    print_feet(rand_num)
    print_tail(rand_num)

def main() -> None:
    print_two_owls()

main()