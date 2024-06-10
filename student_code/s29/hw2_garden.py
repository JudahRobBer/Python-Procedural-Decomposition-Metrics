

def area_calc(side_len): #Calculates circle area, fruitful function
    pi = 3.14
    circle_area = pi * (side_len/4)**2
    return circle_area

def plants(circle_area, plant_spacing): #Provides number of plants needed
    circle_plants = int(circle_area / plant_spacing ** 2)
    semi_plants = int(circle_area / 2 / plant_spacing ** 2) 
    total_plants = circle_plants + semi_plants * 4
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)
    
def fill_calc(side_len, circle_area, fill_depth): #Provides the total fill for garden
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")
    
def soil(circle_area, soil_depth): #Gives soil needed for garden and its different parts
    circle_soil = circle_area/9 * soil_depth/3
    total_soil = circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")

def main():
    #Asks a bunch of prompting questions
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    circle_area = area_calc(side_len) #Saves the area calculation to circle_area in main function
    plants(circle_area, plant_spacing)
    soil(circle_area, soil_depth) #The order of the last two reflects the example code on the assignment sheet
    fill_calc(side_len, circle_area, fill_depth)
    

main() #One main function


#All initially provided code is below
'''
side_len = float(input("Enter length of side of garden (feet): "))
plant_spacing = float(input("Enter spacing between plants (feet): "))
soil_depth = float(input("Enter depth of garden soil (feet): "))
fill_depth = float(input("Enter depth of fill (feet): "))

pi = 3.14
circle_area = pi * (side_len/4)**2 
circle_plants = int(circle_area / plant_spacing ** 2)
semi_plants = int(circle_area / 2 / plant_spacing ** 2) 
total_plants = circle_plants + semi_plants * 4
print()
print("Plants for each semicircle garden:", semi_plants)
print("Plants for the circle garden:", circle_plants)
print("Total plants for garden:", total_plants)

fill_area = side_len**2 - circle_area * 3
total_fill = fill_area/9 * fill_depth/3
print("Total fill for the garden:", round(total_fill, 1), "cubic yards")

circle_soil = circle_area/9 * soil_depth/3
total_soil = circle_soil * 3
print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
print("Total soil for the garden:", round(total_soil, 1), "cubic yards")
'''