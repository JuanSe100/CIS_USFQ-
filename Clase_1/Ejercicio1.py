
import numpy as np
    
print("=== Sumatoria  1 ===")

resultado1= np.sum(np.arange(5)**2)

#Version hecha con python normal
acumulador = 0
for p in range(0,5):
    acumulador = acumulador + p**2

test = acumulador == resultado1   ##Booleano
if test==True:
    print("Resultado NumPy:", resultado1)
    print("Resultado Python:", acumulador)

print("\n== Sumatoria  2 ===")
   

print('np.arange()', np.arange(5))
