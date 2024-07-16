import numpy as np

scelta = input("""Cosa vuoi effettuare?
               1. generazione 50 numeri equidistanti
               2. generazione 50 numeri random
               3. somma singoli elementi array
               4. somma degli array
               5. somma degli elementi maggiori di 5
               6. uscita dal programma
               """)

def gen_array():
    arr = np.linspace(0,10,50)
    print(arr)
    return arr

def gen_randomarray():
    arr1 = np.random.rand(50)
    print(arr1)
    return arr1


def somma_singoli(arr,arr1):
    sum = arr + arr1
    print(sum)
    return sum

def somma(sum):
    sum1 = np.sum(sum)
    print(sum1)
    return sum1

def somma_5(sum):
    sum2 = 0
    for i in sum:
        if i > 5:
            sum2 += i
    print(sum2)
    return sum2
condizione = True
#while condizione = 
if scelta == '1':
    print(f"Gli elementi generati sono: {gen_array()}")
elif scelta == '2':
    print(f"Gli elementi generati sono: {gen_randomarray()}")
elif scelta == '3':
    print(f"La somma dei singoli elementi è {somma_singoli(gen_array(),gen_randomarray())}")
elif scelta == '4':
    print(f"La somma di tutti gli elementi è {somma(somma_singoli)}")
elif scelta == '5':
    print(f"La somma degli elementi maggiori di 5 è {somma_5(somma_singoli)}")
elif scelta == '6':
    print("uscita dal programma")
    condizione = False
else:
    print("il valore inserito non è valido")