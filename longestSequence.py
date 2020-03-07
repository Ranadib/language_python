'''Problem #4
a) Write a method longestSequence that takes a single-dimensional array of integers as parameter and
returns the maximum length of uninterrupted series of strictly positive integers in the array.
For example: let 8, 6, 7, 8, 9, 2, 1, 2, 3, and 5 be the elements of the array. There is two uninterrupted
series (6, 7, 8, 9) and (1, 2, 3). So the method returns 4 which is the number of digits in the longest series.
b) Write a test program that creates and fills an array of size 10 with random digits. The program displays
the array as well as the length of the longest uninterrupted series of integers.
Sample Run:
The generated array is: 8 6 7 8 9 2 1 2 3 5
The size of the longest uninterrupted series is: 4'''


def longestSequence(array):
    vale_after_v = 0
    count_before = 0
    count_after = 0
    for v in array:
        if int(v) > int(vale_after_v):
            vale_after_v = v
            count_before = count_before + 1
          
        else:   
            if count_after < count_before:
                count_after = count_before
                count_before = 0
        
      
    print(f"The size of the longest uninterrupted series is: {count_after}") 
   

length = int(input("please enter the length of array"))

array = []

for i in range(length):
    array.append(input())

longestSequence(array)


