import matplotlib.pyplot as plt
import numpy as np

x = np.arange(20)
y = np.random.randint(1, 100, 20)

plt.plot(x, y, marker="o", color="black", ls="--")
plt.title("Ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()