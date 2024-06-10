

# the function calculates the circle area and return
def circle_area(side_len: float) -> float:
    pi = 3.14
    circle_area = pi * (side_len/4)**2 
    return circle_area

# the function calculates how many plants are there for semicircle,
#circle, and the garden, respectively
def plant(circle_area: float, plant_spacing: float) -> None:
    print()
    semi_plants = int(circle_area / 2 / plant_spacing ** 2) 
    print("Plants for each semicircle garden: ", semi_plants)
    circle_plants = int(circle_area / plant_spacing ** 2)
    print("Plants for the circle garden: ", circle_plants)
    total_plants = circle_plants + semi_plants * 4
    print("Total plants for garden: ", total_plants)
    
# the function calculates how much soil for semicircle,
#circle, and the garden, respectively
def soil(circle_area: float, soil_depth: float) -> None:
    circle_soil = circle_area / 9 * soil_depth / 3
    total_soil = circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")

# the function calculates the total fill for the garden
def total_fill(circle_area: float, side_len: float, fill_depth: float) -> None:
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")
    
def main() -> None:
    #User's input
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    plant = (circle_area(side_len), plant_spacing)
    soil(circle_area(side_len), soil_depth)
    total_fill(circle_area(side_len), side_len, fill_depth)
    
# function call
main()