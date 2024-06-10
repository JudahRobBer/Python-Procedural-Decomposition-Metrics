
import random
s = random.randint(5,20) #for space between the owls

'''
Thought about using a printspace function but it's easier to do it the
way I did it
'''
def print_repeat(s, a): ##prints a repeating number of something. this time it is equals for the branch or spaces
    spaces = (a * s)
    return spaces

    
def print_crown(): #prints both crowns of the owls and the spaces between them
    print('  .-"-.  ' + print_repeat(s," ") + '  .-"-.')

def print_eyes(): #prints both eyes of the owls and the spaces between them
    print(" / 4 4 \\"  + print_repeat(s," ") + "  / 4 4 \\")
          
def print_beak(): #prints both beaks of the owls and the spaces between them
    print(" \\_ v _/"  + print_repeat(s, " ") + "  \\_ v _/")

def print_chest(): #you get the point... just imagine the last few comments but insert (part of body) here
    print(" //   \\\\ " + print_repeat(s," ") + " //   \\\\ ")

def print_belly():
    print("((     ))" + print_repeat(s," ") + "((     ))")

def print_feet():
    print('=""===""=' + print_repeat(s,"=") + '=""===""=')

def print_tail():
    print("   |||   " + print_repeat(s," ") + "   |||   ")


def print_two_owls(): #defines the order in which the owl is printed
    print_crown()
    print_eyes()
    print_beak()
    print_chest()
    print_belly()
    print_feet()
    print_tail()


def main():
    print_two_owls()
    
main() #executes the code
