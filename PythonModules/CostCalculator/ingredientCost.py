'''You are tasked to build a python code for a bakery shop. The bakery owner needs a program to calculate the calculate the total cost of ingredients for a batch of cookies. Total cost is based on the flour quantity, sugar, butter, and chocolate chips.
The owner also runs a smoothie shop. A program is also required to calculate the cost of making different types of smoothies. Here the total cost is based on the base, fruits, vegetables, and the type of protein added to the smoothie.
Use modules and functions to develop the python code.
Hint:
o	Use a file bakery.py to get the inputs for the bakery shop ingredients
o	Use a file smoothie.py to get the inputs for the smoothie shop ingredients
o	Create a module ingredientCost.py to calculate the cost of the ingredients. Use this module in bakery.py and smoothie.py
'''
def calculateCost(quantity, ingredient):
    bakery_ingredient_price={#use dictionary to store prices
        "flour":2.00,
        "sugar":2.50,
        "butter":12.00,
        "chocChips":10.00
    }
    smoothie_ingredient_price={
        "base":5.00,
        "fruit":2.50,
        "vege":3.00,
        "protein":10.00
    }
     #calculate line total
    if ingredient in bakery_ingredient_price:
        cost_per_line=bakery_ingredient_price[ingredient]
        total_cost=quantity * cost_per_line
        return total_cost
    elif ingredient in smoothie_ingredient_price:
        cost_per_line=smoothie_ingredient_price[ingredient]
        total_cost=quantity * cost_per_line
        return total_cost
    else:
        return 0


