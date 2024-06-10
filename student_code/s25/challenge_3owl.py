
def print_crown(x,y) -> None:
    print("  .-\"-.  " + " "*x + "  .---.  " + " "*y + "  .-\"-.  ") 

def print_eyes(x,y) -> None:
    print(" / 4 4 \\ " + " "*x + " / _ _ \\ " + " "*y + " /   6_6 ")
          
def print_beak(x,y) -> None:
    print(" \\_ v _/ " + " "*x +" \\_ v _/ " + " "*y + " \\_  (__\\")

def print_chest(x,y) -> None:
    print(" //   \\\\ " + " "*x + " //   \\\\ " + " "*y + " //   \\\\ ")

def print_belly(x,y) -> None:
    print("((     ))" + " "*x + "((     ))" + " "*y + "((     ))")

def print_feet(x,y) -> None:
    print("=\"\"===\"\"=" + "="*x + "=========" + "="*y + "=\"\"===\"\"=")

def print_tail(x,y) -> None:
    print("   |||   " + " "*x + "   |||   " + " "*y + "   |||   ")

def print_three_owls(x,y) -> None:
    print_crown(x,y)
    print_eyes(x,y)
    print_beak(x,y)
    print_chest(x,y)
    print_belly(x,y)
    print_feet(x,y)
    print_tail(x,y)

def main():
    import random
    x = random.randint(5,20)
    y = random.randint(5,20)
    print_three_owls(x,y)

main()