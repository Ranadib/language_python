'''Write a method generateArray that takes as parameter an integer representing the size of an array. The
method creates the array, fills it with random integers between 1 and 20 inclusive and returns it.
b) Write a method countEven that returns the number of even numbers in an array of integers
c) Write a method move (int[] values, int[] evenValues, int[] oddValues) that moves the even elements as
well as the odd ones from the array values into the evenValues and oddValues arrays respectively.
d) Test the above methods as per the below sample run.
Sample Run:
Enter the size of the array: 10
The generated array is: 9 20 11 10 13 18 6 7 15 19
The array contains 4 even numbers
The array evenValues: 20 10 18 6
The array oddValues: 9 11 13 7 15 19'''


#defin variable 
length_array = int(input("Enter the size of the array"))
number = input("the generated array is:")
array1 = number.split(" ")

even = 0
c = 0 
array2 = []
array3 = []
for i in array1:
    #search value of even
    if int(i)%2==0:
        array2.append(i)
        even = even + 1
    else:
        #search value of odd
        array3.append(i)
       
   
print(f"the array contains {even} numbers")
print(f"the array evenValues:{array2}")
print(f"the array oddValues:{array3}") 