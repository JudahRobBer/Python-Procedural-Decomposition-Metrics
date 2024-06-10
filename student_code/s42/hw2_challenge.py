

# The functions print_crown until print_tail are used to print the parts of the owl line by line while using the int randomized in print_two_owls to standardize the space in between the owls
def print_crown(x: int) -> None:
    print("""  .-"-.  """ + " " * x + """  .---.  """ + " " * x + """  .-"-.  """)
    
def print_eyes(x: int) -> None:
    print(""" / 4 4 \ """ + " " * x + """ / _ _ \ """ + " " * x + """ /   6_6 """)
          
def print_beak(x: int) -> None:
    print(""" \_ v _/ """ + " " * x + """ \_ v _/ """ + " " * x + """ \\_  (__\\""")

def print_chest(x: int) -> None:
    print(""" //   \\\\ """ + " " * x + """ //   \\\\ """ + " " * x + """ //   \\\\ """)

def print_belly(x: int) -> None:
    print("""((     ))""" + " " * x + """((     ))""" + " " * x + """((     ))""")

def print_feet(x: int) -> None:
    print("""=""===""=""" + "=" * x + """=""===""=""" + "=" * x + """=""===""=""")

def print_tail(x: int) -> None:
    print("""   |||   """ + " " * x + """   |||   """ + " " * x + """   |||   """)

# print_two_owls randomizes the distance between the owls and calls upon the print functions for the owl
def print_two_owls() -> None:
    import random
    distance = random.randint(5, 20)
    print_crown(distance)
    print_eyes(distance)
    print_beak(distance)
    print_chest(distance)
    print_belly(distance)
    print_feet(distance)
    print_tail(distance)

def main():
    print_two_owls()

main()

