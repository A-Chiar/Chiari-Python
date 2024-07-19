"""Testo dell'esercizio:
Creato un DataFrame pandas con tre colonne: 'Altezza', 'Peso' e età di un gruppo
di persone, normalizza i dati di 'Altezza' e 'Peso' usando la normalizzazione min-
max (ridimensiona i valori in modo che varino tra 0 e 1). 
Assicurati di lasciare inalterata la colonna età; mostra il DataFrame
originale e quello modificato.
Fornisci un codice che:
Carichi il DataFrame (puoi assumere che i dati siano già disponibili in un
DataFrame chiamato df).
Applichi la normalizzazione min-max alle colonne 'Altezza' e 'Peso'.
Stampa sia il DataFrame originale sia quello modificato per compararli.
"""


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

altezza = np.random.randint(150,170,size = (10))
peso = np.random.randint(50,120,size = (10))
età = np.random.randint(20,50,size = (10))

data =  {
    'Altezza': altezza,
    'Peso': peso,
    'Età': età
}
df = pd.DataFrame(data)
print("\n Il dataframe è:",df)

print("\n I valori normalizzati sono: ")
df['Altezza']=(df['Altezza'] - df['Altezza'].min()) / (df['Altezza'].max() - df['Altezza'].min())
df['Peso']=(df['Peso'] - df['Peso'].min()) / (df['Peso'].max() - df['Peso'].min())

print(df)

sns.histplot(data=df, x='Peso',kde=True)
plt.title('Distribuzione peso nel campione')
plt.show()
