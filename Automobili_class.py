class Automobile: #dichiaro la classe
    numero_di_ruote = 4 #primo attributo della classe ed è sempre valorizzato
    def __init__ (self, marca,modello): #metodo costruttore
        self.marca = marca #attributo di istanza
        self.modello = modello #attributo di istanza
    def stampa_info(self): #metodo di istanza
        print("L'automobile è una", self.marca, self.modello)


auto1 = Automobile("Fiat","500") #crea un oggetto Automobile
auto2 = Automobile("BMW","X3") #crea un altro oggetto di Automobile

auto1.stampa_info() #stampa "l'automobile è una Fiat 500"
auto2.stampa_info() #stampa "l'automobile è una BMW X3"