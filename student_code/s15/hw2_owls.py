

def print_crown(s:int) -> None:
    print ('  .-"-.  ' + s + '  .-"-.  ')

def print_eyes(s:int) -> None:
    print (' / 4 4 \\ ' + s + ' / 4 4 \\ ')
          
def print_beak(s:int) -> None:
    print (' \\_ v _/ ' + s + ' \\_ v _/ ')

def print_chest(s:int) -> None:
    print (' //   \\\\ ' + s + ' //   \\\\ ')

def print_belly(s:int) -> None:
    print ('((     ))' + s + '((     ))')

def print_feet(s:int) -> None:
    print ('=""===""=' + s + '=""===""=')

def print_tail(s:int) -> None:
    print ('   |||   ' + s + '   |||   ')

def print_two_owls(s:int) -> None:
    print_crown(s)
    print_eyes(s)
    print_beak(s)
    print_chest(s)
    print_belly(s)
    print_feet(s)
    print_tail(s)

def main():
    import random
    n = random.randint(5, 20)
    s = " " * n
    print_two_owls(s)

main()
    

    