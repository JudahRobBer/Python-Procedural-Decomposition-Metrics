

def main():
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    circle_area = area(side_len,plant_spacing)
    soil(side_len,circle_area,fill_depth,soil_depth)

def area(side_len,plant_spacing):
    pi = 3.14
    circle_area = pi * (side_len/4)**2
    circle_plants = plants(circle_area,plant_spacing)
    semi_plants = plants(circle_area/2,plant_spacing)
    total_plants = circle_plants + semi_plants * 4
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)
    return circle_area

def soil(side_len,circle_area,fill_depth,soil_depth):
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill(fill_area,fill_depth)
    circle_soil = fill(circle_area,soil_depth)
    total_soil = circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")

def plants(area,spacing):
    #Calculate how many plants can be planted in an area
    return int(area/spacing**2)

def fill(area,depth):
    #Calculate how much soil needs to be filled in an area
    return area*depth/27

main()
