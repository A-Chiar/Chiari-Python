import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

colore = "red"
plt.figure()
plt.hist(data, bins=30,color = colore)
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.show()