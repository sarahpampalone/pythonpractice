#Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right. (Hint: remember to
# use the user input lessons from the very first exercise)
 
#Extras:
#1. Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when
# the game ends, print this out.
 
import random
a = random.randint(1,9)
guess = 0
count = 0
 
while guess!=a and guess!="exit" :
    guess = input("Enter a guess between 1 and 9: ")
 
    if guess=="exit" :
        break
    guess = int(guess)
    count+=1
 
    if guess<a :
        print("Your guess is too low.")
    elif guess>a :
        print("Your guess is too high.")
    else :
        print("Correct!")
        print("You took %s tries!" %count)
 
input()
