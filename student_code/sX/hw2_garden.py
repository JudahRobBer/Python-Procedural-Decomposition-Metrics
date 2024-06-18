

def plant_math(side_len, plant_spacing):
    pi = 3.14
    circle_area = pi * (side_len/4)**2 
    circle_plants = int(circle_area / plant_spacing ** 2)
    semi_plants = int(circle_area / 2 / plant_spacing ** 2) 
    total_plants = circle_plants + semi_plants * 4
    return semi_plants, circle_plants, total_plants
#the previous code statements stay the same but has been made into a function
#it will return the variables that we need

def fill_soil_math(side_len, fill_depth, soil_depth, semi_plants, circle_plants):
    pi = 3.14
    circle_area = pi * (side_len/4)**2 
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    circle_soil = circle_area/9 * soil_depth/3
    total_soil = circle_soil * 3
    return total_fill, circle_soil, total_soil
#the blocks of code which were once divided by a print function are put together
#code statements are not altered, but they are made into a function

def main():
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
#input functions are put into a function called main(), so we can call it later

    semi_plants, circle_plants, total_plants = plant_math(side_len, plant_spacing)
#these are the variables that the function has been asked to return
#we are assigning variables on the left side of the = sign
#we are calling the function with the arguments on the right side of the = sign
#we need to assign them here because they were only local variables before
#we are able to assign multiple variables in one line of code for efficiency
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)

    total_fill, circle_soil, total_soil = fill_soil_math(side_len, fill_depth, soil_depth, semi_plants, circle_plants)
#this line of code has the same function as the previous variable assignment line
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")
#none of the print statements are altered

main()
#we can start the code by calling the "main" function that we made
