#Ask the user for a number and determine whether the
# number is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.). You
# can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions
 
number = input("Enter a number: ")
num=int(number)
list=[]
 
def eval(num, list) :
    i=num-1
    while i>1 :
        if num%i==0 :
            list.append(i)
        i-=1
 
def test(list) :
    if len(list)==0 :
        print("This number is prime.")
    else :
        print("This number is not prime")
        print(list)
 
eval(num, list)
print(test(list))
