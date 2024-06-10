
def print_crown(x) -> None:
    print("  .-\"-.  " + " "*x + "  .-\"-.  ") 

def print_eyes(x) -> None:
    print(" / 4 4 \\ " + " "*x + " / 4 4 \\ ")
          
def print_beak(x) -> None:
    print(" \\_ v _/ " + " "*x +" \\_ v _/ ")

def print_chest(x) -> None:
    print(" //   \\\\ " + " "*x + " //   \\\\ ")

def print_belly(x) -> None:
    print("((     ))" + " "*x + "((     ))")

def print_feet(x) -> None:
    print("=\"\"===\"\"=" + "="*x + "=\"\"===\"\"=")

def print_tail(x) -> None:
    print("   |||   " + " "*x + "   |||   ")

def print_two_owls(x) -> None:
    print_crown(x)
    print_eyes(x)
    print_beak(x)
    print_chest(x)
    print_belly(x)
    print_feet(x)
    print_tail(x)

def main():
    import random
    x = random.randint(5,20)
    print_two_owls(x)

main()
