


side_len = float(input("Enter length of side of garden (feet): "))
plant_spacing = float(input("Enter spacing between plants (feet): "))
soil_depth = float(input("Enter depth of garden soil (feet): "))
fill_depth = float(input("Enter depth of fill (feet): "))

def circarea (side_len: float)->float:
    pi = 3.14
    circle_area = pi * (side_len/4)**2
    return circle_area

def totplants () -> None:
    circle_area = circarea (side_len)
    circle_plants = int(circle_area / plant_spacing ** 2)
    semi_plants = int(circle_area / 2 / plant_spacing ** 2)
    total_plants = circle_plants + semi_plants * 4
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)

def soil() -> None:
    circle_area = circarea (side_len)
    circle_soil = circle_area/9 * soil_depth/3
    total_soil = circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")

def totfill () -> None:
    circle_area = circarea (side_len)
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")

def main() -> None:
    circarea(side_len)
    totplants()
    soil()
    totfill()
    
main()