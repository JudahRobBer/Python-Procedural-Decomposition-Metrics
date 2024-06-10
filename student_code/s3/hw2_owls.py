
import random
x = random.randint(5,20)

def print_crown(x:int) -> None:
    print('''  .-"-.  ''' + x * " " + '''   .-"-.''' )

def print_eyes(x:int) -> None:
    print(''' / 4 4 \ ''' + x * " " + '''  / 4 4 \ ''')
          
def print_beak(x:int) -> None:
    print(''' \_ v _/ ''' + x * " " + '''  \_ v _/ ''')

def print_chest(x:int) -> None:
    print(''' //   \\\ ''' + x * " " + '''  //   \\\ ''' )

def print_belly(x:int) -> None:
    print('''((     )) ''' + x * " " +'''((     ))''')

def print_feet(x:int) -> None:
    print('''=""===""=''' + x * "=" +'''==""===""=''' )

def print_tail(x:int) -> None:
    print('''   |||  ''' + x * " " + '''     ||| ''')

def print_two_owls(x:int) -> None:
    print_crown(x)
    print_eyes(x)
    print_beak(x)
    print_chest(x)
    print_belly(x)
    print_feet(x)
    print_tail(x)

def main():
    print_two_owls(x)

main()

print(" ")

def print_crown(x:int) -> None:
    print('''  .-"-.  ''' + x * " " + '''   .-"-.''' + x * " " + '''    .---.''' )

def print_eyes(x:int) -> None:
    print(''' / 4 4 \ ''' + x * " " + '''  / 4 4 \ ''' + x * " " + ''' / _ _ \ ''')
          
def print_beak(x:int) -> None:
    print(''' \_ v _/ ''' + x * " " + '''  \_ v _/ ''' + x * " " + ''' \_ v _/''')

def print_chest(x:int) -> None:
    print(''' //   \\\ ''' + x * " " + '''  //   \\\ ''' + x * " " + ''' //   \\\ ''' )

def print_belly(x:int) -> None:
    print('''((     )) ''' + x * " " +'''((     ))''' + x * " " +'''((     )) ''')

def print_feet(x:int) -> None:
    print('''=""===""=''' + x * "=" +'''==""===""=''' + x * "=" + '''=========''')

def print_tail(x:int) -> None:
    print('''   |||  ''' + x * " " + '''     ||| ''' + x * " " + '''     |||''')

def print_three_owls(x:int) -> None:
    print_crown(x)
    print_eyes(x)
    print_beak(x)
    print_chest(x)
    print_belly(x)
    print_feet(x)
    print_tail(x)

def main():
    print_three_owls(x)

main()