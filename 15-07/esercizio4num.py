import numpy as np
arr = np.linspace(0,1,12)
print(arr)

"""arr1 = np.random.rand(3,4)
print(arr1)
"""
arr1 = arr.reshape(3,4)
print(arr1)

sum = np.sum(arr)
print(sum)

sum1 = np.sum(arr1)
print(sum)