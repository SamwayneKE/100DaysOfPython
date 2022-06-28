print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Child ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Teen ticketis $7.")
    else:
        bill = 12
        print("Adult ticket is $12") 

    wants_photo = input("Do you want a photo taken? Y or N \n") 
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}")              
else:
    print("Sorry, you will have to grow taller to ride the rollercoaster!")
