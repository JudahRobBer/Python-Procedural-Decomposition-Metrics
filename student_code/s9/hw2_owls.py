

def print_crown(b) -> None:
    print( '''  .-"-.  '''+b*" "+'''  .-"-.''')
#the function of the crown

def print_eyes(b) -> None:
    print(''' / 4 4 \\ '''+b*" "+''' / 4 4 \\ ''')
#the function of the eyes
          
def print_beak(b) -> None:
    print(''' \_ v _/ '''+b*" "+''' \_ v _/ ''')
#the function of the beak

def print_chest(b) -> None:
    print(''' //   \\\\ '''+b*" "+''' //   \\\\''')
#the chest

def print_belly(b) -> None:
    print('''((     ))'''+b*" "+'''((     ))''')
#the belly

def print_feet(b) -> None:
    print('''=""===""='''+b*"="+'''=""===""=''')
#the feet

def print_tail(b) -> None:
    print('''   |||   '''+b*" "+'''   ||| ''')
#the tail

def print_two_owls(b) -> None:
    print_crown(b)
    print_eyes(b)
    print_beak(b)
    print_chest(b)
    print_belly(b)
    print_feet(b)
    print_tail(b)
#calling the previous functions
    
def main():
    import random
    a=random.randint(5,20)
#making the random distance
    
    print_two_owls(a)

main()
