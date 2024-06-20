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

'''Punto 3: Utilizzo di for
Scrivi un sistema che prende in input una lista di numeri e 
stampa il quadrato di ciascun numero nella lista.'''

#Definisco gli input
lista_numeri= []
aggiunta1 = int(input("quanti numeri si desidera aggiungere?"))

for i in range(aggiunta1):
    aggiunta2=int(input("che numero si desidera aggiungere?"))
    lista_numeri.append(aggiunta2)
    
print(lista_numeri)

#creo il ciclo for che per ogni numero nella lista stampa il quadrato
for i in lista_numeri:
    print(i**2)


#####

'''Punto 4: Utilizzo di if, while e for insieme 
Scrivi un sistema che prende in input una lista di numeri interi 
che precedente è stata valorizzata dall’utente.
Il sistema deve:
Utilizzare un ciclo for per trovare il numero massimo nella lista.
Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota,
altrimenti stampare il numero massimo trovato e il numero di elementi nella lista'''

#inizializzo le variabili necessarie
lista_numeri= []
#definisco una variabile per permettere all'utente di decidere il numero di elementi da aggiungere
aggiunta1 = int(input("quanti numeri si desidera aggiungere? "))

#creo un ciclo for in modo tale da dare la possibilità all'utente di creare la sua lista
for i in range(aggiunta1):
    aggiunta2=int(input("che numero si desidera aggiungere? "))
    lista_numeri.append(aggiunta2)
    
print(lista_numeri)

#creo un ciclo for per trovare il numero massimo
for i in lista_numeri:
    lista_numeri.sort()
print(lista_numeri[-1])

#creo il ciclo while per contare i numeri presenti in lista
#prima inizializzo le variabili necessarie:
condizione = True
conteggio = 0
#scrivo il ciclo while
while condizione == True:
    for i in lista_numeri:
        conteggio += 1 #aggiungo un contatore
    print(conteggio)
    break

#creo la condizione if con tutti i cicli sopra riportati
if lista_numeri == []: #definisco come condizione una lista vuota dettata dalle parentesi quadre
    print("Lista Vuota")
else: #nel caso in cui la lista non sia vuota
    for i in lista_numeri:
        lista_numeri.sort()
    print("il numero massimo è:") 
    print(lista_numeri[-1])
    while condizione == True:
        for i in lista_numeri:
            conteggio += 1
        print("il numero di elementi presenti nella lista è:")
        print(conteggio)
        break

