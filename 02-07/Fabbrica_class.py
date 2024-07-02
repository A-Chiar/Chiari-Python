class Prodotto():

    def __init__(self, nome, costo_produzione, prezzo_vendita): #creare il metodo costruttore 
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
    def calcola_profitto(self): #metodo calcolo del profitto
        return self.prezzo_vendita-self.costo_produzione #è corretta come soluzione per calcolare il profitto?

    class Elettronica(): ##non so come fare 
        def __init__(self, garanzia):
            self.garanzia = garanzia
    
    class Abbigliamento():
        def __init__(self, materiale):
            self.materiale = materiale
        

class Fabbrica():
    inventario = {"forbice":1,"gatto":4}
    

    def aggiungi_prodotto(self):
        domanda = input("vuoi aggiungere un prodotto? ")
        while domanda.lower() == "sì":
            aggiunta = input("che prodotto vuoi aggiungere ")
            quantità = input("quanti prodotti vuoi aggiungere ")
            self.inventario[aggiunta] = quantità
            return self.inventario
    
    def vendi_prodotto(self):
        vendita = input("inserire il prodotto venduto ")
        quantità = int(input("inserire la quantità venduta "))
        if vendita in self.inventario:
            self.inventario[vendita] -= quantità #funziona ma a che costo? 
            return self.inventario

    def resi_prodotto(self):
        vendita = input("inserire il nome del prodotto reso ")
        quantità = int(input("inserire la quantità di prodotto resa "))
        if vendita in self.inventario:
            self.inventario[vendita] += quantità
            return self.inventario


 #controllo che i metodi funzionino
prodotto = Prodotto("prodotto",3,4)
fabbrica = Fabbrica()
print(fabbrica.resi_prodotto())