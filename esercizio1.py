numero = int(input("inserire un numero intero "))
lista_numeri = []
conteggio = 0

while numero != 0:
    lista_numeri.append(numero)
    numero = int(input("inserisci un altro numero "))
    if numero == 0:
        for i in lista_numeri:
            conteggio += i
        print("la somma dei numeri inseriti è: ", conteggio)