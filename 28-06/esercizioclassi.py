'''Create una classe calciatore che ha come attributi:
- nome:
- ruolo:
- valore:
creare un metodo getter per avere solo i valori dei calciatori
e un metodo setter per settare il ruolo del calciatore 
create almeno 3 calciatori e poi printate in ordine di valore i calciatori'''

class Calciatore:
    def __init__(self,nome, ruolo, valore):
        self.nome = nome
        self.ruolo = ruolo
        self.valore = valore
    def __str__(self):
        return f"Nome:{self.nome}, Cognome: {self.ruolo}, Valore {self.valore}"
    
    def visualizza_valore(self):
        print(self.valore)

    def setta_ruolo(self):
        self.ruolo = input("inserisci ruolo ")

    def max_valore(self)
        lista = self.valore()
        max(lista)
pippo = Calciatore("pippo","", 7)
franco = Calciatore("franco", "",10)
gigi = Calciatore("gigi", "", 9)

lista = [pippo,franco,gigi]
for i in lista:
    i.setta_ruolo()



#franco.setta_ruolo()
'''pippo.visualizza_valore()
print(pippo)
print(franco)
print(gigi)'''

