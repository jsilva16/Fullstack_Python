from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, x**2, label="Ecc. cuadrática")

plt.legend()

plt.show()

plt.savefig('line_plot.pdf') 