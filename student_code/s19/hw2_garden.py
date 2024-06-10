

#area of the circle
def circle_area_ (four_radius:float) -> float:
    pi = 3.14
    circle_area = pi * (four_radius/4)**2
    return circle_area

#number of plants in one circle
def circle_plants_ (one_circle_area:float, space_between:float, four_radius:float) -> float:
    circle_plants = int(circle_area_(four_radius) / space_between ** 2)
    return circle_plants

#number of plants in one semicircle
def semi_plants_ (one_circle_area:float, space_between:float) -> float:
    semi_plants = int(one_circle_area / 2 / space_between ** 2)
    return semi_plants
    
#total fill for the garden
def total_fill_  (four_radius,area_of_circle, depth) -> float:
    fill_area = four_radius**2 - area_of_circle * 3
    total_fill = fill_area/9 * depth/3
    return total_fill

#total soil for the circle garden
def circle_soil_ (one_circle_area:float, depth:float) -> float:
    circle_soil = one_circle_area/9 * depth/3
    return circle_soil

def main () -> None:
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    print ()
    
    circle_area = circle_area_(side_len)
    
    semi_plants = semi_plants_ (circle_area, plant_spacing)
    print("Plants for each semicircle garden:", semi_plants)
    
    plants_for_circle = circle_plants_ (circle_area, plant_spacing, side_len)
    print("Plants for the circle garden:", plants_for_circle)
    
    #total number of plants
    total_plants = semi_plants * 4 + plants_for_circle
    print("Total plants for garden:", total_plants)
    
    circle_soil = circle_soil_(circle_area, soil_depth)
    #soil for each semicircle garden
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    #soil for the circle garden
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    
    total_soil = circle_soil * 3
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")
    
    total_fill = total_fill_(side_len,circle_area,fill_depth)
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")

main ()



