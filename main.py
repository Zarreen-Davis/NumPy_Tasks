#1 dimensional array from 0-9
import numpy as np

array = np.array([0,1,2,3,4,5,6,7,8,9])

print(array)

print("\n")

#Create a 3×3 NumPy array of all True’s
import numpy as np

a = np.arange(1, 10).reshape(3, 3)

print(a)

print("\n")

#Extract all odd numbers from array of 1-10
import numpy as np 

array=np.array([1,2,3,4,5,6,7,8,9,10])

print(array[array % 2 == 1])

print("\n")

#Subtract 1 from each of the numbers in the above array
import numpy as np 

array = np.array([1,2,3,4,5,6,7,8,9,10])

array1 = [x - 1 for x in array]

print(array1)

print("\n")

#Convert a 1D array to a 2D array with 2 rows
import numpy as np 

#1D array
array1 = np.array ([1,2,3,4,5,6,7,8,9,10])
print(array1)

#2D array
array2 = np.array ([[1,2,3,4,5], [6,7,8,9,10]])
print(array2)

print("\n")

#Create two arrays a and b, stack these two arrays vertically use the np.dot and np.sum to calculate totals
import numpy as np 

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)
c = np.vstack((a,b))
print (c)

#np.dot
d = np.dot(a, b)
print(d)

#np.sum
sum = np.sum(d)
print(sum)

sum1 = np.sum(a)