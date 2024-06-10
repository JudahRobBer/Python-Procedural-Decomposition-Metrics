

#All the calculations given that take inputs and output neccesary outputs, prerounding for fill and soil
def calculateCircleArea(sideLen: float) -> float:
    return 3.14 * (sideLen / 4) ** 2

def calculatePlants(area: float, plantSpacing: float) -> int:
    return int(area / plantSpacing ** 2)

def calculateFill(fillArea: float, fillDepth: float) -> float:
    totalFill = fillArea / 9 * fillDepth / 3
    return round(totalFill, 1)


def calculateSoil(soilArea: float, soilDepth: float) -> float:
    return round(soilArea / 9 * soilDepth / 3, 1)

def main() -> None:
    sideLen = float(input("Enter length of side of garden (feet): "))
    plantSpacing = float(input("Enter spacing between plants (feet): "))
    soilDepth = float(input("Enter depth of garden soil (feet): "))
    fillDepth = float(input("Enter depth of fill (feet): "))

#Calculate Areas
    circleArea = calculateCircleArea(sideLen)
    semiCircleArea = circleArea / 2
    totalGardenArea = sideLen ** 2
    fillArea = totalGardenArea - 3 * circleArea

#Calculate Plants
    circlePlants = calculatePlants(circleArea, plantSpacing)
    semiCirclePlants = calculatePlants(semiCircleArea, plantSpacing)
    totalPlants = circlePlants + semiCirclePlants * 4

#Calculate Fill and Soil
    totalFill = calculateFill(fillArea, fillDepth)
    semiCircleSoil = calculateSoil(semiCircleArea, soilDepth)
    circleSoil = calculateSoil(circleArea, soilDepth)
    totalSoil = semiCircleSoil * 2 + circleSoil

#Print Everything
    print("Plants for each semicircle garden:", semiCirclePlants)
    print("Plants for the circle garden:", circlePlants)
    print("Total plants for garden:", totalPlants)
    print("Soil for each semicircle garden:", round(semiCircleSoil, 1), "cubic yards")
    print("Soil for the circle garden:", round(circleSoil, 1), "cubic yards")
    print("Total soil for the garden:", round(totalSoil, 1), "cubic yards")
    print("Total fill for the garden:", totalFill, "cubic yards")

main()