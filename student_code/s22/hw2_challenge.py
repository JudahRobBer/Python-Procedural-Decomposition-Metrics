

# Import the random module for generating random distances
import random

# Function to print the crown of the owl
def print_crown(distance:int) -> None:
    print('  .-*-. '+' '*distance+'-.-=-.- '+' '*distance+'.---.'+' '*(distance+2)+'.|*|.')

# Function to print the eyes of the owl
def print_eyes(distance:int) -> None:
    print(' / 6 6 \\'+' '*distance+'| * * | '+' '*distance+'|^ ^|'+' '*(distance+2)+'(- -) ')

# Function to print the beak of the owl
def print_beak(distance:int) -> None:
    print(' \_ v _/'+' '*distance+'|_ ^ _| '+' '*distance+'\_^_/'+' '*(distance+2)+'\\_^_/ ')

# Function to print the chest of the owl
def print_chest(distance:int) -> None:
    print(' |     |'+' '*distance+'//   \\\\'+' '*distance+'</   \\>'+' '*distance+'-/   \\- ')

# Function to print the belly of the owl
def print_belly(distance:int) -> None:
    print(' {     }'+' '*(distance-2)+'  [     ]'+' '*(distance-2)+' 《      》'+' '*(distance-1)+'{    }')

# Function to print the feet of the owl
def print_feet(distance:int) -> None:
    print('=""===""'+"="*distance+'""===""='+"="*(distance-1)+'""===""='+"="*(distance-1)+'""===""=')

# Function to print the tail of the owl
def print_tail(distance:int) -> None:
    print('   |||  '+' '*distance+'  |||  '+' '*distance+'  ||| '+' '*(distance+2)+' |||   ')

# The function to print two owls with random distances
def print_two_owls() -> None:
    # Generate a random distance for the owls
    distance = random.randint(5, 20)
    # Print each part of the owls
    print_crown(distance)
    print_eyes(distance)
    print_beak(distance)
    print_chest(distance)
    print_belly(distance)
    print_feet(distance)
    print_tail(distance)

# The main function that executes the program
def main() -> None:
    # Print two owls with random distances
    print_two_owls()

# Call the main function to start the program
main()
