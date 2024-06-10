

#Defining each individual section of the tower
def stem() -> None:
    print('      ||      ')
    print('      ||      ')

def tower_base() -> None:
    print('   __{{}}__')
    print('__{::::::::}__')
    print('||||||||||||||')
    
def tower_middle() -> None:
    print('(_)()()()()(_)')
    print('  (_)()()(_)  ')
    print('  ____][____  ')
    print('   ___][___   ')
    stem()
    print('   |%%%%%%|   ')
    print('   |%%%%%%|   ')
    print('   |%%%%%%|   ')
    print('   |%%%%%%|   ')
    
#How to draw the whole tower
def main() -> None:  
    stem()           
    tower_base() 
    tower_middle()   
    tower_base()     
    
main()