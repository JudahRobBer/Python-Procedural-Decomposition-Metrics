


def plants(circle_area:float,plant_spacing:float)->None:
    #Plants for each semicircle garden
    semi_plants = int(circle_area / 2 / plant_spacing ** 2)
    print("Plants for each semicircle garden: ",semi_plants)
    #Plants for the circle garden
    circle_plants = int(circle_area / plant_spacing ** 2)
    print('Plants for the circle garden: ',circle_plants)
    #Total plants for garden
    total_plants = circle_plants + semi_plants * 4
    print('Total plants for garden: ',total_plants)
    
def soil(circle_area:float,soil_depth:float)->None:
    circle_soil = circle_area/9 * soil_depth/3
    #Soil for each semicircle garden
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    #Soil for the circle garden
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    #Total soil for the garden
    total_soil = circle_soil * 3
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")

def fill(side_len:float,circle_area:float,fill_depth:float)->None:
    fill_area = side_len**2 - circle_area * 3
    total_fill = fill_area/9 * fill_depth/3
    #total fill
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")


def main()->None:
    #input value
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    #circle area
    pi = 3.14
    circle_area = pi * (side_len/4)**2
    plants(circle_area,plant_spacing)
    #circle soil
    soil(circle_area,soil_depth)
    #total fill
    fill(side_len,circle_area,fill_depth)
    
    
main()
