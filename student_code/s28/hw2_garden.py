
    
    
def one(n: float, y: float, z: float) -> None:
    circle_plants = int(z / y ** 2)
    semi_plants = int(z / 2 / y ** 2)
    total_plants = circle_plants + semi_plants * 4
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)
    
def two(n: float, y: float, z: float) -> None:    
    fill_area = n**2 - z* 3
    total_fill = fill_area/9 * y/3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")
   
def three(n: float, y: float) -> None:   
    circle_soil = y/9 * n/3
    total_soil = circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")


def main():
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    
    pi= 3.14
    circle_area = float(pi * (side_len/4)**2)
    
    one(side_len, plant_spacing, circle_area)
    three(soil_depth, circle_area)
    two(side_len, fill_depth, circle_area)

main()