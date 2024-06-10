

#find circle area
def circlearea(side_len):
    pi = 3.14
    circle_area = pi * (side_len/4)**2
    return circle_area
#find and print plant in garden
def plant(circle_area, plant_spacing):
    circle_plants = int(circle_area / plant_spacing ** 2)
    semi_plants = int(circle_area / 2 / plant_spacing ** 2) 
    total_plants = circle_plants + semi_plants * 4
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)
#find and print total fill for garden    
def area(circle_area, side_len, fill_depth):
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")
#find and print soil in garden    
def soil(circle_area, soil_depth):
    circle_soil = circle_area/9 * soil_depth/3
    total_soil = circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")
#input function and get the result    
def main():
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    circle_area=circlearea(side_len)
    plant(circle_area, plant_spacing)
    area(circle_area, side_len, fill_depth)
    soil(circle_area, soil_depth)
#print the result    
main()
