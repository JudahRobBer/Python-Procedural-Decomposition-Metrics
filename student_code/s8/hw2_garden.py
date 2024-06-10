

#All the calculations given that take inputs and outputs when needed
def questions():
    sideLen = float(input("Enter length of side of garden (feet): "))
    plantSpacing = float(input("Enter spacing between plants (feet): "))
    soilDepth = float(input("Enter depth of garden soil (feet): "))
    fillDepth = float(input("Enter depth of fill (feet): "))
    return sideLen, plantSpacing, soilDepth, fillDepth

def calculateCircleArea(sideLen):
    return 3.14 * (sideLen / 4) ** 2

def calculatePlants(circleArea, plantSpacing):
    circlePlants = int(circleArea / plantSpacing ** 2)
    semiPlants = int(circleArea / 2 / plantSpacing ** 2)
    totalPlants = circlePlants + semiPlants * 4
    return semiPlants, circlePlants, totalPlants

def calculateFill(sideLen, circleArea, fillDepth):
    fillArea = sideLen ** 2 - circleArea * 3
    totalFill = fillArea / 9 * fillDepth / 3
    return round(totalFill, 1)

def calculateSoil(circleArea, soilDepth):
    circleSoil = circleArea / 9 * soilDepth / 3
    totalSoil = circleSoil * 3
    return round(circleSoil / 2, 1), round(circleSoil, 1), round(totalSoil, 1)
    
def main():
#calling the questions and setting them equal to the corresponding variable
    sideLen, plantSpacing, soilDepth, fillDepth = questions()
#calling all the variables with the correct input
    circleArea = calculateCircleArea(sideLen)
    semiPlants, circlePlants, totalPlants = calculatePlants(circleArea, plantSpacing)
    totalFill = calculateFill(sideLen, circleArea, fillDepth)
    semiSoil, circleSoil, totalSoil = calculateSoil(circleArea, soilDepth)
#printing everything
    print("Plants for each semicircle garden:", semiPlants)
    print("Plants for the circle garden:", circlePlants)
    print("Total plants for garden:", totalPlants)
    print("Soil for each semicircle garden:", semiSoil, "cubic yards")
    print("Soil for the circle garden:", circleSoil, "cubic yards")
    print("Total soil for the garden:", totalSoil, "cubic yards")
    print("Total fill for the garden:", totalFill, "cubic yards")

    
main()