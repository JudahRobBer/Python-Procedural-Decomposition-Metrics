
#Get user input
side_len = float(input("Enter length of side of garden (feet): "))
plant_spacing = float(input("Enter spacing between plants (feet): "))
soil_depth = float(input("Enter depth of garden soil (feet): "))
fill_depth = float(input("Enter depth of fill (feet): "))

#beggining of defining functions to be used
def circle_area():
    pi = 3.14
    circle_area = pi * (side_len/4)**2
    return circle_area

def circle_plants():
    circle_plants = int(circle_area() / plant_spacing ** 2)
    return circle_plants

def semi_circle():
    semi_plants = int(circle_area() / 2 / plant_spacing ** 2)
    return semi_plants

def total_plants():
    total_plants = circle_plants() + semi_circle() * 4
    return total_plants

#in the above functions, total_plants() depends on circle_plants and semi_circle(), which both depent on circle_area()
#This is so that these functions can be reused, as they each have a specific functions

#Finds the total_fill area, and converts to yards
def fill():
    fill_area = side_len**2 - circle_area() * 3
    total_fill = fill_area/9 * fill_depth/3
    total_fill = round(total_fill, 1)
    return total_fill

#uses circle area, which shows that the call back to the function is efficient.
def circle_soil():  
    circle_soil = circle_area()/9 * soil_depth/3
    return circle_soil

def total_soil():
    total_soil = circle_soil() * 3
    return total_soil

#main() calls all the functions, and displays them.
def main():
    print("Plants for each semicircle garden:", semi_circle())
    print("Plants for the circle garden:", circle_plants())
    print("Total plants for garden:", total_plants())
    print("Soil for each semicircle garden:", round(circle_soil()/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil(), 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil(), 1), "cubic yards")
    print("Total fill for the garden:", round(fill(), 1), "cubic yards")

main()