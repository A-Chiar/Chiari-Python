#il dizionario non è obbligatorio, ma è meglio in questo caso 
#invece di fare due liste

#creare la classe ristorante
class Ristorante():
    stato = False #se è False è chiuso #attributo aperto
    menù = {} #utilizzare i dizionari, x evitare di dover creare due liste
    def __init__(self, nome,tipo_cucina): #classe costruttora
        self.nome = nome 
        self.tipo_cucina = tipo_cucina
        
    
    def __str__(self): #si può sostituire con descrivi_ristorante() o ha bisogno del metodo stringa?
        return f"Benvenuto a {self.nome}, qui potrai assaggiare i piatti tipici della cucina {self.tipo_cucina}"

    def stato_apertura(stato):
        if stato == True:
            print("il ristorante è aperto")
        elif stato == False:
            print("il ristorante è chiuso")
    
    def apri_ristorante(stato): #è corretto mettere stato piuttosto che self? dal momento che con self non mi legge la variabile stato indentata sotto
        stato = True
        print("il ristorante è aperto")
    
    def chiudi_ristorante(stato):
        stato = False
        print("il ristorante ora è chiuso")

    def aggiungi_al_menu(menù): # è giusto mettere menù e non self?
        portata = input("inserire portata ")
        prezzo = input("inserira il prezzo associato ")
        menù[portata] = prezzo
    
    def togli_dal_menu(menù):
        portata = input("inserire il portata da eliminare ")
        if portata in menù.keys():
            del menù[portata]
        else:
            print("la portata non è presente")

    def stampa_menù(menù):
        print(menù)


ristorante = Ristorante("sisi","nono")
ristorante.aggiungi_al_menu()
#il codice dà errore dicendo che Ristorante non supporta l'item assignment, trovare soluzione