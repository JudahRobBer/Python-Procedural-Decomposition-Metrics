

import random

def print_ws(t1,t2,s):
    #ws stands for w/ space
    print(t1+' '*s+t2)

def print_crown(a,b,s) -> None:
    crown = ['  .-"-.  ','  .---.  ','  .-"-.  ']
    print_ws(crown[a],crown[b],s)

def print_eyes(a,b,s) -> None:
    eyes = [' / 4 4 \\ ',' / _ _ \\ ',' /   6_6 ']
    print_ws(eyes[a],eyes[b],s)
          
def print_beak(a,b,s) -> None:
    beak = [' \\_ v _/ ',' \\_ v _/ ',' \\_  (__\\']
    print_ws(beak[a],beak[b],s)

def print_chest(a,b,s) -> None:
    print_ws(' //   \\\\ ',' //   \\\\ ',s)

def print_belly(a,b,s) -> None:
    print_ws(' ((   )) ',' ((   )) ',s)

def print_feet(a,b,s) -> None:
    feet = ['=""===""=','=========','=""===""=']
    print(feet[a]+'='*s+feet[b])

def print_tail(a,b,s) -> None:
    print_ws('   |||   ','   |||   ',s)

def print_two_owls() -> None:
    a = random.choice(range(3))
    b = random.choice(range(3))
    s = random.randint(5,20)
    #s stands for space
    #print(a,b,s)
    print_crown(a,b,s)
    print_eyes(a,b,s)
    print_beak(a,b,s)
    print_chest(a,b,s)
    print_belly(a,b,s)
    print_feet(a,b,s)
    print_tail(a,b,s)

def main():
    print_two_owls()

main()
