#the print functions take the first owl and then add two slightly different owls
#they take two different random int istead of one to create space between them.

def print_crown(space1:int, space2:int) -> None:
    print(("  .-\"-.  ") + (space1 * " ") + ("  .---.  ") + (space2 * " ") + ("  .-\"-.  "))

def print_eyes(space1:int, space2: int) -> None:
    print((" / 4 4 \\ ") + (space1 * " ") + (" / _ _ \\ ") + (space2 * " ") + (" /   6_6 "))
          
def print_beak(space1:int, space2: int) -> None:
    print((" \\_ v _/ ") + (space1 * " ") + (" \\_ v _/ ") + (space2 * " ") + (" \\_  (__\\"))

def print_chest(space1:int, space2: int) -> None:
    print((" //   \\\\ ") + (space1 * " ") + (" //   \\\\ ") + (space2 * " ") + (" //   \\\\ "))

def print_belly(space1:int, space2: int) -> None:
    print(("((     ))") + (space1 * " ") + ("((     ))") + (space2 * " ") + ("((     ))"))

def print_feet(space1:int, space2: int) -> None:
    print(("=\"\"===\"\"=") + (space1 * "=") + ("=========") + (space2 * "=") + ("=\"\"===\"\"="))

def print_tail(space1:int, space2: int) -> None:
    print(("   |||   ") + (space1 * " ") + ("   |||   ") + (space2 * " ") + ("   |||   ")) 

#this function generates two random int and passes them both to the print functions. It then calls the print functions in the right order to draw three owls.
def print_three_owls() -> None: 
    import random
    branch1 = random.randint(5, 20)
    branch2 = random.randint(5, 20)
    print_crown(branch1, branch2)
    print_eyes(branch1, branch2)
    print_beak(branch1, branch2)
    print_chest(branch1, branch2)
    print_belly(branch1, branch2)
    print_feet(branch1, branch2) 
    print_tail(branch1, branch2)


def main():
    print_three_owls()


main()