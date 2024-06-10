

# imported random module from python
import random
# print_crown function prints the crown of the owls for one owl first and concatenates it with the distance * " " which is the value transfered from the print_two_owls function and concatenates it again with the crown for the second owl. This process is repeated for the next two owls.
def print_crown(distance:int) -> int:
    print(( '  .-"-. ')  + distance * " " +  ( '   .---. ')  + distance * " " + ('  .-"-. ') + distance * " " + ('    .-|-. '))
    
# print_eyes function prints the eyes of the owls for one owl first and concatenates it with the distance * " " which is the value transfered from the print_two_owls function and concatenates it again with the eyes for the second owl. This process is repeated for the next two owls.
def print_eyes(distance:int) -> int:
     print((  " / 4 4 \\") + distance * " " + (   "  / - - \\") + distance * " " + (' /   6_6 ') + distance * " " + (  "  / $ $ \\"))
    
# print_beak function prints the beaks of the owls for one owl first and concatenates it with the distance * " " which is the value transfered from the print_two_owls function and concatenates it again with the beak for the second owl. This process is repeated for the next two owls.
def print_beak(distance:int) -> int: 
     print((  " \_ V _/ ") + distance * " " + (   " \_ V _/ ") + distance * " " + ('\_  (__\ ')+ distance * " " + (   " \_ O _/ "))
     
# print_chest function prints the chests of the owls for one owl first and concatenates it with the distance * " " which is the value transfered from the print_two_owls function and concatenates it again with the chest for the second owl. This process is repeated for the next two owls.
def print_chest(distance:int) -> int:
     print((  " //   \\\ ") + distance * " " + (  " //   \\\ ") + distance * " " + (  "//   \\\ ") + distance * " " + (  "  //   \\\ "))
     
# print_belly function prints the bellies of the owls for one owl first and concatenates it with the distance * " " which is the value transfered from the print_two_owls function and concatenates it again with the belly for the second owl. This process is repeated for the next two owls.
def print_belly(distance:int) -> int:
     print((  " ((   ))") + distance * " " + (  "  ((   ))") + distance * " " + (" ((   ))" ) + distance * " " + (  "   ((   ))"))

# print_feet function prints the feet of the owls for one owl first and concatenates it with the distance * " " which is the value transfered from the print_two_owls function and concatenates it again with the feet for the second owl. This process is repeated for the next two owls.
def print_feet(distance:int) -> int:
     print((  '=""===""=') + distance * branch() + ('======') + distance * branch() + ('===""===""=') + distance * branch() + ('==""===""='))
         
# print_tail function prints the tails of the owls for one owl first and concatenates it with the distance * " " which is the value transfered from the print_two_owls function and concatenates it again with the tail for the second owl. This process is repeated for the next two owls.
def print_tail(distance:int) -> int:
     print((  "   |||  ") + distance * " " + (  "    |||  ") + distance * " " + (  "   |||  ") + distance * " " +  (  "     |||  "))
          
# The branch function returns the string, "="
def branch() -> str:
     return  "="
    
# print_two_owls contains the variable distance which is assigned to a random number between 5 and 20 which is then transfered to all the other functions    
def print_two_owls() -> None:
    distance = random.randint(5,20)
    print_crown(distance)
    print_eyes(distance) 
    print_beak(distance)
    print_chest(distance)
    print_belly(distance)
    print_feet(distance)
    print_tail(distance)
    
# main function calls print_two_owls
def main():
    print_two_owls()

main()
