age = int(input("Enter age: "))
if age <= 1:
    print("He or she is an infant")
elif age > 1 and age < 13:
    print("He or she is a child")
elif age >= 13 and age < 20:
    print("He or she is a teenager")
else:
    print("He or she is an adult")
