#Write a password generator in Python. Be creative with how you
# generate passwords - strong passwords have a mix of lowercase
# letters, uppercase letters, numbers, and symbols. The passwords
#  should be random, generating a new password every time the user
#  asks for a new password. Include your run-time code in a main method.
#Extra:
#1. Ask the user how strong they want their password to be. For weak
# passwords, pick a word or two from a list.
 
import random
 
def gen_lower() :
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    x = random.randint(0,25)
    return lower[x]
 
def gen_upper() :
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    x = random.randint(0,25)
    return upper[x]
 
def gen_number() :
    return random.randint(0,9)
 
def gen_symbol() :
    symbol = ['!','@','#','$','%','^','&','*','-']
    x = random.randint(0,8)
    return symbol[x]
 
a = random.randint(8,15)
list = []
new = []
 
i=0
while i<a :
    list.append(random.randint(1,4))
    i+=1
 
i = 0
while i<len(list) :
    if list[i] == 1 :
        x = gen_lower()
        new.append(x)
    elif list[i] == 2 :
        x = gen_upper()
        new.append(x)
    elif list[i] == 3 :
        x = gen_number()
        new.append(x)
    else :
        x = gen_symbol()
        new.append(x)
    i+=1
 
print(a)
print(list)
print(new)
