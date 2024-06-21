#inizializzo le variabili
numero = int(input("inserire un numero intero "))
lista_numeri = [] #la lista vuota mi servirà per la successiva somma
conteggio = 0

while numero != 0: #se il numero è diverso da zero, aggiunge il numero alla lista e chiede di inserire un altro numero
    lista_numeri.append(numero)
    numero = int(input("inserisci un altro numero "))
    if numero == 0:
        for i in lista_numeri:
            conteggio += i
        print("la somma dei numeri inseriti è: ", conteggio) #stampa la somma
        