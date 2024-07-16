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

arr = np.array([1,2,3,4,5])

#indexing
print(arr[0])

#slicing
print(arr[1:3])

#boolean indexing
print(arr[arr>2])

arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#slicing sulle righe
print(arr_2d[1:3])

#slicing sulle colonne
print(arr_2d[:,1:3])

#slicing misto
print(arr_2d[1:, 1:3])

arr = np.array([0,1,2,3,4,5,6,7,8,9])
#slicing di base
print(arr[2:7])

#slicing con passo
print(arr[1:8:2])

#omettere start e stop
print(arr[:5])
print(arr[5:])

#utilizzare indici negativi
print(arr[-5])
print(arr)

#FANCY INDEXING
arr = np.array([10,20,30,40,50])

#utilizzo di un array di indici
indices = np.array([1,3])
print(arr[indices])

#utilizzo di una lista di indici
indices =[0,2,4]
print(arr[indices])

#SLICING limitato a selezioni rettangolari
#restituisce una vista dell'array originale (non si crea una copia)
#utilizza indici di inizio, fine e passo

#FANCY INDEXING 
#può selezionare elementi non contigui e in ordine arbitrario
#crea sempre una copia dei dati selezionati
#utilizza array di indici interi

#linspace
arr =np.linspace(0,1,5)
print(arr)

#random
random_arr = np.random.rand(3,3)
print(random_arr)

#sum mean std

arr = np.array([1,2,3,4,5])
sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print(sum_value)
print(mean_value)
print(std_value)