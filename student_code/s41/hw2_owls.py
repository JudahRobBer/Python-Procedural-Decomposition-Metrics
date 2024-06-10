

# the function prints the crown of the owl and return
def print_crown() -> str:
    crown = ('  .-"-.  ')
    return crown

# the function prints the owl without the crown and return
def print_nocrown() -> str:
    nocrown = ('  .---.  ')
    return nocrown

# the function prints the eyes of the owl and return
def print_eyes() -> str:
    eyes = (' / 4 4 \ ')
    return eyes

# the function prints the owl without eyes and return
def print_noeyes() -> str:
    noeyes = (' / _ _ \ ')
    return noeyes

# the function prints the 6 as owl's eyes and return
def print_eyes6() -> str:
    eyes6 =  (" /   6_6 ")
    return eyes6

#the funciton prints the beak of the owl and return
def print_beak() -> str:
    beak = (' \_ v _/ ')
    return beak

# the function prints a special beak for the owl and return
def print_beak2() -> str:
    beak2 = (" \_  (__\ " )
    return beak2

# the function prints the chest of the owl and return
def print_chest() -> str:
    chest = (' //   \\\ ')
    return chest

# the function prints the belly of the owl and return
def print_belly() -> str:
    belly = ('((     ))')
    return belly

# the function prints the feet of the owl and return
def print_feet() -> str:
    feet = ('=""===""=')
    return feet

# the function prints the owl without feet and return
def print_nofeet() -> str:
    feet = ('=========')
    return feet

# the function prints the tail of the owl and return
def print_tail() -> str:
    tail = ('   |||   ')
    return tail

# the funciton prints two idential owls with random spacing as the computer decides
def print_two_owls(space1:str,equal: str) -> None:
    print(print_crown() + space1 + print_crown())
    print(print_eyes() + space1 + print_eyes())
    print(print_beak() + space1 + print_beak())
    print(print_chest() + space1 + print_chest())
    print(print_belly() + space1 + print_belly())
    print(print_feet() + equal + print_feet())
    print(print_tail() + space1 + print_tail())
    print()
    print()

#challenge: the function prints three different owls with different appearances
def print_three_different_owls(space1: str, equal: str) -> None:
    print(print_crown() + space1 + print_nocrown() + space1 + print_crown())
    print(print_eyes() + space1 + print_noeyes() + space1 + print_eyes6())
    print(print_beak() + space1 + print_beak() + space1 + print_beak2())
    print(print_chest() + space1 + print_chest() + space1 + print_chest())
    print(print_belly() + space1 + print_belly() + space1 + print_belly())
    print(print_feet() + equal + print_nofeet() + equal + print_feet())
    print(print_tail() + space1 + print_tail() + space1 + print_tail())

#the function imports random function to let the computer decide the random
#lengths that will lay between two owls
def main():
    import random
    space = random.randint(5,21)
    equal = "=" * space
    space1 = " " * space
    print_two_owls(space1, equal)
    print_three_different_owls(space1, equal)
    
# funciton call
main()