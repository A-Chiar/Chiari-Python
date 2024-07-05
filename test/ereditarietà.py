"""permette a una classe di ereditare attributi e metodi di una classe padre. Con super() possiamo richiamare
metodi e attributi della classe padre. Esiste anche il concetto di eredità multipla, per cui una classe figlio
può avere diverse classi padri. In più esiste anche il concetto dell'overwriting per cui possiamo importare una funzione
dalla classe padre e modificarne leggermente il comportamento.
"""

class Animale:  #creo una superclasse
    def __init__(self, nome,età):
        self.nome = nome
        self.età = età
    def fai_suono(self):
        if self.nome == "leone":
            return "ruggito"
        elif self.nome == "giraffa":
            return "landito"
        elif self.nome == "pinguino":
            return "garrito"
        else:
            print("animale non presente nello zoo ")
        return f"il {self.nome} fa il verso del {self.fai_suono}"


class Pinguino(Animale): #creo una classe figlia
    def __init__(self, nome, età):
        super().__init__(self, nome, età) #con il metodo super() che permette di richiamare metodi e attributi della super classe
    def metodo_caccia(self):
        print("il pinguino caccia i pesci nell'oceano")
    def fai_suono(self):
        print(super().fai_suono()) ##richiamo con super il metodo della classe padre
        
        

