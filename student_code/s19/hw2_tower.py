

def draw_spire () -> None:
    print ("      ||")

def draw_topshell () -> None:
    print ("   __{{}}__")
    print ("__{::::::::}__")
    print ("||||||||||||||")
    
def draw_bottomshell () -> None:
    print ("(_)()()()()(_)")
    print ("  (_)()()(_)")
    print ("  ____][____")
    print ("   ___][___")
    
def draw_middle () -> None:
    print ("   |%%%%%%|")

def main () -> None:
    #spire
    draw_spire()
    draw_spire()
    #shell
    draw_topshell()
    draw_bottomshell()
    #connect
    draw_spire()
    draw_spire()
    #middle part
    draw_middle()
    draw_middle()
    draw_middle()
    draw_middle()
    #base
    draw_topshell()
    
main()