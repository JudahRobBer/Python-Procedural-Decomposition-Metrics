

def body (side_len:float, plant_spacing:float)-> int: #The function body takes on two parameters: length and spacing. These are both class type float and the function will return an integer.
    pi = 3.14 
    circle_area= pi * (side_len/4)**2
    circle_plants= int(circle_area/ plant_spacing ** 2)
    semi_plants= int(circle_area/ 2 / plant_spacing ** 2)
    total_plants= circle_plants+ semi_plants * 4 
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)
    return circle_area #Return the area of the circular garden as a integer

def body_2 (side_len:float, circle_area:float, fill_depth:float)-> None: #Function to calculate the fill needed for the garden
    fill_area= side_len**2 - circle_area * 3
    total_fill= fill_area/9 * fill_depth/3
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards") #Round function rounds value to one decimal place

def body_3 (circle_area:float, soil_depth:float)-> None: #Function to calculate the soil needed for the garden
    circle_soil= circle_area/9 * soil_depth/3
    total_soil= circle_soil * 3
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1),"cubic yards")

def main ( )-> None: #Define a main function to call the other functions
    side_len= float(input("Enter length of side of garden (feet): ")) #Define variable names and convert string inputs to floats
    plant_spacing= float(input ("Enter spacing between plants (feet): ")) #User inputs values
    soil_depth= float(input("Enter depth of garden soil (feet): "))
    fill_depth= float(input ("Enter depth of fill (feet): "))
    circle_area= body(side_len,plant_spacing)
    body_3(circle_area,soil_depth) #Call previous function to calculate soil needed given inputs
    body_2(side_len,circle_area,fill_depth) #Call previous function to calculate fill required given inputs
    
main()

