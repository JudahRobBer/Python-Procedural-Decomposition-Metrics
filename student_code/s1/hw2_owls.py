
import random
space = int(random.randint(5,20))

def print_crown(space:int) -> None:
    print ('  .-"-.',' ' * space,'  .-"-.')

def print_eyes(space:int) -> None:
    print (' / 4 4 \\',' ' * (space-1),' / 4 4 \\')
          
def print_beak(space:int) -> None:
    print (' \_ v _/',' ' * (space-1),' \_ v _/')

def print_chest(space:int) -> None:
    print (' //    \\\\',' ' * (space-1),'//   \\\\' )

def print_belly(space:int) -> None:
    print ('((     ))',' ' * (space-2),'((     ))')

def print_feet(space:int) -> None:
    print ('=""===""','=' * space,'=""===""')

def print_tail(space:int) -> None:
    print ('   |||',' ' * space,'    |||')

def print_two_owls(space:int) -> None:
    print_crown(space)
    print_eyes(space)
    print_beak(space)
    print_chest(space)
    print_belly(space)
    print_feet(space)
    print_tail(space)

def main(space:int):
    print_two_owls(space)


main(space)


