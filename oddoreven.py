#Ask the user for a number.
#Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
 
#Extras
#1. If the number is a multiple of 4, print out a different message.
#2. Ask the user for two numbers: one number to check (call it num) and
# one number to divide by (check). If check divides evenly into num,
# tell that to the user. If not, print a different appropriate message.
 
number1 = input("Enter a number: ")
number2 = input("Enter a second number: ")
 
num = int(number1)
check = int(number2)
 
if num//check==0:
    print("The first number is divisible by the second.")
else :
    if num//2==0 :
        if num//4==0 :
            print("This number is divisible by 4.")
        else :
           print("This number is even.")
    else :
        print("This number is odd.")
