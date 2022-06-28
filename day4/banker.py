# prick a person randomly who will pay the bill

import random

names_string = input("Give me everybody's name, seperated by commas: \n")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

# The above 3 lines can be replaced with the commented line below
#person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to pay for the meals today.")


