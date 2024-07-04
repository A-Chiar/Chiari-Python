class Veicolo:
    def __init__(self,marca,modello,anno):
        self.__marca = marca
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
#da qui in giù serve un self
class Auto(Veicolo):
    def __init__(self,marca,modello, anno,numero_porte):
        super().__init__(marca, modello, anno)
        self.__numero_porte = numero_porte
    
    def suona_clacson(self):
        print("suona clacson")
    
class Furgone(Veicolo):
    def __init__(self,marca,modello,anno,capacità_carico):
        super().__init__(marca, modello,anno,capacità_carico)
        self.__capacità_carico = capacità_carico

    def carica(self):
        print()
    
    def scarica(self):
        print()
    
class Motocicletta(Veicolo):
    def __init__(self,marca,modello,anno,tipo):
        super().__init__(marca,modello,anno)
        self.__tipo = tipo

    def esegui_wheelie(self):
        if self.__tipo == "sportivo":
            print("la moto si alza su una ruota")
        else:
            print("la moto non riesce ad alzarsi su una ruota")
    def __set_anno(self,anno):
        self.anno = anno

class GestoreParcoVeicoli(Motocicletta):
    def __init__(self):
        self.__veicoli = []
    def set_anno(self,veicolo,anno):
        veicolo.__set_anno(anno)
    

    


