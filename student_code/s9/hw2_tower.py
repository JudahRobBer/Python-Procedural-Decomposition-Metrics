
"""   ||
      ||
   __{{}}__
__{::::::::}__
||||||||||||||
(_)()()()()(_)
  (_)()()(_)
  ____][____
   ___][___
      ||
      ||
   |%%%%%%|
   |%%%%%%|
   |%%%%%%|
   |%%%%%%|
   __{{}}__
__{::::::::}__
||||||||||||||"""
#spire 17-18，topshell：19-21，middle:22-31, bottomshell:32-34

def spire()->None:
    print("""      ||
      ||""")
#the spire
    
def topshell_base()->None:
    print("""   __{{}}__
__{::::::::}__
||||||||||||||""")
#the topshell

def bottomshell()->None:
    print("""(_)()()()()(_)
  (_)()()(_)
  ____][____
   ___][___""")
#bottomshell
    
def middle()->None:
    print("""   |%%%%%%|
   |%%%%%%|
   |%%%%%%|
   |%%%%%%|""")
#middle
    
def main()->None:
    spire()
    topshell_base()
    bottomshell()
    spire()
    middle()
    topshell_base()

main()
