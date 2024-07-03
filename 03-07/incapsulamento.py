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
        return self.__saldo

    def get_titolare():
       self.__titolare.isalpha()
conto = ContoBancario()
print(conto.preleva())
