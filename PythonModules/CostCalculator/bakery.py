import ingredientCost
#define a function to calculate ingredients quantity
def calculateCookieCost(flourQty,sugarQty,butterQty,chipsQty):
    flourCost=ingredientCost.calculateCost(flourQty,"flour")
    sugarCost = ingredientCost.calculateCost(sugarQty, "sugar")
    butterCost = ingredientCost.calculateCost(butterQty, "butter")
    chipsCost = ingredientCost.calculateCost(chipsQty, "chocChips")

    total_cost=flourCost+sugarCost+butterCost+chipsCost
    return total_cost

#input the quantity of each ingredient
flourQty=float(input("Input the flour quantity:  "))
sugarQty=float(input("Input the sugar quantity:  "))
butterQty=float(input("Input the butter quantity:  "))
chipsQty=float(input("Input the choc chips quantity:  "))

#call the function to calculate the total cost
total_cost = calculateCookieCost(flourQty,sugarQty,butterQty,chipsQty)
#print result
print("Total Cost of Cookie: ",total_cost)
