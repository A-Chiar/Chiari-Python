'''Scrivi un sistema ché faccia quanto segue:

Chieda all'utente di inserire un numero intero positivo n.
Se il numero inserito non è positivo, chieda nuovamente l'inserimento fino a quando non viene inserito un numero positivo.
Una volta ottenuto un numero positivo n, il programma dovrà:
Stampare tutti i numeri pari da 0 a n inclusi.
Calcolare e stampare la somma di tutti i numeri dispari da 0 a n inclusi.
terminare solo dopo tre tentativi ("hai finito i tentativi") o dopo che una soma totale supera 250 ("hai vinto")'''

#il codice dovrebbe essere funzionante

#inizializzo le variabili 
condizione = True
somma_num_dispari = 0
tentativi = 0

#creo un ciclo while che mi permetta di effettuare più tentativi
while condizione == True:
    tentativi += 1 #questa variabile serve a conteggiare il numero di tentativi
    lista_pari = []
    numero = int(input("inserisci un numero intero positivo n "))
    if numero <= 0:
        numero = int(input("il numero non è valido, inserire di nuovo"))
    elif numero >= 0:
        print("il numero è valido")
        for i in range(0,numero+1):
            if i % 2 == 0:
                lista_pari.append(i) #questo ciclo for non funziona bene 
        print("la lista dei numeri pari presenti tra 0 e ", numero, "è ", lista_pari)
        for i in range(0,numero+1):
            if i % 2 != 0:
                 somma_num_dispari += i
        print("la somma dei numeri dispari è ", somma_num_dispari)
        if somma_num_dispari > 250:
             print("complimenti hai vinto")
             break #abbiamo raggiunto il nostro obiettivo, possiamo interrompere il ciclo con break
        elif somma_num_dispari <= 250: #se il numero è < a 250 permette di rientrare nel ciclo while
             print("hai altri 3 tentativi per superare il numero 250")
             #condizione = True
        if tentativi == 3: #questa condizione mi permette di fermare il ciclo dopo 3 tentativi
             print("hai finito i tentativi")
             condizione = False #la condizione è falsa e non rientra nel ciclo while
       

             
            
             
                

