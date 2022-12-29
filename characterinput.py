#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Note: for this exercise, the expectation is that you explicitly write out the year
# (and therefore be out of date the next year)
 
name = input("What is your name? ")
age = input("How old are you? ")
 
year = 2022 + (100-int(age))
 
print("Your name is " + name + " and you are " + age + " years old.")
print("You will turn 100 years old in " + str(year))
