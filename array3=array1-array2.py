'''
arrayيحذف كل الارقام يلي مشتركين بين تنان ل File  بدنا نعمل 

'''

array1 = [5,1,1,3,2,4,5,1,2]
array2 = [1,2]
array3 = [] 
for x in array1:
   if x not in array2:
        array3.append(x)
        
print(array3)

