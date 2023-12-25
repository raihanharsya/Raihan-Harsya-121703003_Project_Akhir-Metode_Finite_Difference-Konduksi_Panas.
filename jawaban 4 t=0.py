import numpy as np
import matplotlib.pyplot as plt

# Define parameters
s = 0.5  # Panjang sisi [m]
alpha = 50  # Koefisien Difusivitas Termal [m^2/s]
t_final = 0  # Waktu simulasi [s]
node = 50  # Jumlah titik grid

# Calculate grid spacing
dx = s / (node - 1)
dy = s / (node - 1)

# Initialize temperature array
T = np.zeros((node, node))

# Set initial conditions
T[0, :] = 0  # Suhu tepi kiri
T[-1, :] = 100  # Suhu tepi kanan
T[:, 0] = np.linspace(0, 100, node)  # Suhu tepi bawah (variasi linear)
T[:, -1] = np.linspace(0, 100, node)  # Suhu tepi atas (variasi linear)

# Solve 2D heat conduction equation
for t in np.arange(0, t_final, 0.01):  # Using small time steps for better visualization
    T[1:-1, 1:-1] = T[1:-1, 1:-1] + alpha * 0.01 / dx**2 * (T[:-2, 1:-1] - 2 * T[1:-1, 1:-1] + T[2:, 1:-1]) + \
                    alpha * 0.01 / dy**2 * (T[1:-1, :-2] - 2 * T[1:-1, 1:-1] + T[1:-1, 2:])

# Plot the temperature distribution at t = 0
plt.imshow(T, cmap='hot', origin='lower', extent=[0, s, 0, s])
plt.colorbar(label='Temperature (°C)')
plt.title(f'Temperature Distribution at t = {t_final} seconds')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()
