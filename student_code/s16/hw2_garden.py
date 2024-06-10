
def plants(side_len, plant_spacing):
    pi = 3.14
    circle_area = pi * (side_len/4)**2 
    circle_plants = int(circle_area / plant_spacing ** 2)
    semi_plants = int(circle_area / 2 / plant_spacing ** 2) 
    total_plants = circle_plants + semi_plants * 4
    return circle_plants, semi_plants, total_plants

def fill(side_len, circle_area, fill_depth):
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    return round(total_fill, 1) 

def soil(circle_area, soil_depth):
    circle_soil = circle_area/9 * soil_depth/3
    total_soil = circle_soil * 3
    return round(circle_soil/2, 1), round(circle_soil, 1), round(total_soil, 1)  
    
def main() -> None:
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    pi = 3.14
    circle_area = pi * (side_len/4)**2
    
    semi_plants, circle_plants, total_plants = plants(side_len, plant_spacing)
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)
    
    total_fill = fill(side_len, circle_area, fill_depth)
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")
    
    circle_soil_half, circle_soil, total_soil = soil(circle_area, soil_depth)
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")
    
main()
    