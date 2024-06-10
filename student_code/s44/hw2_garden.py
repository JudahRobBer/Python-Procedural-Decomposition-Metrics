
def plant_information(circle_area, plant_spacing) -> None:
    circle_plants = int(circle_area / plant_spacing ** 2)
    semi_plants = int(circle_area / 2 / plant_spacing ** 2)
    total_plants = circle_plants + semi_plants * 4
    print("\nPlants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)


def fill_information(circle_area, fill_depth, side_len) -> None:
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")


def soil_information(circle_area, soil_depth) -> None:
    circle_soil = circle_area/9 * soil_depth/3
    total_soil = circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")

def main() -> None:
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    pi = 3.14
    circle_area = pi * (side_len/4)**2
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))

    plant_information(circle_area, plant_spacing)
    soil_information(circle_area, soil_depth)
    fill_information(circle_area, fill_depth, side_len)
    
main()