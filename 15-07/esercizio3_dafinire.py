import numpy as np

menù = input("""quale operazione vuoi effettuare in seguito alla creazione della matrice:
             1. generare una sottomatrice centrale 4x4
             2. invertire le righe della matrice estratta
             3. estrarre la diagonale della matrice invertita
             4. sostituire gli elementi della matrice invertita che sono multipli di 3 con -1
                """)

def matrice():
    matr = np.random.randint(1,101,size=(6,6))
    print(matr)
    return matr

def estai(matr):
    estratta = matr[1:5,1:5]
    print(estratta)
    return estratta




