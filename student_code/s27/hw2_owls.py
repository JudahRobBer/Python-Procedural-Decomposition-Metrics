
import random

def print_crown() -> None:
    return ("  .-\"-.  ") 

def print_eyes() -> None:
    return (" / 4 4 \ ")  
          
def print_beak() -> None:
    return (" \_ v _/ ") 

def print_chest() -> None:
    return (" //   \\\ ") 

def print_belly() -> None:
    return ("((     ))")   

def print_feet() -> None:
    return ("=\"\"===\"\"=")  

def print_tail() -> None:
    return ("   |||   ")   

def print_two_owls() -> None:
    
    #random distance generated for branch length
    distance = random.randint(5, 20)
    
    print(print_crown() + str(distance * " ") + print_crown())   
    print(print_eyes() + str(distance * " ") + print_eyes())
    print(print_beak() + str(distance * " ") + print_beak())
    print(print_chest() + str(distance * " ") + print_chest())
    print(print_belly() + str(distance * " ") + print_belly())
    print(print_feet() + str(distance * "=") + print_feet())
    print(print_tail() + str(distance * " ") + print_tail())
    
def main():
    
    print_two_owls()
    
main()

