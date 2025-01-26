food_bill =int(input("Enter a bill amount:"))
tip_percentage = int(input("Enter percentage of tip:"))

tip = (tip_percentage/100) * food_bill

print("Therefore tip amount to is: ", round(tip))

print("Total bill at the end is:", tip + food_bill,"Rupees")
          