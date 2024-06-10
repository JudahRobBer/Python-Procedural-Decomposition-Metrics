

def spire():
    for i in range(2):
        print('      ||')

def base():
    print('   __{{}}__')
    print('__{::::::::}__')
    print('||||||||||||||')

def middle():
    print('(_)()()()()(_)')
    print('  (_)()()(_)')
    print('  ____][____')
    print('   ___][___')

def pillar():
    for i in range(4):
        print('   |%%%%%%|')

def main():
    spire()
    base()
    middle()
    spire()
    pillar()
    base()

main()
