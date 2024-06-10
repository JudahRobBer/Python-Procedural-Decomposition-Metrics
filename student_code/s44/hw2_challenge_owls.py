
def print_crown() -> None:
    crown= str("""  .-"-.         .-"-.         ."-".  		    .">.<".""")
    print(crown)

def print_eyes() -> None:
    eyes= str(" / 4 4 \\       / 4 4 \\       / - - \\    	    / - 6 \\")
    print(eyes)
          
def print_beak() -> None:
    beak= str(" \\_ v _/       \\_ v _/       \\_ v _/		    \\_ v _/")
    print(beak)

def print_chest() -> None:
    chest= str(" //   \\\\       //   \\\\       //   \\\\  		   //     \\\\")
    print(chest)

def print_belly() -> None:
    belly= str("((     ))     ((     ))     ((  0  ))	          ((       ))")
    print(belly)

def print_feet() -> None:
    feet= str("""=""===""=======""===""=======""===""===============""=====""===""")
    print(feet)

def print_tail() -> None:
    tail= str("   |||           |||           |||	              |||")
    print(tail)

def print_two_owls() -> None:
    print_crown()
    print_eyes()
    print_beak()
    print_chest()
    print_belly()
    print_feet()
    print_tail()

def main():
    print_two_owls()

main()
