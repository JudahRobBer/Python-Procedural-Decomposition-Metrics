

# plant function uses values tranfered from main in order to calculate the required values for the user
def plants(plant_spacing:int, area_circle:int) -> None:
    circle_plants = int(area_circle / plant_spacing ** 2)
    semi_plants = int(area_circle / 2 / plant_spacing ** 2) 
    total_plants = circle_plants + semi_plants * 4
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)
    return None
    

# fill function uses values tranfered from main in order to calculate the required values for the user
def fill(side_len:int, fill_depth:int, area_circle:int) -> None:
    fill_area = side_len**2 - area_circle * 3
    total_fill = fill_area/9 * fill_depth/3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")
    return None
    
# soil function uses values tranfered from main in order to calculate the required values for the user   
def soil(area_circle:int, soil_depth:int) -> None:
    circle_soil = area_circle/9 * soil_depth/3
    total_soil = circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")
    return None
    
# defined area of circle in seperate function
def circle(side_len:int) -> int:
    pi = 3.14
    circle_area = pi * (side_len/4)**2
    return circle_area
    

# I put the user inputs in the main function and defined the circle_area inside it aswell, in order to transfer the values recieved from the inputs and circle_are into the plants, fill, and soil function.
def main() -> None:
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    area_circle = circle(side_len)
    plants(plant_spacing, area_circle)
    soil(area_circle, soil_depth)
    fill(side_len, fill_depth, area_circle)
    
main()