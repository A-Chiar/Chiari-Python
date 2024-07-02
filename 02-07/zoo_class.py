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
            continue
        print(f"il {self.nome} fa il verso del {self.fai_suono}")

animale = Animale("gatto", 8)
print(animale.fai_suono())