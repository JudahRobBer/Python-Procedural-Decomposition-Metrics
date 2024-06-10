

#importing module to use in main function for "random.randint"
import random

#next arrangement of functions used to print components of the owls line by line

def print_crown(x: int) -> None:
    print("""  .-"-.  """ + x * (" ") + """  .---.  """ + x * (" ") + """  .-"-.  """)
    
def print_eyes(x: int) -> None:
    print(" / 4 4 \ " + x * (" ") + " / _ _ \ " + x * (" ") + " /   6_6")
          
def print_beak(x: int) -> None:
    print(" \_ v _/ " + x * (" ") + " \_ v _/ " + x * (" ") + " \_  (__\ ")

def print_chest(x: int) -> None:
    print(" //   \\\\" + x * (" ") + "  //   \\\\" + x * (" ") + "  //   \\\\")

def print_belly(x: int) -> None:
    print("((     ))" + x * (" ") + "((     ))" + x * (" ") + "((     ))")

def print_feet(x: int) -> None:
    print("=\"\"===\"\"=" + x * ("=") + ("=====") + x * ("=") + "=====\"\"===\"\"=")

def print_tail(x: int) -> None:
    print("   |||" + x * (" ") + ("      |||") + x * (" ") + "      |||")

#function to print 3 owls using the previous functions
def print_three_owls(x: int) -> None:
    print_crown(x)
    print_eyes(x)
    print_beak(x)
    print_chest(x)
    print_belly(x)
    print_feet(x)
    print_tail(x)

#main function that randomly chooses an integer 5-20 and then uses that integer as spacing for the 3 owls.
def main():
    x = random.randint(5, 20)
    print_three_owls(x)

main()
