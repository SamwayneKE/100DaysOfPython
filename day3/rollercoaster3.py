print("Welcome to the rollercoaster!")
height = int(input("Enter your height in CM: \n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: \n"))

    if age < 12:
        bill = 5
        print("Children bills are $5.")

    elif age <= 18:
        bill = 7
        print("Teen bills are $7.")

    elif age >= 45 and age <= 55:
        print("Everything is Okay! You can have a free ride with us!")

    else:
        bill = 12
        print("Adults bill is $12.") 


    wants_photo = input("Do you want a photo taken? Y or N. \n")      
    if wants_photo == "Y":
        bill += 3
        print(f"You final bill is: ${bill}")
        
    else:
        print(f"You final bill is: ${bill}")

else:
    print("Sorry, you will have to grow taller before you can ride")        