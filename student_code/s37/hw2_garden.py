


def main() -> None:
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    
    plants(plant_spacing, circ_area(side_len))
    gardenSoil(soil_depth, circ_area(side_len))
    totalFill(side_len, fill_depth, circ_area(side_len))

def circ_area (side_len: float) -> float:
    pi = 3.14 
    circle_area = pi * (side_len/4)**2
    return circle_area

def plants(plant_spacing: float, circle_area: float) -> None:
    circle_plants = int(circle_area / plant_spacing ** 2)
    semi_plants = int(circle_area / 2 / plant_spacing ** 2) 
    total_plants = circle_plants + semi_plants * 4
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)

def totalFill(side_len: float, fill_depth: float, circle_area: float) -> None:

    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")

def gardenSoil(soil_depth: float, circle_area: float) -> None:
    circle_soil = circle_area/9 * soil_depth/3
    total_soil = circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")
    
main()