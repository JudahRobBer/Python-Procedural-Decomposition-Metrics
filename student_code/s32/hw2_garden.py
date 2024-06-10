

#defining functions to be used in outputs:
def find_circle_area(side_len) -> None:
    pi = 3.14
    circle_area = pi * (side_len / 4) ** 2
    return circle_area

def find_circle_plants(circle_area, plant_spacing) -> None:
    circle_plants = int(circle_area / plant_spacing ** 2)
    return circle_plants
    
def find_semi_plants(circle_area, plant_spacing) -> None:
    semi_plants = int(circle_area / 2 / plant_spacing ** 2)
    return semi_plants

def find_total_plants(circle_plants, semi_plants) -> None:
    total_plants = circle_plants + semi_plants * 4
    return total_plants

def find_fill_area(side_len, circle_area) -> None:
    fill_area = side_len ** 2 - circle_area * 3
    return fill_area

def find_soil_volume(circle_area, soil_depth) -> None:
    circle_soil = circle_area / 9 * soil_depth / 3
    return circle_soil

def find_total_soil(circle_soil) -> None:
    total_soil = circle_soil * 3
    return total_soil

def find_fill_volume(fill_area, fill_depth) -> None:
    total_fill = fill_area / 9 * fill_depth / 3
    return total_fill

#defining main()
def main() -> None:
    #inputs
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    #definitions
    circle_area = find_circle_area(side_len)
    circle_plants = find_circle_plants(circle_area, plant_spacing)
    semi_plants = find_semi_plants(circle_area, plant_spacing)
    total_plants = find_total_plants(circle_plants, semi_plants)
    fill_area = find_fill_area(side_len, circle_area)
    circle_soil = find_soil_volume(circle_area, soil_depth)
    total_soil = find_total_soil(circle_soil)
    total_fill = find_fill_volume(fill_area, fill_depth)
    #outputs
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)
    print("Soil for each semicircle garden:", round(circle_soil / 2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")

main()