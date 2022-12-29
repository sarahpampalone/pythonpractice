#Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and
# ask if the players want to start a new game)
 
#Remember the rules:
#Rock beats scissors
#Scissors beats paper
#Paper beats rock
 
import sys
 
user1 = input("What is player one's name? ")
user2 = input("What is player two's name? ")
user1_pick = input("%s, what is your choice (in lowers)? " %user1)
user2_pick = input("%s, what is your choice (in lowers)? " %user2)
 
def compare(u1,u2) :
    if u1==u2 :
        return("It's a tie!")
    if u1=="rock" :
        if u2=="paper" :
            return("Paper wins!")
        else :
            return("Rock wins!")
    elif u1=="paper" :
        if u2=="scissors" :
            return("Scissors wins!")
        else :
            return("Paper wins!")
    elif u1=="scissors" :
        if u2=="rock" :
            return("Rock wins!")
        else :
            return("Scissors wins!")
    else :
        return("Invalid input! Try again.")
        sys.exit()
 
print(compare(user1_pick, user2_pick))
