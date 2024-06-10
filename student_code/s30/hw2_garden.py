

def plants(side_len, plant_spacing) -> int: # returns circle_area
    pi = 3.14
    circle_area = pi * (side_len/4)**2   # calculate circle area
    circle_plants = int(circle_area / plant_spacing ** 2)  # calculate circle plants
    semi_plants = int(circle_area / 2 / plant_spacing ** 2)  # calculate semi plants
    total_plants = circle_plants + semi_plants * 4           # calculate total plants
    print()                                                  # print calculation results 
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)
    return circle_area  

def fill_area(side_len, fill_depth, circle_area) -> None:
    fill_area = side_len**2 - circle_area * 3 # calculate fill area
    total_fill = fill_area/9 * fill_depth/3   # calculate total fill
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")
 
def soil(soil_depth, circle_area) -> None:      # soil
    circle_soil = circle_area/9 * soil_depth/3  # calculate circle soil
    total_soil = circle_soil * 3                # calculate total soil
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")  # print calculation results
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")

def main() -> None:  # function calls
    side_len = float(input("Enter length of side of garden (feet): "))  # inputs
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    x = plants(side_len, plant_spacing)
    soil(soil_depth, x)
    fill_area(side_len, fill_depth, x)
    
main()