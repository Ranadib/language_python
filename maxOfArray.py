#defin variable of length array
length = int(input("please enter the length of array"))

array1 = []

for i in range(length):
    array1.append(input())

max = array1[0]

for i in array1:
    if i > max:
        max = i

print(f"the maximum is:{max}")