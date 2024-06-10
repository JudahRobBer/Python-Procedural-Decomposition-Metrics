

# Function to calculate the circle area in the garden
def circle(side_len:float)->float:
    # Define the value of pi
    pi = 3.14
    # Calculate the area of the circle in the garden
    circle_area = pi * (side_len/4)**2
    # return the circle area back to the main function (this is critical)
    return circle_area

# Function to calculate the number of plants needed for the garden
def plants(circle_area:float,plant_spacing:float)->None:
    # Calculate the number of plants for the circular area
    circle_plants = int(circle_area / plant_spacing ** 2)
    # Calculate the number of plants for each semicircular area
    semi_plants = int(circle_area / 2 / plant_spacing ** 2)
    # Calculate the total number of plants for the entire garden
    total_plants = circle_plants + semi_plants * 4
    # Print information about the number of plants
    print()
    print("Plants for each semicircle garden:", semi_plants)
    print("Plants for the circle garden:", circle_plants)
    print("Total plants for garden:", total_plants)

# Function to calculate the amount of soil needed for the garden
def soil(circle_area:float,soil_depth:float)->None:
    # Calculate the amount of soil needed for the circular area
    circle_soil = circle_area/9 * soil_depth/3
    # Calculate the total amount of soil needed for the entire garden
    total_soil = circle_soil * 3
    # Print information about the amount of soil needed
    print("Soil for each semicircle garden:", round(circle_soil/2, 1), "cubic yards")
    print("Soil for the circle garden:", round(circle_soil, 1), "cubic yards")
    print("Total soil for the garden:", round(total_soil, 1), "cubic yards")

# Function to calculate the amount of fill needed for the garden
def fill(side_len:float,circle_area:float,fill_depth:float)->None:
    # Calculate the area of the fill in the garden
    fill_area = side_len**2 - circle_area * 3
    # Calculate the total amount of fill needed for the entire garden
    total_fill = fill_area/9 * fill_depth/3
    # Print information about the amount of fill needed
    print("Total fill for the garden:", round(total_fill, 1), "cubic yards")

# Main function to execute the program
def main()->None:
    # Inputs for garden parameters
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    # Call the circle function to calculate circle related details
    circle_area=circle(side_len)
    # Call the plants function to calculate plant-related details
    plants(circle_area,plant_spacing)
    # Call the soil function to calculate soil-related details
    soil(circle_area,soil_depth)
    # Call the fill function to calculate fill-related details
    fill(side_len,circle_area,fill_depth)

# Call the main function to start the program
main()