"""
test code for using ast's to count the lines of code 
"""


a = 1
if a == 1:
    print(a)

print(a)

def add(a,b):
    return a + b

b = 2
print(add(a,b))


#expected GLOC: 5

