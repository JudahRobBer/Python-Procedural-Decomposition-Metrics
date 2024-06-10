def spire() -> None:
    print('      ||')
    print('      ||')

def topshell() -> None:
    print('   __{{}}__')
    print('__{::::::::}__')
    print('|' + "|"* 12 +'|')

def bottomshell() -> None:
    print("(_)" + '()'*4 + '(_)')
    print("  (_)()()(_)")

def middle() -> None:
    print("  "+"_"*4 + "][" + "_"*4)
    print("   "+"_"*3 + "][" + "_"*3)
    spire()
    print("   |%%%%%%|\n"*4, end="")

def main() -> None:
    spire()
    topshell()
    bottomshell()
    middle()
    topshell()

main()
