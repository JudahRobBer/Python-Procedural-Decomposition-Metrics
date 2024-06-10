

#calculating the area of a circle
def area_of_circle(side: float) -> float:
    pi = 3.14
    circle_area = pi * (side/4)**2
    return circle_area

#calculating the number of plants needed for the garden
def plants_in_garden(side: float, space: float) -> None: 
    circle_area = area_of_circle(side)
    circle_plants = int(circle_area / space ** 2)
    semi_plants = int(circle_area / 2 / space ** 2) 
    total_plants = circle_plants + semi_plants * 4
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)

#calculating the area in the garden that needs to be filled
def garden_fill_area(side: float, depth: float) -> None:
    circle_area = area_of_circle(side)
    fill_area = side**2 - circle_area * 3
    total_fill = fill_area/9 * depth/3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")

#calculating the total soil needed for the garden
def total_soil_for_garden(side: float, depth: float) -> None: 
    circle_area = area_of_circle(side)
    circle_soil = circle_area/9 * depth/3
    total_soil = circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")

#asking for user input and helping to communicate it to the other functions in the code, also printing statments returned by other functions
def main() -> None:
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    print()
    plants_in_garden(side_len, plant_spacing)
    garden_fill_area(side_len, fill_depth)
    total_soil_for_garden(side_len, soil_depth)
    
main()