import numpy as np

arr = np.random.randint(10,50, size = 20)
print(arr)

primi_dieci = arr[0:11]
print(primi_dieci)

ultimi_cinque = arr[-5:-1] #da rivedere
print(ultimi_cinque)

daindice5_a15 = arr[5:15]
print(daindice5_a15)

#terzo_elemento = arr[:,2:3] #dà errore in quanto l'array è 1-dimensionale

#print(terzo_elemento)
terzo_elemento = arr[2:19:3]
print(terzo_elemento)

arr[5:10] = 99
print(arr)
