

# function that prints the crown of the owls
def print_crown() -> str:
    crown = "  .-\"-.  "
    return crown

# function that prints the eyes of the  owls
def print_eyes() -> str:
    eyes = " / 4 4 \ "
    return eyes

# function that prints the beak of the  owls
def print_beak() -> str:
    beak = " \_ v _/ "
    return beak

# function that prints the chest of the owls
def print_chest() -> str:
    chest = " //   \\\ "
    return chest

# function that prints the belly of the owls
def print_belly() -> str:
    belly = "((     ))"
    return belly

# function that prints the feet of the owls
def print_feet() -> str:
    feet = "=\"\"===\"\"="
    return feet

# function that prints the tail of the owls
def print_tail() -> str:
    tail = "   |||   "
    return tail

# function that prints two complete owls
# iterate through each function in owls_part1 to print parts (except for feet and tail) of two owls that are separated by a randomly chosen space
# then print the feet and tail of two owls with a randomly chosen length of branch between them
def print_two_owls(e_space: str, b_length: str) -> None:
    owls_part1 = [print_crown(), print_eyes(), print_beak(), print_chest(), print_belly()]
    for parts in owls_part1:
        print(parts + e_space + parts)
    print(print_feet() + b_length + print_feet())
    print(print_tail() + e_space + print_tail())

# function that random selects the branch length and calls the print_two_owls function to print a pair of owls
def main():
    import random
    space = random.randint(5, 21)
    branch_length = space * "="
    empty_space = space * " "
    print_two_owls(empty_space, branch_length)

# execute the main function when the program is run
main()