

import random
#creates rand variable between 5 and 20 inclusive
x = random.randint(5,20)

#print functions
#uses rand variable to change spacing between owls
def print_crown(spacing:int) -> None:
    print('''   .-"-.  ''' + spacing * " " +  '''  .-"-.  ''')

def print_eyes(spacing:int) -> None:
    print('''  / 4 4 \ ''' + spacing * " " +  ''' / 4 4 \ ''')
          
def print_beak(spacing:int) -> None:
    print('''  \_ v _/ ''' + spacing * " " +  ''' \_ v _/ ''')

def print_chest(spacing:int) -> None:
    print("  //   \\\\" + spacing * " " +  "  //   \\\\")

def print_belly(spacing:int) -> None:
    print(''' ((     ))''' + spacing * " " +  '''((     ))''')

def print_feet(spacing:int) -> None:
    print(''' =""===""='''+ spacing * "=" + '''=""===""=''')

def print_tail(spacing:int) -> None:
    print('''    |||   ''' + spacing * " " + '''   |||   ''')

#constructs image
def print_two_owls() -> None:
    print_crown(x)
    print_eyes(x)
    print_beak(x)
    print_chest(x)
    print_belly(x)
    print_feet(x)
    print_tail(x)
    

def main():
    print_two_owls()

main()
