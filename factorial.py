number = int(input("enter the number:  "))

factorial = 1
if number < 0 :
    print("please enter a number positive:")

else:

    for i in range(1,number+1):
        factorial = factorial * i

print (f"the factorial of  number:   {factorial}")

