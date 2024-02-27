import math
import random
import matplotlib.pyplot as plt
import os

wysokosc = 100
predkosc = 50
losowaodleglosc = random.randint(50, 340)
print("Odleglosc do celu wynosi: ", losowaodleglosc)

def trajektoria_pocisku(V0, alpha, h):
    alpha_rad = math.radians(alpha)
    g = 9.81
    t_total = (V0 * math.sin(alpha_rad) + math.sqrt((V0 * math.sin(alpha_rad))**2 + 2 * g * h)) / g
    t = 0
    dt = 0.0001
    trajektoria = []
    while t <= t_total:
        x = V0 * math.cos(alpha_rad) * t
        y = h + V0 * math.sin(alpha_rad) * t - 0.5 * g * t**2
        trajektoria.append((x, y))
        t += dt
    return trajektoria

proby = 0

if os.path.exists('trajektoria.png'):
    os.remove('trajektoria.png')

while True:
    kat = int(input("Podaj kat w stopniach: "))
    trajektoria = trajektoria_pocisku(predkosc, kat, wysokosc)
    x_koncowe = trajektoria[-1][0]
    proby += 1
    if x_koncowe >= losowaodleglosc - 5 and x_koncowe <= losowaodleglosc + 5:
        print("Strzelono na: ", x_koncowe)
        print("Cel osiagniety po ", proby, "probach")
        break
    else:
        print("Cel nie osiagniety, sprobuj ponownie")
        print("Cel jest na odleglosci: ", losowaodleglosc, "m")
        print("Strzelono na: ", x_koncowe)
        continue

plt.figure(figsize=(8, 6))
plt.plot(*zip(*trajektoria), marker='o') 
plt.title('Trajektoria pocisku')
plt.xlabel('Odległość (m)')
plt.ylabel('Wysokość (m)')
plt.grid(True)
plt.savefig('trajektoria.png')
plt.show()
