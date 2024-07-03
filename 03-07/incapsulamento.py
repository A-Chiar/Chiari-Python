class ContoBancario:
    def __init__(self):
        self.__titolare = "Gatto"
        self.__saldo = 1000.00
    
    def deposita(self):
        if self.__saldo > 0:
            self.__saldo += 50
            return "operazione eseguita con successo "
        else:
            return "il saldo è negativo"
        
  
    def preleva(self):
        importo = 50
        if self.__saldo > importo:
            self.__saldo -= importo
            return "operazione eseguita con successo "
        else:
            return "l'importo da prelevare supera il saldo"
     
    def get_visualizza_saldo(self):
        print(self.__saldo)

    def get_titolare(self):
        x = self.__titolare.isalpha()
        if x == True:
            return "il titolare è una stringa non vuota"
        else:
            return "il nome del titolare non è valido"
    
    def set_titolare(self,nome):
        nome = "cane"
        self.__saldo = nome
        return "nome modificato"
#non ho ben capito come funziona il metodo set
conto = ContoBancario()
print(conto.set_titolare())
