#Write a program (function!) that takes a list and returns a new
# list that contains all the elements of the first list minus all the duplicates.
 
#Extras:
#1. Write two different functions to do this - one using a loop
# and constructing a list, and another using sets.
#2. Go back and do Exercise 5 using sets, and write the solution
# for that in a different function.
 
def setfunc(list) :
    return set(list)
 
def loopfunc(list) :
    b = []
    [b.append(x) for x in list if x not in b]
    return b
 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
print(setfunc(a))
print(loopfunc(a))
