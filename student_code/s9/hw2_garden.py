

def semi_plant(a,b)-> None:
    semi_plants = int(a / 2 / b ** 2) 
    return semi_plants
#to get semicircle plant

def total_plant(c,d)->None:
    total_plants=c+d*4
    return total_plants
#to get total plants

def total_fill(e,f,g)->None:
    fill_area=e**2-f*3
    total_fill_a=fill_area/9*g/3
    return total_fill_a
#to get totcal fill of the garden

def circle_soil(h,i)->None:
    circle_soils=h/9*i/3
    return round(circle_soils,1)
#to get the area of soil for the circle

def semi_soil(h,i)->None:
    return round(circle_soil(h,i)/2,1)
#to get the area of soil for the semicircle

def total_soil(j)->None:
    return round(j*3,1)
#to get the total soil area

def main():
    pi = 3.14
    side_len = float(input("Enter length of side of garden (feet): "))
    plant_spacing = float(input("Enter spacing between plants (feet): "))
    soil_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))
    #getting all the input for the user
    
    print()
    circle_area = pi * (side_len/4)**2 
    circle_plants = int(circle_area / plant_spacing ** 2)
    s=semi_plant(circle_area,plant_spacing)
    #to let the semicircle plant reused
    
    print("Plants for each semicircle garden:  ",s)
    print("Plants for the circle garden: ",circle_plants)
    print("Total plants for garden:  ",total_plant(circle_plants,s))
    print("Soil for each semicircle garden: ",semi_soil(circle_area,soil_depth),"cubic yards")
    c=circle_soil(circle_area,soil_depth)
    print("Soil for the circle garden: ",c,"cubic yards")
    print("Total soil for the garden:  ",total_soil(c),"cubit yards")
    print("Total fill for the garden: ",round(total_fill(side_len,circle_area,fill_depth),1),"cubic yards")
    #calling the previous function
    
main()
#main function