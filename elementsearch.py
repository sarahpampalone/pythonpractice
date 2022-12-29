#Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest)
# and another number. The function decides whether or not the given
#  number is inside the list and returns (then prints) an appropriate boolean.
#Extras:
#1. Use binary search
 
def find(a,b) :
    for el in a :
        if el == b :
            return True
            break
 
a = [1,2,3,4,5,6,7,8,9,12]
b = 11
 
x = find(a,b)
 
if x==True :
    print("This value is in the list")
else :
    print("This value is not in the list")
