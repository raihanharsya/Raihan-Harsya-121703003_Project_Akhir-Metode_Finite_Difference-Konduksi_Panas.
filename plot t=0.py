import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan variabel
L = 2.5  # Panjang plat [m]
alpha = 500  # Koefisien Difusivitas Termal [m^2/s]
t_initial = 0  # Waktu awal [s]
t_final_1 = 1.5  # Waktu pertama [s]
t_final_2 = 0  # Waktu kedua [s]
node = 100  # Jumlah titik grid
dx = L / (node - 1)  # Jarak antar titik grid [m]
dt = 0.5 * dx**2 / alpha  # Ukuran langkah waktu [s]

# Membuat array untuk menyimpan suhu pada setiap titik grid
T_initial = np.zeros(node)
T_initial[0] = 0  # Kondisi batas kiri
T_initial[-1] = 100  # Kondisi batas kanan

# Fungsi untuk menghitung suhu pada waktu tertentu
def solve_heat_equation(T, t_final):
    time_steps = int(t_final / dt)
    for _ in range(time_steps):
        T[1:-1] = T[1:-1] + alpha * dt / dx**2 * (T[:-2] - 2 * T[1:-1] + T[2:])
    return T

# Mensimulasikan suhu pada waktu awal
T_0 = T_initial.copy()

# Mensimulasikan suhu pada waktu t_final_1
T_1 = solve_heat_equation(T_initial.copy(), t_final_1)

# Mensimulasikan suhu pada waktu t_final_2
T_2 = solve_heat_equation(T_initial.copy(), t_final_2)

# Plot hasil simulasi
plt.figure(figsize=(10, 6))
plt.plot(np.linspace(0, L, node), T_0, label=f'T = {t_initial}s', linestyle='--', color='black')
plt.plot(np.linspace(0, L, node), T_1, label=f'T = {t_final_1}s')
plt.plot(np.linspace(0, L, node), T_2, label=f'T = {t_final_2}s')
plt.xlabel('Posisi (m)')
plt.ylabel('Suhu (°C)')
plt.legend()
plt.title('Simulasi Konduksi Panas 1 Dimensi')
plt.grid(True)
plt.show()
