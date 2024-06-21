'''Scrivi un sistema ché faccia quanto segue:

Chieda all'utente di inserire una stringa.
Conti quante vocali (a, e, i, o, u, sia maiuscole che minuscole) sono presenti nella stringa.
Stampi il numero di vocali trovate nella stringa.'''

#chiedo all'utente di inserire una stringa
stringa = input("inserisci una stringa ")

#inizializzo la variabile lista, dove inserisco all'interno i caratteri che sono interessata a contare
lista = ["a","e","i","o","u","A","E","I","O","U"]
#inizializzo una variabile contatore pari a 0 che mi servirà successivamente nel ciclo for
contatore = 0


for i in stringa:
    if i in lista:
        contatore += 1 #aggiungo un contatore che aggiunga un elemento ogni volta che legge una vocale
print("il numero di vocali presenti nella stringa è", contatore)