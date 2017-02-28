import numpy as np
import random
import math
import matplotlib.pyplot as plt
random.seed()

n = int(input("Ile ruchów? "))
x = y = 0
wsp_x = [0]
wsp_y = [0]

for i in range(0,n):
    #Wylosuj kąt i zamień go na radiany
    rad = math.radians(float(random.randint(0,360)))
    x = x + np.cos(rad)     # wyliczamy współrzędne x i y
    y = y + np.sin(rad)
    print(x, y)
    wsp_x.append(x)
    wsp_y.append(y)
    c = np.sqrt((wsp_x[i]-wsp_x[i-1])**2 + (wsp_y[i]-wsp_y[i-1])**2)
print(wsp_x, wsp_y)



# Obliczamy wektor końcowego przesunięcia
s = np.fabs(np.sqrt(x**2 + y**2))
w_x = [0, wsp_x[len(wsp_x)-1]]
w_y = [0, wsp_y[len(wsp_y)-1]]
print("Wektor przesunięcia: ", s)

plt.plot(wsp_x, wsp_y, "o:", color = "green", linewidth = 3, alpha = 0.5)
plt.plot(wsp_x, wsp_y, c, "r:", color = "blue", linewidth = 1, alpha = 0.2)
plt.plot(w_x, w_y, s, "o:", color = "blue", linewidth = 2, alpha = 1)
plt.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc = "upper left")
plt.xlabel("Wsp_x")
plt.ylabel("Wsp_y")
plt.title("Ruchy Browna")
plt.grid(True)
plt.show()


