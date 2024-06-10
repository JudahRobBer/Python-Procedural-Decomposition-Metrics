
import random
random_num= random.randint(5,21)

def print_crown() -> None:
    crown= (str("""  .-"-.  """ + (" "*random_num)))*2
    print(crown)

def print_eyes() -> None:
    eyes= str(" / 4 4 \\ " + " "*random_num)*2
    print(eyes)
          
def print_beak() -> None:
    beak= str(" \\_ v _/ " + " "*random_num)*2
    print(beak)

def print_chest() -> None:
    chest= str(" //   \\\\ " + " "*random_num)*2
    print(chest)

def print_belly() -> None:
    belly= str("((     ))" + " "*random_num)*2
    print(belly)

def print_feet() -> None:
    feet= str("""=""===""=""" + "="*random_num)*2
    print(feet)

def print_tail() -> None:
    tail= str("   |||   " + " "*random_num)*2
    print(tail)

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
