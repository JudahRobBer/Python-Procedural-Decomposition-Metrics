

#function to print the crown of the owl
def print_crown(spaces: str) -> None:
    print("    _||_  " + spaces + "    _||_  ")
    print("   .   . " + spaces + "    .   . ")

#function to print the eyes of the owl
def print_eyes(spaces: str) -> None:
    print("  / 4 4 \\" + spaces + "   / 4 4 \\")

#function to print the beak of the owl
def print_beak(spaces: str) -> None:
    print ("  \\_ v _/" + spaces + "   \\_ v _/")
    
#function to print the chest of the owl    
def print_chest(spaces: str) -> None:
    print ("  //   \\\\" + spaces + "   //   \\\\")

#function to print the belly of the owl
def print_belly(spaces: str) -> None:
    print (" ((     ))" + spaces + " ((     ))")

#function to print the feet of the owl
def print_feet(branch_size: str) -> None:
    print (' =""===""=' + branch_size + '==""===""= ')

#function to print the tail of the owl
def print_tail(spaces: str) -> None:
    print ("    |||    " + spaces + "    |||    ")

#function to print two owls with spaces randomly generated inbetween
def print_two_owls() -> None:
    import random
    random_number = random.randint(5,20)
    spaces = random_number * " "
    branch_size = random_number * "="
    print_crown(spaces)
    print_eyes(spaces)
    print_beak(spaces)
    print_chest(spaces)
    print_belly(spaces)
    print_feet(branch_size)
    print_tail(spaces)

#function to call the function to print owls 
def main():
    print_two_owls()

#calling the main function
main()
