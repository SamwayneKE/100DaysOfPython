#Remember to use the random module
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
    