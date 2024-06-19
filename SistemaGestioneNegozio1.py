'''TRACCIA Lo scopo di questo esercizio è implementare un sistema di gestione per un negozio che deve interagire con clienti, 
gestire l'inventario e permettere agli amministratori di supervisionare le operazioni. Il sistema sarà strutturato in tre parti 
principali:
Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.'''
#creo le variabili:
controllo = True
selezione = input("Salve, si desidera visitare il negozio? ")
lista_prodotti = ["matita", "penna", "foglio", "agenda"]
acquisti = []

#ciclo if per definire le varie opzioni da effettuare possibili
if selezione == "sì":
    while controllo == True:
        selezione2 = input("vuoi vedere i prodotti? ")
        if selezione2 == "sì":
            print(lista_prodotti)
        else:
            pass
        selezione3 = input("Salve, si desidera effettuare acquisti?")
        if selezione3 == "sì":
            print(acquisti)
            acquisti2 = input("cosa si intende acquistare?")
            acquisti.append(acquisti2)
        elif selezione3 == "no":
            #per fermare il ciclo while, nel momento in cui il cliente non vuole più acquistare
            break
        else:
            print("risposta non valida")
    


        

        


            