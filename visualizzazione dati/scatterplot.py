import numpy as np
import matplotlib.pyplot as plt
N = 50
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(N)

plt.figure()
plt.scatter(x, y,c=colors)
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()