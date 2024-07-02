'''Create un classe libro che ha al suo interno:
-titolo;
- autore;
- prezzo;
- codice isbn viene generato automaticamente in maniera randomica ogni volta che inserito un libro;
- stato_prestito;

Metodo

Create poi 2 metodi:
- Metodo sconto per applicare lo sconto della percentuale passata al prezzo;
- Metodo prestito per cambiare lo stato del prestito, 
quindi se è libero diventa prestato, se è prestato diventa libero'''

class libro:
    def __init__(self, titolo, autore, prezzo, isbn, stato_prestito):
        self.titolo = titolo
        self.autore = autore 
        self.prezzo = prezzo
        self.isbn = isbn
        self.stato_prestito = stato_prestito

    def random_isbn():
        from random import randint
        codice = 0
        x = random.randint(1,9)
        for i in range(10):
            codice += x
        print(codice)

random_isbn()


            
        


