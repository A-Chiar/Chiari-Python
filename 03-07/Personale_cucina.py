class PersonaleCucina:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    def lavora(self):
        print(f"l'impiegato si chiama {self.nome} ed ha {self.età} ")


class Chef(PersonaleCucina):
    def __init__(self, nome, età,specialità):
        PersonaleCucina.__init__(self,nome,età)
        self.specialità = specialità

    def prepara_menu(self):
        nuovi_piatti = []
        domanda = input("vuoi inserire un nuovo piatto?")
        while domanda.lower() == "sì":
            piatto = input("inserire il nome del piatto ")
            if piatto not in nuovi_piatti:
                nuovi_piatti.append(piatto)
            elif piatto in nuovi_piatti:
                print("il piatto è già presente nella lista")
            domanda = input("vuoi inserire un altro prodotto?")
            return nuovi_piatti


class SuosChef(PersonaleCucina):
    inventario = {}
    def __init__(self, nome, età):
        PersonaleCucina.__init__(self,nome,età)
        
    def gestisci_inventario(self):
        domanda = input("vuoi inserire un nuovo prodotto nell'inventario? ")
        while domanda.lower() == "sì":
            prodotto = input("inserire il nome del prodotto ")
            quantità = int(input("inserire la quantità di prodotto "))
            if prodotto in self.inventario:
                self.inventario[prodotto] += quantità
            elif prodotto not in self.inventario:
                self.inventario[prodotto] = quantità
            domanda = input("vuoi inserire un altro prodotto?")
        return self.inventario

class CuocoLinea(PersonaleCucina):
    def __init__(self, nome, età):
        
        PersonaleCucina.__init__(self,nome,età)

    def cucina_piatto(self):
        nome_piatto = input("inserisci il nome del piatto ")
        return f"il Cuoco di linea {self.nome} prepara il piatto {nome_piatto}"


#chef = Chef("giovanni",32,"sushi")
#print(chef.prepara_menu())
#suoschef =  SuosChef("giovanni",32)
#print(suoschef.gestisci_inventario())
cuocolinea = CuocoLinea("giovanni",32)
print(cuocolinea.cucina_piatto())