class Posto():
    def __init__(self):
        self.__numero = 1
        self.__fila ="M"
        self.__occupato = True
    
    def prenota(self):
        if self.__occupato != True:
            print("il posto è occupato")
        elif self.__occupato == True:
            print("il posto è stato prenotato con successo ")
            self.__occupato = False
    
    def libera(self): 
        if self.__occupato != True:
            print("il posto è stato liberato ")
            self.__occupato = False
        elif self.__occupato == True:
            print("il posto è già libero ")
            
    def get_numfil(self):
        return f"il posto {self.__numero}{self.__fila} è occupato? {self.__occupato}"


class PostoVIP(Posto):
    def __init__(self, __numero, __fila, __occupato):
        Posto.__init__(self,__numero, __fila, __occupato)
        self.servizi_extra = ["accesso al lounge", "servizio in posto"]
    def prenotazione(self):
        super().prenota()
        extra = input("vuoi aggiungere un servizio extra? ")
        if extra.lower() == "sì":
            extra1 = input("quale servizio extra vuoi aggiungere? Accesso lounge o Servizio in posto")
            if extra1.lower()  == "accesso lounge":
                print("aggiunto con successo")
            elif extra1.lower()== "servizio in posto":
                print("aggiunto con successo")

class PostoStandard(Posto):
    def __init__(self,online):
        self.online = online

class Teatro:
    def __init__(self):
        self.__posti = ["1A","2A","3A"]
        self.__postioccupati = ["1B","2B","3B"]
        
    def prenota_posto(self):
        posto = input("inserire il numero e la fila del posto da prenotare ")
        if posto in self.__posti:
            self.__postioccupati.append(posto)
            self.__posti.remove(posto)
            print("il posto è stato prenotato ")
        else:
            print("il posto è occupato o non presente")

    def get_stampa_posti_occupati(self):
        return self.__postioccupati

#posto = Posto()
#teatro = Teatro()
postovip = PostoVIP(1,"M", True)
print(postovip.prenotazione())
#print(teatro.get_stampa_posti_occupati())
