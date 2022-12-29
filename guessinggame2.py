import random
 
number = random.randint(0, 100)
attempt = 0
running = True
ans = None
 
while running:
    print ("Is it %s?" % str(number))
    ans = input()
   
    if "no" in ans.lower() and "lower" in ans.lower():
        number -= random.randint(1, 4)
    elif "no" in ans.lower() and "higher" in ans.lower():
        number += random.randint(1, 4)
    elif ans.lower() == "no":
        print ("Higher or lower?")
        ans = input()
        if ans.lower() == "higher":
            number += random.randint(1, 4)
        elif ans.lower() == "lower":
            number -= random.randint(1, 4)
    elif ans.lower() == "yes":
        if attempt < 2:
            print ("Yes! It only took me %s try!" % str(attempt))
        elif attempt < 2 and attempt < 10:
            print ("Pretty well for a robot, %s tries." % str(attempt))
        else:
            print ("That's so bad, %s tries." % str(attempt))
        running = False
    attempt += 1
   
print ("Thanks for the game!")
