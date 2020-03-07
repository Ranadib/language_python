import random

rand = random.randint(0,50)
num = -1
while rand != num:
    num = int(input ("please enter a number"))
    if num < rand:
        print ("your number is younger than random")
    elif num > rand:
        print ("your number is larger than random")
    else:
        print ("your number equal the rondom")