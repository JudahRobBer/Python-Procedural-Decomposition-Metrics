
''' practice outputs
Example output 1

Enter length of side of garden (feet): 10
Enter spacing between plants (feet): 0.5
Enter depth of garden soil (feet): 0.8333
Enter depth of fill (feet): 0.8333

Plants for each semicircle garden: 39
Plants for the circle garden: 78
Total plants for garden: 234
Soil for each semicircle garden: 0.3 cubic yards
Soil for the circle garden: 0.6 cubic yards
Total soil for the garden: 1.8 cubic yards
Total fill for the garden: 1.3 cubic yards
Example output 2:

Enter length of side of garden (feet): 13
Enter spacing between plants (feet): 0.25
Enter depth of garden soil (feet): 0.5
Enter depth of fill (feet): 0.25

Plants for each semicircle garden:  265
Plants for the circle garden:  530
Total plants for garden:  1590
Soil for each semicircle garden: 0.3 cubic yards
Soil for the circle garden: 0.6 cubic yards
Total soil for the garden:  1.8 cubic yards
Total fill for the garden: 0.6 cubic yards

'''
#establish global variable pi
pi = 3.14

def c_area(side_len): #calculates circle area
    circle_area = pi * (side_len/4)**2
    return circle_area

def circle_plants(circle_area, plant_spacing): #calculates plants for circle garden, returns it for use, and prints the statement
    cp_plants = int(circle_area / plant_spacing ** 2)
    print("Plants for the circle garden:", cp_plants)
    return cp_plants

def semi_plants(circle_area, plant_spacing): #calculates number of semi plants for each semicircle garden, returns it for use, and prints the statement
    semi_plants = int(circle_area / 2 / plant_spacing ** 2)
    print("Plants for each semicircle garden:", semi_plants)
    return semi_plants
    
def total_plants(circle, semi): #calculates total number of plants
    #factors in 4 semicircular sections
    total_plants = circle + semi * 4
    print("Total plants for garden:", total_plants)
    
def soil(circle_area, soil_depth, a): #calculates circle soil, semicircle soil, and total soil depending on 'a' which will be either circle, semicircle, or total
    if a == 'circle':
        soil = circle_area/9 * soil_depth/3
        print("Soil for the circle garden:", round(soil, 1), "cubic yards")
    elif a == 'semicircle':
        soil = (circle_area/9 * soil_depth/3)/2
        print("Soil for each semicircle garden:", round(soil, 1), "cubic yards")
    else: #total soil
        soil = circle_area/9 * soil_depth
        print("Total soil for the garden:", round(soil, 1), "cubic yards")
    return soil

def total_fill(side_len, circle_area, fill_depth):
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")


def main(): 
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    print()
    circle_area = c_area(side_len) # don't forget to put equals for ones with important return
    
    s_plants = semi_plants(circle_area, plant_spacing) #both of the next two functions return something for later but also print in the process
    c_plants = circle_plants(circle_area, plant_spacing)
    total_plants(c_plants, s_plants)
    
    soil(circle_area, soil_depth, 'semicircle')
    soil(circle_area, soil_depth, 'circle')
    
    soil(circle_area, soil_depth, 'total')
    total_fill(side_len, circle_area, fill_depth) # I spaced these out because the original code didn't print them in the same order the code originally did so this made it easy to move around and test

main()
#print()
#print("Plants for each semicircle garden:", semi_plants)
#print("Plants for the circle garden:", circle_plants)
#print("Total plants for garden:", total_plants)
#print("Total fill for the garden:", round(total_fill, 1), "cubic yards")
#print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
#print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
#print("Total soil for the garden:", round(total_soil, 1), "cubic yards")

#circle_area = pi * (side_len/4)**2 
#circle_plants = int(circle_area / plant_spacing ** 2)
#semi_plants = int(circle_area / 2 / plant_spacing ** 2) 
#total_plants = circle_plants + semi_plants * 4

#print()

#print("Plants for each semicircle garden:", semi_plants)
#print("Plants for the circle garden:", circle_plants)
#print("Total plants for garden:", total_plants)

#fill_area = side_len**2 - circle_area * 3
#total_fill = fill_area/9 * fill_depth/3
#print("Total fill for the garden:", round(total_fill, 1), "cubic yards")

#circle_soil = circle_area/9 * soil_depth/3
#total_soil = circle_soil * 3
#print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
#print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
#print("Total soil for the garden:", round(total_soil, 1), "cubic yards")