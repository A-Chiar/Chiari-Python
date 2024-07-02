#il dizionario non è obbligatorio, ma è meglio in questo caso 
#invece di fare due liste
'''salvare in una lista ogni piatto ordinato, e creare una classe utente che può ordinare.'''
#creare la classe ristorante
class Ristorante():
    stato = False #se è False è chiuso #attributo aperto
    menù = {"pizza":"3"} #utilizzare i dizionari, x evitare di dover creare due liste
    def __init__(self, nome,tipo_cucina): #classe costruttora
        self.nome = nome 
        self.tipo_cucina = tipo_cucina
        
    
    def __str__(self): #si può sostituire con descrivi_ristorante() o ha bisogno del metodo stringa?
        return f"Benvenuto a {self.nome}, qui potrai assaggiare i piatti tipici della cucina {self.tipo_cucina}"

    def stato_apertura(self):
        if self.stato == True:
            print("il ristorante è aperto")
        elif self.stato == False:
            print("il ristorante è chiuso")
    
    def apri_ristorante(self): 
        self.stato = True
        print("il ristorante è aperto")
    
    def chiudi_ristorante(self):
        self.stato = False
        print("il ristorante ora è chiuso")

    def aggiungi_al_menu(self): 
        portata = input("inserire portata ")
        prezzo = input("inserira il prezzo associato ")
        self.menù[portata] = prezzo
        return self.menù
    
    def togli_dal_menu(self):
        portata = input("inserire il portata da eliminare ")
        if portata in self.menù.keys():
            del self.menù[portata]
        else:
            print("la portata non è presente")
        return self.menù
    
    def stampa_menù(self):
        print(self.menù)
'''salvare in una lista ogni piatto ordinato, 
e creare una classe utente che può ordinare.'''
class Utente():
    def __init__(self, nome_utente, Portata):
        self.nome_utente = nome_utente
        self.Portata = Portata
    '''def ordine(self):
        if self.Portata in self.menù():'''


#controllo che tutto funzioni:
ristorante = Ristorante("pizzeria","pizza")
print(ristorante)
print(ristorante.aggiungi_al_menu())
print(ristorante.stato_apertura())
print(ristorante.togli_dal_menu())
print(ristorante.chiudi_ristorante())
