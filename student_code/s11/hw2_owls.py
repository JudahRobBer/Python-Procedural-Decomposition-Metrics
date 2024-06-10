
import random

def print_crown() -> str:
    return('  .-"-. ')
    
def print_eyes() -> str:
    return(' / 4 4 \\')
          
def print_beak() -> str:
    return(' \\_ v _/')

def print_chest() -> str:
    return('  // \\\\ ') 

def print_belly() -> str:
    return(' ((   ))')

def print_feet() -> str:
    return('=""===""')

def print_tail() -> str:
    return('   |||  ') 
    
def print_two_owls() -> None:
    num_log = random.randrange(5,21)
    logs = num_log * '='
    print(print_crown() + len(logs)*" " + print_crown())
    print(print_eyes() + len(logs)*" " + print_eyes())
    print(print_beak() + len(logs)*" " + print_beak())
    print(print_chest() + len(logs)*" " + print_chest())
    print(print_belly() + len(logs)*" " + print_belly())
    print(print_feet() + logs + print_feet())
    print(print_tail() + len(logs)*" " + print_tail())

print_two_owls()

    

    

    