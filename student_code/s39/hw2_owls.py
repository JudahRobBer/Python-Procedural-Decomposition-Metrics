

def print_crown() -> str:
    print_crown='   .-"-.   '
    return print_crown 

def print_eyes() -> str:
    print_eyes='  / 4 4 \\  '
    return print_eyes

def print_beak() -> str:
    print_beak='  \_ v _/  '
    return print_beak
  
def print_chest() -> str:
    print_chest='  //   \\\\  '
    return print_chest

def print_belly() -> str:
    print_belly=" ((     )) "
    return print_belly

def print_feet() -> str:
    print_feet='==""===""=='
    return print_feet

def print_tail() -> str:
    print_tail='    |||    '
    return print_tail

def print_two_owls() -> None:
    import random
    rand=random.randrange(5,21)
#combine all parts together to be main()
    print(print_crown()+(' '*rand)+print_crown())
    print(print_eyes()+(' '*rand)+print_eyes())
    print(print_beak()+(' '*rand)+print_beak())
    print(print_chest()+(' '*rand)+print_chest())
    print(print_belly()+(' '*rand)+print_belly())
    print(print_feet()+('='*rand)+print_feet())
    print(print_tail()+(' '*rand)+print_tail())

def main():
    print_two_owls()

main()