#Create a program that will play the “cows and bulls”
# game with the user. The game works like this:
#Randomly generate a 4-digit number. Ask the user to guess
# a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a “cow”. For
# every digit the user guessed correctly in the wrong place
#  is a “bull.” Every time the user makes a guess, tell them
#  how many “cows” and “bulls” they have. Once the user guesses
#  the correct number, the game is over. Keep track of the number
#  of guesses the user makes throughout teh game and tell the user at the end.
 
import random
 
def reset(guess) :
    guess = []
    return guess
 
a = random.sample(range(9),4)
num=[]
for val in a :
    num.append(str(val))
guess = []
count = 0
print(num)
 
while guess!=a and guess!="exit" :
    guess.clear()
    a = input("Enter a guess: ")
    for val in a :
        guess.append(val)
 
    cow = 0
    bull = 0
 
    if guess=="exit" :
        break
    count+=1
 
    i=0
    while i<4 :
        if num[i]==guess[i] :
            cow+=1
        else :
            bull+=1
        i+=1
   
    if cow==4 :
        print("Correct! You took %s guesses." %count)
        break
    else :
        print("%s cows and %s bulls" %(cow, bull))
