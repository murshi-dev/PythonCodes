import ingredientCost
#define a function to calculate ingredients quantity
def calculateSmoothieCost(baseQty,fruitQty,vegQty,proteinQty):
    baseCost=ingredientCost.calculateCost(baseQty,"base")
    fruitCost = ingredientCost.calculateCost(fruitQty, "fruit")
    vegeCost = ingredientCost.calculateCost(vegQty, "vege")
    proteinCost = ingredientCost.calculateCost(proteinQty, "protein")

    total_cost=baseCost+fruitCost+vegeCost+proteinCost
    return total_cost

#input the quantity of each ingredient
baseQty=float(input("Input the base quantity:  "))
fruitQty=float(input("Input the fruit quantity:  "))
vegeQty=float(input("Input the vege quantity:  "))
proteinQty=float(input("Input the protein quantity:  "))

#call the function to calculate the total cost
total_cost = calculateSmoothieCost(baseQty,fruitQty,vegeQty,proteinQty)
#print result
print("Total Cost of Cookie: ",total_cost)
