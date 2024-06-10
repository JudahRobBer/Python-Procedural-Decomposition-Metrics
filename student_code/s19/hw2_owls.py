

def print_crown(space:int) -> None:
    print ('  .-"-.  ' + space + '  .-"-.  ')

def print_eyes(space:int) -> None:
    print (' / 4 4 \\ ' + space + ' / 4 4 \\ ')
          
def print_beak(space:int) -> None:
    print (' \\_ v _/ ' + space + ' \\_ v _/ ')

def print_chest(space:int) -> None:
    print (' //   \\\\ ' + space + ' //   \\\\ ')

def print_belly(space:int) -> None:
    print ('((     ))' + space + '((     ))')

def print_feet(space:int) -> None:
    print ('=""===""=' + space + '=""===""=')

def print_tail(space:int) -> None:
    print ('   |||   ' + space + '   |||   ')

def print_two_owls(spacing) -> None:
    print_crown(spacing)
    print_eyes(spacing)
    print_beak(spacing)
    print_chest(spacing)
    print_belly(spacing)
    print_feet(spacing)
    print_tail(spacing)

def main():
    import random
    number_space = random.randint(5, 20)
    spacing = " " * number_space
    
    print_two_owls(spacing)

main()
