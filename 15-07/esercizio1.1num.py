import numpy as np

#condizione per il ciclo while
condizione = int(input("Benvenuto! Vuoi avviare il programma? 1 = sì, 2 = no "))
while condizione == 1:
    #richiedo il num min e max per la generazione dell'array tramite arange
    rangemin = int(input("inserire il numero minimo del range "))
    rangemax = int(input("inserire il numero massimo del range "))

    arr = np.arange(rangemin,rangemax)
    #stampo il tipo (deve essere intero)
    print(f"il tipo di array è {arr.dtype}")
    arr = np.array(arr,dtype='float64') #modifico l'array in float64
    print(f"il tipo di array è stato modificato in {arr.dtype}") #controllo che l'array sia stato correttamente modificato
    print(f"la forma del tuo array è {arr.shape}") #stampo la forma dell'array

    condizione = int(input("vuoi usare di nuovo il programma? 1 = sì, 2 = no ")) #chiedo all'utente se vuole continuare e modifico la condizione del ciclo while
    if condizione == 2: #stampa di uscita
        print("Uscita dal programma ")
    else:
        print("Riavvio del programma ")
