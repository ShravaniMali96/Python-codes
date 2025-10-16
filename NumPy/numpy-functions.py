import numpy as np

#1
arr1 = np.arange(0, 10, 2)
print("Arange:", arr1)

#2
zeros_array = np.zeros((2, 3))
print("Zeros Array:\n", zeros_array)

#3
ones_array = np.ones((3, 2))
print("Ones Array:\n", ones_array)

#4
arr2 = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:", arr2)
reshaped = arr2.reshape(2, 3)
print("Reshaped:\n", reshaped)

#5
arr3 = np.array([10, 20, 30])
print("Sum:", np.sum(arr3))
#6
print("Mean:", np.mean(arr3))

#7
arr4 = np.array([4, 9, 2, 7])
print("Max:", np.max(arr4))
#8
print("Min:", np.min(arr4))

#9
arr5 = np.array([1, 2, 3, 4, 5])
squared = np.square(arr5)
print("Squared:", squared)

#10
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Dot Product:\n", np.dot(a, b))

#11
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
combined = np.concatenate((a, b))
print("Concatenated:", combined)

#12
arr7 = np.array([[1, 2, 3], [4, 5, 6]])
transposed = np.transpose(arr7)
print("Transposed:\n", transposed)
