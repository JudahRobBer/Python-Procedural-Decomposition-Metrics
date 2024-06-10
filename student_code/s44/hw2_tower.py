
def print_top() -> None:
    top=str("      ||\n      ||")
    print(top)
    
def print_curly_dots_and_lines() -> None:
    curly_bracket= str("   __{{}}__")
    dots= str("__{::::::::}__")
    lines= str("||||||||||||||")
    print(curly_bracket)
    print(dots)
    print(lines)
    
def print_circles() -> None:
    circles= str("(_)()()()()(_)\n  (_)()()(_)")
    print(circles)
            
def print_more_lines () -> None:
    ml= str("  ____][____\n   ___][___")
    print(ml)
    
def print_percent() -> None:
    percentage= str("   |%%%%%%|")
    print(percentage)
    print(percentage)
    print(percentage)
    print(percentage)

def print_tower() -> None:
    print_top()
    print_curly_dots_and_lines()
    print_circles()
    print_more_lines()
    print_top()
    print_percent()
    print_curly_dots_and_lines()

print_tower()