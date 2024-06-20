'''Punto 1: Utilizzo di if
Scrivi un sistema che prende in input un numero e stampa "Pari" 
se il numero è pari e "Dispari" se il numero è dispari.'''

numero = int(input("Digitare un numero "))

if (numero%2) == 0:
    print("Pari")
else:
    print("Dispari")

#############

'''Punto 2: Utilizzo di while e range
Scrivi un sistema che prende in input un numero intero 
positivo n e stampa tutti i numeri da n a 0 (compreso), 
decrementando di 1.Deve potersi ripete all’infinito'''

NumeroInt = int(input("scrivere un numero intero positivo "))
condizione = True

while condizione == True:
    for i in range(NumeroInt,-1,-1):
        print(i)
    ciclo= input("si vuole ripetere il ciclo?")
    if ciclo == "sì":
        NumeroInt = int(input("inserire numero"))
    elif ciclo == "no":
        break

#############

'''TRACCIA Punto 3: Utilizzo di for
Scrivi un sistema che prende in input una lista di numeri e 
stampa il quadrato di ciascun numero nella lista.'''

#Definisco gli input
numero1 = int(input("inserire un numero"))
numero2 = int(input("inserire un numero"))
numero3 = int(input("inserire un numero"))
numero4 = int(input("inserire un numero"))

#creo una lista in cui inserire tutti gli input
lista_numeri = [numero1, numero2, numero3, numero4]

#creo il ciclo for che per ogni numero nella lista stampa il quadrato
for i in lista_numeri:
    print(i**2)


#####
