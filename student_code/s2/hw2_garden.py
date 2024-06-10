

def inputs():
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    return [side_len, plant_spacing, soil_depth, fill_depth]

def circle(side_len:float, plant_spacing:float):
    pi = 3.14
    circle_area = pi * (side_len/4)**2 
    circle_plants = int(circle_area / plant_spacing ** 2)
    semi_plants = int(circle_area / 2 / plant_spacing ** 2) 
    total_plants = circle_plants + semi_plants * 4
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)
    return [circle_area, circle_plants, semi_plants, total_plants]

def calculations(fill_depth:float, circle_area:float, side_len:float, soil_depth:float):
    circle_soil = circle_area/9 * soil_depth/3
    total_soil = circle_soil * 3
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    return [circle_soil, total_soil, total_fill]

    
def output(circle_soil:float, total_soil:float, total_fill:float):
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")


def main():
    x = inputs()
    y = circle(x[0], x[1])
    z = calculations(x[3], y[0], x[0], x[2])
    output(z[0], z[1], z[2])
#I returned the variables and made them into a list so that they would be able to utiziled much more efficiently 

main()