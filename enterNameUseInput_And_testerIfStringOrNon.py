name = input("Please enter your name")

if name.isdigit():
    print("error please enter a values of type string") 
else:
    if len(name) < 3:
        print ("name must be more then 3 charactere!")
    elif len(name) > 50:
        print ("name must be lee then 50 character!")
    else:
        print ("this is good name")