
import random

#All the body parts using end to not go to next line
def print_crown() -> None:
    print("  .-\"-.  ", end="")

def print_eyes() -> None:
    print(" / 4 4 \\ ", end="")
          
def print_beak() -> None:
    print(" \\_ v _/ ", end="")

def print_chest() -> None:
    print(" //   \\\\ ", end="")

def print_belly() -> None:
    print("((     ))", end="")

def print_feet() -> None:
    print("=\"\"===\"\"=", end="")

def print_tail() -> None:
    print("   |||   ", end="")

def space(dist) -> None:
    print(" "*dist, end="")

def branch(dist) -> None:
    print("="*dist, end="")
    
def print_two_owls() -> None:
    dist = random.randint(5, 20)
#Getting random num as the distance.
#Printing the body part of one owl, the space, the same part of the second owl, and a next line
    print_crown()
    space(dist)
    print_crown()
    print()
    
    print_eyes()
    space(dist)
    print_eyes()
    print()
    
    print_beak()
    space(dist)
    print_beak()
    print()
    
    print_chest()
    space(dist)
    print_chest()
    print()
    
    print_belly()
    space(dist)
    print_belly()
    print()
    
    print_feet()
    branch(dist)
    print_feet()
    print()
    
    print_tail()
    space(dist)
    print_tail()
    print()


#all Extra Credit Below Here
def sleepingFace1() -> None:
    print("  .---.  ", end="")
def sleepingFace2() -> None:
    print(" / _ _ \\ ", end="")
def sleepingFace3() -> None:
    print(" \\_ v _/ ", end="")
          
def lookingFace1() -> None:
    print("  .-\"-.  ", end="")
def lookingFace2() -> None:
    print(" /   6_6 ", end="")
def lookingFace3() -> None:
    print(" \\_  (__\\", end="")
    
def threeOwls() -> None:
    dist1 = random.randint(3, 25)
    dist2 = random.randint(3, 25)
    
    print_crown()
    space(dist1)
    sleepingFace1()
    space(dist2)
    lookingFace1()
    print()
    
    print_eyes()
    space(dist1)
    sleepingFace2()
    space(dist2)
    lookingFace2()
    print()
    
    print_beak()
    space(dist1)
    sleepingFace3()
    space(dist2)
    lookingFace3()
    print()
    
    print_chest()
    space(dist1)
    print_chest()
    space(dist2)
    print_chest()
    print()
    
    print_belly()
    space(dist1)
    print_belly()
    space(dist2)
    print_belly()
    print()
    
    print_feet()
    branch(dist1)
    print_feet()
    branch(dist2)
    print_feet()
    print()
    
    print_tail()
    space(dist1)
    print_tail()
    space(dist2)
    print_tail()
    print()
    
    
def main():
    print_two_owls()
    print("\n\n\n\n")
    threeOwls()

main()
