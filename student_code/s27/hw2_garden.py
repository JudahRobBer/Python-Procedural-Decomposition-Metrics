

import math

#calculate number of plants that fit in semicircle garden    
def calculate_circle_plants(side_len , plant_spacing):
    pi = 3.14
    circle_area = pi * (side_len/4)**2 
    circle_plants = int(circle_area / plant_spacing ** 2)
    return circle_plants

#calculate number of plants that fit in circle garden
def calculate_semi_plants(side_len , plant_spacing):
    pi = 3.14
    circle_area = pi * (side_len/4)**2
    semi_plants = int(circle_area / 2 / plant_spacing ** 2)
    return semi_plants

#calculate total number of plants that fit in garden
def calculate_total_plants(circle_plants, semi_plants):
    total_plants = circle_plants + semi_plants * 4
    return total_plants

#calculate the total fill of the garden
def calculate_total_fill(side_len, circle_area, fill_depth):
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    return total_fill

#calculate the soil needed for the circle garden
def calculate_circle_soil(circle_area, soil_depth):
    circle_soil = circle_area/9 * soil_depth/3
    return circle_soil

#calculate the soil needed for the total garden
def calculate_total_soil(circle_soil):
    total_soil = circle_soil * 3
    return total_soil

def main() -> None:
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    
    pi = 3.14
    circle_area = pi * (side_len/4)**2
    
    circle_plants = calculate_circle_plants(side_len , plant_spacing)
    semi_plants = calculate_semi_plants(side_len , plant_spacing) 
    total_plants = calculate_total_plants(circle_plants, semi_plants)
    total_fill = calculate_total_fill(side_len, circle_area, fill_depth)
    circle_soil = calculate_circle_soil(circle_area, soil_depth)
    total_soil = calculate_total_soil(circle_soil)
    
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")
    
main()