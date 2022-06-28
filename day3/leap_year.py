# A program to check whether a year is a leap year or not.
#  Add an extra day after 4 years. Skip it if it's a new century.
# One day = 24hrs +- 0.005 secs

# Rule
    # Every year that is evenly divisible by 4, EXCEPT on every year that is evenly divisible by 100,Unless the year is also evenly divisible by 400.

year = int(input("Enter in the year to check\n")) 

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")  
    else:
        print("Leap year")  
else:
    print("Not Leap year")        
