
def top_base() -> str:
    print('   __{{}}__')
    print('__{::::::::}__')
    print('||||||||||||||')


def middle() -> str:
    for i in range(2):
        print('      ||')


def bottom() -> str:
    for i in range(4):
        print('   |%%%%%%|')


def spire() -> str:
    print('(_)()()()()(_)')
    print('  (_)()()(_)')
    print('  ____][____')
    print('   ___][___')


def main():
    middle()
    top_base()
    spire()
    middle()
    bottom()
    top_base()
    

main()