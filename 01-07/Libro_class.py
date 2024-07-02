
class Libro():
    def __init__(self, titolo, autore,pagine):
        self.titolo = titolo 
        self.autore = autore
        self.pagine = pagine
    def __str__(self):
        return f"il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine"

               
#Libro1 = Libro("Gomorra","Saviano","200")
#print(Libro1)

class Biblioteca:
    def crea_libro(self):
        libri = []
        while True: 
            titolo = input("inserire titolo libro ")
            autore = input("inserire autore ")
            pagine = input("inserire pagine ")
            libri.append(Libro(titolo,autore,pagine))
            a = input("vuoi aggiungere un nuovo libro (sì per continuare)")
            if a != "sì":
                break
        return libri
    def __str__(self):
        return f"il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine"

biblio = Biblioteca()
biblio.crea_libro()

