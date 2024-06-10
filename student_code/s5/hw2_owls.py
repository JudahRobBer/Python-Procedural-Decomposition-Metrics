

def print_crown(space) -> None:
    print('  .-"-.  ',end='')
    for i in range(space):
        print(' ',end='')
    print('  .-"-.  ')

def print_eyes(space) -> None:
    print(' / 4 4 \\ ',end='')
    for i in range(space):
        print(' ',end='')
    print(' / 4 4 \\ ')
          
def print_beak(space) -> None:
    print(' \\_ v _/ ',end='')
    for i in range(space):
        print(' ',end='')
    print(' \\_ v _/ ')

def print_chest(space) -> None:
    print(' //   \\\\ ',end='')
    for i in range(space):
        print(' ',end='')
    print(' //   \\\\ ')

def print_belly(space) -> None:
    print('((     ))',end='')
    for i in range(space):
        print(' ',end='')
    print('((     ))')

def print_feet(space) -> None:
    print('=""===""=',end='')
    for i in range(space):
        print('=',end='')
    print('=""===""=')

def print_tail(space) -> None:
    print('   |||   ',end='')
    for i in range(space):
        print(' ',end='')
    print('   |||   ')

def print_two_owls(space) -> None:
    print_crown(space)
    print_eyes(space)
    print_beak(space)
    print_chest(space)
    print_belly(space)
    print_feet(space)
    print_tail(space)

def main():
    import random
    space=random.randint(5, 20)
    print_two_owls(space)

main()
