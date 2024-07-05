"""l'incapsulamento permette di nascondere implementazioni del codice che vogliamo mantenere private.
abbiamo 3 livelli nell'incapsulamento:
- GLOBALE: è il livello più alto, questa variabile può essere accessibile dappertutto, a meno che non venga oscurata 
da una variabile con lo stesso nome in una funzione
-LOCALE quella variabile la si può accedere solo all'interno della funzione
-NONLOCAL riguarda le funzioni annidate """


class Veicolo:
      def __init__(self,marca,modello,anno): 
        self.__marca = marca  #con due underscore posso rendere privati gli attributi
        self.__modello = modello
        self.__anno = anno
        self.__accensione = False

    def accendi(self):
        self.__accensione = True
        if self.__accensione == True:
            print("il veicolo ora è acceso")
        else:
            print("il veicolo non si è acceso")
    
    def spegni(self):
        self.__accensione = False
        if self.__accensione == False:
            print("il veicolo ora è spento")
        else:
            print("il veicolo non si è spento")
    def __set_marca(self,marca):  #con get e self posso permettere di accedere e modificare gli elementi privati
        self.marca = marca
    
    def __set_modello(self,modello):
        self.modello = modello
    
    def __set_anno(self,anno):
        self.anno= anno
    
    def __get_marca(self,marca):
        self.marca = marca
    
    def __get_modello(self,modello):
        self.modello = modello
    
    def __get_anno(self,anno):
        self.anno = anno

class GestoreParcoVeicoli(Veicolo):
    def __init__(self):
        Veicolo.__init__()
        self.__veicoli = []
    
    def set_anno(self,veicolo,anno):
        veicolo.__set_anno(anno)

    def aggiungi_veicolo(self,veicolo):
        veicolo.__Veicolo__set_marca(input("inserire marca ")) 
        veicolo.__Veicolo__set_modello(input("inserire modello "))
        veicolo.__Veicolo__set_anno(input("inserisci anno "))
        self.__veicoli.append(veicolo)

veicolo = GestoreParcoVeicoli()
veicolo.aggiungi_veicolo()