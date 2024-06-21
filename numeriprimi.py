#inizializzare variabili
numero1 = int(input("inserisci il numero minimo dell'intervallo "))
numero2 = int(input("inserisci il numero massimo dell'intervallo "))

#inizializzare le liste
lista_primi = []
lista_nonprimi = []

#creare ciclo for per calcolare se i numeri sono primi
for i in range(numero1,numero2):
    primo = True
    for x in range(2,i):
        pass
        if i % x == 0:
            primo = False
    if primo:
        lista_primi.append(i) #se il numero è primo lo aggiunge alla lista dei numeri primi
    else:
        lista_nonprimi.append(i) #se il numero non è primo lo aggiunge alla lista dei numeri non primi
stampa =input("vuoi stampare la lista di numesi primi o la lista dei numeri non primi?")
if stampa == "primi":
    print(lista_primi)
elif stampa == "non primi":
    print(lista_nonprimi)