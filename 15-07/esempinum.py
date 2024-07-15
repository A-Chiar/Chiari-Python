import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
arr2d = np.array([[1,2,3],[4,5,6]])
print(arr2d)


print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.size)
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.argmax())

arr = np.array([1,2,3],dtype = 'int32')
print(arr.dtype)

arr =np.array([[1,2,3],[4,5,6]])
print(arr.shape)

arr = np.arange(10)
print(arr)

arr = np.arange(6)
reshaped_arr = arr.reshape((2,3))
print(reshaped_arr)

