import matplotlib.pyplot as plt

categories = ['Attenzione', 'Voglia', 'Sonno']
values = [3, 1, 10]

plt.figure()
plt.bar(categories, values)
plt.title('Le mie stats oggi: ')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.show()
