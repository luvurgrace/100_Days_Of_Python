print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"Please pay {bill} dollars.")
    elif age <= 18:
        bill = 7
        print(f"Please pay {bill} dollars.")
    else:
        bill = 12
        print(f"Please pay {bill} dollars.")
    photo_desire = input("Do you want to have a photo take? Type \"y\" if Yes and \"n\" if No.")
    if photo_desire == "y":
        bill += 3
    print(f"Your final bill is {bill} dollars.")
else:
    print("Sorry you have to grow taller before you can ride.")
