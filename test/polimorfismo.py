"""Polimorfismo: permette al codice di cambiare forma ma non comportamento.Lo abbiamo visto nel caso delle variabili,
dove una variabile poteva cambiare contenuto, ma le operazioni che potevano essere effettuate, e quindi il comportamento,
dipendono pur sempre dal tipo della variabile. E lo abbiamo visto anche nel caso delle funzioni, dove potevamo richiamare
all'interno del codice funzioni con lo stesso nome ma che avevano comportamenti diversi"""

class Felino:
    def __init__(self,nome):
        self.nome = nome

    def metodo_caccia():
        return "il felino caccia di notte"

class Gatto(Felino):
    def __init__(self,nome):
        super().__init__(self,nome)
    
    def metodo_caccia():
        return "il gatto caccia i topi"
        
