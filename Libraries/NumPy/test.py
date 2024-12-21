import numpy as np 

# array1 = np.array([1,2,3,4,5])
# array2 = np.array([6,7,8,9,10])

# result = array1+array2
# result1 = array1 - array2
# result2 = array1 * array2
# result3 = array1 / array2
# print(result)
# print(result1)
# print(result2)
# print(result3)

# #sum 
# np.sum(array1)
# print(array1)

# max and min 
# max = np.max(array1)
# min = np.min(array1)
# print(max)
# print(min)

#Multi dimensional arrays

# 2-D arrays are arrays that have 1-D arrays as it's elements
# array_1 = np.array([[1,2,3],[4,5,6]])
# print(array_1.size,len(array_1))
# print(array_1.shape,array_1.dtype,array_1.ndim)

# # 3-D arrays are arrays that have 2-D arrays as it's elements
# array_2 = np.array([ [[1,2,3],[4,5,6]] , [[1,2,3],[4,5,6]] , [[1,2,3],[4,5,6]] ])
# print(array_2.size,len(array_2))
# print(array_2.shape,array_2.dtype,array_2.ndim)

#shape - Describes the dimensions of a NumPy array. It returns a tuple representing the size of the array in each dimension
#dtype - This specifies the data type of the elements stored in the NumPy array, such as int32, float64 or bool.
#size - Returns the total number of elements in the array.
#ndim - Indicates the number of dimensions in the array.

# array_1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print('2nd element on 1st row is',array_1[0,1])

#create a 2D numpy array which has dymension 4*5 which contains the numbers 1 to 20.
# porform the following on this array add 10 to every element.
#multiply every element by 2
#calculate the square of each element

# array_1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])

# array_2 = array_1+10
# print(array_2)
# array_3 = array_1*2
# print(array_3)
# array_4 = array_1**2
# print(array_4)

#Boolean indexing in NumPy

# arr = np.array([10,20,30,40,50])
# condition = arr>25
# print(condition,type(condition))
# filtered = arr[condition]
# print(filtered)
# filtered_array = arr[arr>25]
# print(filtered_array)
# filtered_combined = arr[(arr>20) & (arr<50)]
# print(filtered_combined)


#Functions in NumPy arrays



#np.zeros() - used to initialize arrays with 0 as it's elements.

# array_1 = np.zeros(5)
# print(array_1)
# array_2 = np.zeros((2,3),dtype=float)         #sets as float as standard
# print(array_2)

#np.full() - used to return a new array of given shape and type, filled with fill_value.

# array_1 = np.full(4,7)
# print(array_1)
# array_2 = np.full((2,3),8)
# print(array_2)

#np.empty() - Return a new array of given shape and type, without initializing entries. Array will contain arbitrary values(uninitialized garbage values)
# This will give performance and flexibility

# array_1 = np.empty((2,3))
# print(array_1)

#1.Create a 1-D numpy array with values from 1-20. Use boolean indexing to extract all even numbers.
#2.Create a 1-D numpy array with elements 10,20,30,40,50. Use boolean indexing to extract all elements greater than the mean of the array

# array_1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# even_array = array_1[array_1%2==0]
# print(even_array)

# array_2  = np.array([10,20,30,40,50])
# greater_mean = array_2[np.mean(array_2)<array_2]
# print(greater_mean)


