import numpy as np


arr = np.linspace(0,10,50)
print(arr)

arr1 = np.random.rand(50)
print(arr1)

sum = arr + arr1
print(sum)

sum1 = np.sum(sum)
print(sum1)

#sum1 = np.sum(sum> 5)
sum2 = 0
for i in sum:
    if i > 5:
        sum2 += i
print(sum2)