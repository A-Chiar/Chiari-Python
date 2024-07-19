"""Hai a disposizione un dataset, che devi autogenerare,
contenuto in un DataFrame pandas con una singola colonna
temperature che rappresenta la temperatura giornaliera in
una città per un mese. 
Scrivi un programma Python che calcoli e stampi le seguenti
statistiche:
La temperatura massima
La temperatura minima
La temperatura media
La mediana delle temperature"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

T = np.random.randint(10,30,size = (30))

data =  {
    'Temperature': T
}
df = pd.DataFrame(data)
print(df)

T_max = df['Temperature'].max()
print("\n La temperatura massima è: ", T_max)

T_min = df['Temperature'].min()
print("\n La temperatura minima è: ", T_min)

T_mean = df['Temperature'].mean()
print("\n La temperatura media è: ", T_mean)


T_median = df['Temperature'].median()
print("\n La temperatura mediana è: ", T_median)

def graficoalinee():
    x = np.linspace(1,30,30)
    y = T
    plt.figure()
    plt.plot(x, y)
    plt.title('Temperature medie giornaliere ')
    plt.xlabel('Giorni')
    plt.ylabel('Temperatura')
    plt.show()

def massima_minima():
    categories = ['Minima', 'Massima','Media','Mediana']
    values = [T_min,T_max,T_mean,T_median]
    colors = ["blue","red","orange","yellow"]
    plt.figure()
    plt.bar(categories, values,color = colors)
    plt.title('La massima,la minima, la media e la mediana registrate questo mese sono: ')
    plt.xlabel('Statistiche')
    plt.ylabel('Gradi')
    plt.show()

#graficoalinee()
massima_minima()

