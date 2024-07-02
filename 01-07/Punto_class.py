

class Punto():
    x = 0
    y = 0

    ''' def __init__(self, x, y):
        self.x = x
        self.y = y'''
    
    def nuovipunto(self, nuovax, nuovay):
        self.x = nuovax
        self.y = nuovay
    
    def distanza_or(self):
        if self.x > 0 and self.y > 0:
            print("la differenza da zero è -->")
            print(self.x, self.y)
        if self.x > 0:
            print("la differenza da zero è -->")
            print(self.x)
        if self.y > 0:
            print("la differenza da zero è -->")
            print(self.y)

oggettPunto = Punto()

oggett = oggettPunto.nuovipunto(6,11)
#oggettPunto.nuovipunto()
print(oggett)