import numpy as np
scelta = input("""Buongiornissimo, cosa vuoi fare?
            1. generare array di 12 gatti
            2. cambiare la forma dell'array
            3. sommare i gatti
            """)

def genera_array():
    arr = np.linspace(0,1,12)
    print(arr)
    return arr

def cambiare_forma(arr):
    arr1 = np.random.rand(3,4)
    print(arr1)
    return arr1

def somma(arr,arr1):
    sum = np.sum(arr)
    print(sum)
    sum1 = np.sum(arr1)
    print(sum1)

if scelta == 1:
    genera_array()

else:
    pass
"""arr1 = np.random.rand(3,4)
print(arr1)
"""
"""arr1 = arr.reshape(3,4)
print(arr1)"""

