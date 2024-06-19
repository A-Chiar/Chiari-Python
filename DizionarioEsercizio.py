'''TRACCIA: Andiamo a creare 3 input che riempiamo con booleano un numero intero e una stringa  
li inseriamo in una lista

e inseriamo la lista come valore di un dizionario per chiave ‘tipididato’:'''
# creare input e chiedere input
lista = []
a =(input("inserire un True o un False"))
b =(input("inserire un numero intero"))
c =(input("inserire una stringa"))

#aggiungere in lista gli input
lista.append(a)
lista.append(b)
lista.append(c)
print(lista)

#creare dizionario
dizionario = {"tipididato": lista}
print(dizionario)