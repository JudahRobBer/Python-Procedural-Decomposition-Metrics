

# Define function to print the spire of the tower
def spire()->None:
    print('      ||')
    print('      ||')

# Define function to print the topshell or base of the tower
def topshell_or_base()->None:
    print('   __{{}}__')
    print('__{::::::::}__')
    print('||||||||||||||')

# Define function to print the bottomshell of the tower
def bottomshell()->None:
    print('(_)()()()()(_)')
    print('  (_)()()(_)')
    print('  ____][____')
    print('   ___][___')

# Define function to print the middle section of the tower
def middle()->None:
    print('   |%%%%%%|')
    print('   |%%%%%%|')
    print('   |%%%%%%|')
    print('   |%%%%%%|')

# Define the main function to assemble and print the tower
def main() -> None:
    # Print each part in the tower
    spire()
    topshell_or_base()
    bottomshell()
    spire()
    middle()
    topshell_or_base()

# Call the main function to assemble and print the tower
main()