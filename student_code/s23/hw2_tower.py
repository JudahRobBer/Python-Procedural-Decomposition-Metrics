
#the first fuction will draw the spire which is used twice in the tower
def draw_spire() -> None:
    print("      ||      ")
    print("      ||      ")
    
#the second fuction will draw the top and base which is used twice in the tower    
def  draw_topshell_base() -> None:
    print("   __{{}}__   ")
    print("__{::::::::}__")
    print("||||||||||||||")

#the third fuction will draw the higher of the two middle pieces in the tower
def draw_middle() -> None:
    print("(_)()()()()(_)")
    print("  (_)()()(_)  ")
    print("  ____][____  ")
    print("   ___][___   ")

#the fourth function will draw the lower of the two middle pieces in the the tower
def draw_bottomshell() -> None:
    print("   |%%%%%%|   ")
    print("   |%%%%%%|   ")
    print("   |%%%%%%|   ")
    print("   |%%%%%%|   ")

#this function puts all the pieces of the tower in the proper order
def draw_tower() -> None:
    draw_spire() 
    draw_topshell_base()
    draw_middle()
    draw_spire()
    draw_bottomshell()
    draw_topshell_base() 

# the last function calls the tower we put together 
def main() -> None:
    draw_tower()
    
main()    
    