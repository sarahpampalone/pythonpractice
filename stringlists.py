# Ask the user for a string and print out whether this string
# is a palindrome or not. (A palindrome is a string that reads
# the same forwards and backwards.)
 
word = input("Enter a word: ")
a = []
b = []
c = []
d = []
 
for letter in word :
    a.append(letter)
b = a
 
for letter in word :
    c.append(letter)
d = c
c.reverse()
 
#print(b)
#print(d)
 
if b==d :
    print("This is a palindrome.")
else :
    print("This is not a palindrome.")
