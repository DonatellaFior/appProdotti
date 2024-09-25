import matplotlib.pyplot as plt
import numpy as np

# Generiamo alcuni dati di esempio
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creiamo il grafico
plt.plot(x, y)

# Impostiamo i limiti per l'asse X e Y
plt.xlim(2, 8)  # Mostra solo i dati per X tra 2 e 8
plt.ylim(-0.5, 1)  # Mostra solo i dati per Y tra -0.5 e 1

# Mostriamo il grafico
plt.show()

fig, ax = plt.subplots(2, 1)

# Primo grafico: visualizzazione completa
ax[0].plot(x, y)
ax[0].set_title("Grafico completo")

# Secondo grafico: zoom su una porzione
ax[1].plot(x, y)
ax[1].set_xlim(4, 6)   # Zoom sull'asse X
ax[1].set_ylim(-0.5, 0.5)  # Zoom sull'asse Y
ax[1].set_title("Zoom su una porzione")

plt.tight_layout()
plt.show()