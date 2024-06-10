
#functions need to return strings
#need to import random for random number within 5 and 20

def print_crown() -> str:
    return ('  .-"-.  ')
    
def print_eyes() -> str:
    return (" / 4 4 \ ")
          
def print_beak() -> str:
    return (" \_ v _/ ")

def print_chest() -> str:
    return (" //   \\\ ")

def print_belly() -> str:
    return ("((     ))")

def print_feet() -> str:
    return('=""===""=')

def print_tail() -> str:
    return("   |||   ")

def print_two_owls() -> str:
    import random
    x = random.randint(5,21)
    print(print_crown()+" " * x+print_crown())
    print(print_eyes()+" " * x+print_eyes())
    print(print_beak()+" " * x+print_beak())
    print(print_chest()+" " * x+print_chest())
    print(print_belly()+" " * x+print_belly())
    print(print_feet()+"=" * x+print_feet())
    print(print_tail()+" " * x+print_tail())

def main():
    print_two_owls()

main()
