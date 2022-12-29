#Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains
# only the elements that are common between the lists
# (without duplicates). Make sure your program works on
# two lists of different sizes. Write this in one line of
# Python using at least one list comprehension.
#Extra:
#1. Randomly generate two lists to test this
 
import random
 
c = random.sample(range(100), random.randint(1,10))
d = random.sample(range(100), random.randint(1,10))
e = set(c).intersection(set(d))
 
print(e)
