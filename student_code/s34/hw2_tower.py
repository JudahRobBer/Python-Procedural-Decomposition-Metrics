

#creating a function for spire (also seen in body)
def spire() -> None:
    print("      ||      ")
    print("      ||      ")
    
#creating a function for base (also seen in bulb)
def base() -> None:
    print("   __{{}}__   ")
    print("__{::::::::}__")
    print("||||||||||||||")

#creating a function for bottom of the bulb
def lower_bulb() -> None:
    print("(_)()()()()(_)")
    print("  (_)()()(_)  ")
    print("  ____][____  ")
    print("   ___][___   ")
    
#creating a function for midsection
def middle() -> None:
    print("   |%%%%%%|   ")
    print("   |%%%%%%|   ")
    print("   |%%%%%%|   ")
    print("   |%%%%%%|   ")
    
#creating a function to put the tower together
def main() -> None:
    spire()
    base()
    lower_bulb()
    spire()
    middle()
    base()
    
#calling the function that creates the whole tower
main()

