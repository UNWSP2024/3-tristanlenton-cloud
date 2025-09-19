itemWeight = float(input("What is your item weight? "))
if itemWeight <= 2:
    print("Shipping price:", itemWeight * 1.5)
elif itemWeight <= 6:
    print("Shipping price:", itemWeight * 3)
elif itemWeight <= 10:
    print("Shipping price:", itemWeight * 4)
else:
    print("Shipping price:", itemWeight * 4.75)