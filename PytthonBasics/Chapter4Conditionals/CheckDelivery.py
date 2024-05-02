# Define constants
local_area_code1 = "XYZ"
local_area_code2 = "ABC"
min_sale_amount = 300  # Minimum sale amount for free delivery

# Input sale amount and customer location
sale_amount = float(input("Enter the sale amount (RM): "))
customer_location = input("Enter the customer's local area code: ")

# Check if free delivery is applicable
if sale_amount >= min_sale_amount or customer_location == local_area_code1 or customer_location == local_area_code2:
    print("Free home delivery")
else:
    print("Delivery charges apply")
