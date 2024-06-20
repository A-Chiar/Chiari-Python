

condizione= True

while condizione == True:
    scelta = input("Digita 1 se vuoi inserire un numero. Digita 2 se vuoi inserire una stringa ")
    if scelta =="1":
        numero= int(input("inserisci il numero "))
        if numero % 2 == 0:
            print("il numero è pari")
        else:
            print("il numero è dispari")
    elif scelta =="2":
        stringa= input("inserisci la stringa da inserire ")
        lunghezza_stringa = len(stringa)
        if lunghezza_stringa %2 == 0:
            print("la stringa è composta da un numero pari di caratteri")
        else:
            print("la stringa è composta da un numero dispari di caratteri")
    rip= input("si vuole ripetere? ")
    if rip == "sì":
        continue
    elif rip == "no":
        break

####
numero1 = int(input("inserisci il numero minimo dell'intervallo "))
numero2 = int(input("inserisci il numero massimo dell'intervallo "))

lista_pari = []
lista_dispari = []

for i in range(numero1,numero2):
    pass
    if i % 2 == 0:
        lista_pari.append(i)
    elif i % 2 == 1:
        lista_dispari.append(i)
stampa =input("vuoi stampare la lista di numesi pari o la lista dei numeri dispari?")
if stampa == "pari":
    print(lista_pari)
elif stampa == "dispari":
    print(lista_dispari)
