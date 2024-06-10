

def calculate_circle_area(side_len: float) -> float:
#Calculates the area of the central circle flowerbed.
    pi = 3.14
    circle = pi * (side_len / 4) ** 2
    return circle

def calculate_plants(circle_area: float, plant_spacing: float) -> None:
#Calculates the number of plants needed for the garden.
    circle_plants = int(circle_area / plant_spacing ** 2)
    semi_plants = int(circle_area / 2 / plant_spacing ** 2)
    total_plants = circle_plants + semi_plants * 4
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)

def calculate_soil(circle_area: float, soil_depth: float) -> None:
#Calculates the amount of soil needed for the garden.
    circle_soil = circle_area / 9 * soil_depth / 3
    total_soil = circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil / 2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")

def calculate_fill(side_len: float, circle_area: float, fill_depth: float) -> None:
#Calculates the amount of fill material needed for the garden.
    fill_area = side_len ** 2 - circle_area * 3
    total_fill = fill_area / 9 * fill_depth / 3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")

def main() -> None:
#Entry point of the program.
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    
    circle = calculate_circle_area(side_len)
    calculate_plants(circle, plant_spacing)
    calculate_soil(circle, soil_depth)
    calculate_fill(side_len, circle, fill_depth)

main()