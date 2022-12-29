#Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and makes
# a new list of only the first and last elements of
# the given list. For practice, write this code inside a function.
 
import random
 
list = random.sample(range(50), 5)
def pull(list) :
    return [list.pop(0),list.pop()]
print(pull(list))
