print("Welcome to the Rollercoaster!")
height = int(input("What is your height in CM?\n"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller to ride the Rollercoaster!")    
    