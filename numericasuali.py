'''
Scrivete un programma che genera 5 numeri casuali e li salva su un file, l’utente dovrà
cercare di indovinarne almeno 2 oppure avrà perso.'''

import random

#Inizializza una lista vuota per memorizzare i numeri casuali
random_numbers = []
num_input = 5




#Usa un ciclo for per generare i numeri casuali e aggiungerli alla lista
for i in range(num_input):
    random_number = random.randint(1, 6)  # Genera un numero intero casuale tra 1 e 100
    random_numbers.append(random_number)
    
#separatore = " "
with open("numericasuali.txt","w") as file:
    file.write("".join(map(str,random_numbers)))

'''with open("numericasuali.txt","r") as file:
    contenuto = file.read()
print(type(contenuto))'''

input = input("inserisci 5 valori ")

for i in range(num_input):
    if input in file: 
        print("ok")