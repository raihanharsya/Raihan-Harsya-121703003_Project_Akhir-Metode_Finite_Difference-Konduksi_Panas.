import numpy as np
import matplotlib.pyplot as plt

# Define parameters
s = 0.5  # Panjang sisi [m]
alpha = 50  # Koefisien Difusivitas Termal [m^2/s]
t_final = 1.5  # Waktu simulasi [s]
node = 50  # Jumlah titik grid

# Calculate grid spacing
dx = s / (node - 1)
dy = s / (node - 1)

# Calculate time step for stability
dt = 0.1 * min(dx**2, dy**2) / alpha

# Ensure stability condition
if alpha * dt / min(dx**2, dy**2) > 0.5:
    print("Warning: Stability condition may not be satisfied. Consider further reducing the time step.")

# Initialize temperature array
T = np.zeros((node, node))

# Set initial conditions
T[0, :] = 0  # Suhu tepi kiri
T[-1, :] = 100  # Suhu tepi kanan
T[:, 0] = np.linspace(0, 100, node)  # Suhu tepi bawah (variasi linear)
T[:, -1] = np.linspace(0, 100, node)  # Suhu tepi atas (variasi linear)

# Solve 2D heat conduction equation
for t in np.arange(0, t_final, dt):
    T[1:-1, 1:-1] = T[1:-1, 1:-1] + alpha * dt / dx**2 * (T[:-2, 1:-1] - 2 * T[1:-1, 1:-1] + T[2:, 1:-1]) + \
                    alpha * dt / dy**2 * (T[1:-1, :-2] - 2 * T[1:-1, 1:-1] + T[1:-1, 2:])

# Plot the temperature distribution at t = 1.5 seconds
plt.imshow(T, cmap='hot', origin='lower', extent=[0, s, 0, s])
plt.colorbar(label='Temperature (°C)')
plt.title(f'Temperature Distribution at t = {t_final} seconds')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()
