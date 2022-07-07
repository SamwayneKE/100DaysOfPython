# Solution 1

from numpy import number


total = 0

for num in range(2, 101, 2):
    total += num

print(total)


# Solution 2
total1 = 0

for number in range(1, 101):
    if number % 2 == 0:
        total1 += number

print(total1)        