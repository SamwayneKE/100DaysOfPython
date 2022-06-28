print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
names_in_lowercase = combined_names.lower()

t = names_in_lowercase.count("t")
r = names_in_lowercase.count("r")
u = names_in_lowercase.count("u")
e = names_in_lowercase.count("e")
true = t + r + u + e

l = names_in_lowercase.count("l")
o = names_in_lowercase.count("o")
v = names_in_lowercase.count("v")
e = names_in_lowercase.count("e")
love = l + o + v + e


love_score = int(str(true) + str(love))
print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos!")

elif (love_score >= 40) and (love_score<= 50):
    print(f"Your love score is {love_score}, you are alright together!")

else:
    print(f"Your love score is {love_score}")



