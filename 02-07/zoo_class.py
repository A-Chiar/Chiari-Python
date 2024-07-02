class Animale:
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
        print(f"il {self.nome} fa il verso del {self.fai_suono}")


class Leone(Animale):
    def __init__(self, nome, età):
        Animale.__init__(self, nome, età)
    
    def metodo_caccia(self):
        print("il leone dorme, cacciano le leonesse")

class Giraffa(Animale):
    def __init__(self, nome, età):
        Animale().__init__(self, nome, età)
        super().fai_suono()
    def metodo_caccia(self):
        print("la giraffa caccia le foto sugli alberi")


class Pinguino(Animale):
    def __init__(self, nome, età):
        Animale.__init__(self, nome, età)
        super().fai_suono()
    def metodo_caccia(self):
        print("il pinguino caccia i pesci nell'oceano")
    def fai_suono(self):
        return super().fai_suono()
        
    

pinguino = Pinguino("pinguino",9)
print(pinguino.metodo_caccia())