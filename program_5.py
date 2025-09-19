hotdog = input("Would you like a regular hot dog or a chili dog? ")
if hotdog == "chili dog":
    priceOfDog = 4.5
else:
    priceOfDog = 3.5
topping = input("Would you like any topping? ")
if topping == "yes":
    topping = input("Which topping would you like? We have cheese, peppers, or grilled onions: ")
    if topping == "cheese":
        priceOfTopping = 0.5
    elif topping == "peppers":
        priceOfTopping = 0.75
    elif topping == "grilled onions":
        priceOfTopping = 1
    else :
        priceOfTopping = 0
else:
    priceOfTopping = 0
print("Hot dog cost: $", priceOfDog)
print("Tax: $", (priceOfDog + priceOfTopping)*.07)
print("Total price: $", (priceOfDog + priceOfTopping)*1.07)
