print("=" * 65)
print(" CURSO: INTRODUCCIÓN A LA INTELIGENCIA ARTIFICIAL")
print("=" * 65)
print()
print("El problema que resolveremos en este curso consta en estudiar")
print("17,000 barrios de California. Para cada uno conocemos:")
print("  • Su ingreso mediano")
print("  • El valor mediano de sus viviendas")
print()
print("-" * 65)
print("Y responderemos a la siguiente pregunta:")
print("¿Si te doy el ingreso de un barrio nuevo, puedes predecir")
print("el valor de sus casas?")
print("-" * 65)


print ("De manera preliminar veamos la Data que usaremos")
#Importación de bibliotecas
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parámetros para las imagenes
plt.rcParams["figure.figsize"] = (7, 4.5)
plt.rcParams["axes.grid"] = True
# ==========================================
#    FUNCIONES
# ==========================================
def dibujar_recta(w, b):
    plt.scatter(x, y, s=3, alpha=0.15, label="datos")
    xs = np.linspace(0, 15, 100)
    plt.plot(xs, w * xs + b, color="C3", lw=2.5, label=f"$\\hat y = {w}x + {b}$")
    plt.ylim(0, 5.5)
    plt.xlabel("Ingreso $x$"); plt.ylabel("Valor $y$")
    plt.legend()
    plt.show()
#===========================================

RUTA = "/content/sample_data/california_housing_train.csv"
if not os.path.exists(RUTA):  # por si no estás en Colab
    RUTA = "https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv"
df = pd.read_csv(RUTA)
print("\nDimensiones del archivo de Datos")
print('Número de filas', df.shape[0])
print('Número de columnas', df.shape[1])

# Conversión DF a arreglos numpy
x = df["median_income"].to_numpy()                # decenas de miles de USD
y = df["median_house_value"].to_numpy() / 100_000 # cientos de miles de USD


print("Desea ver una grafica de los datos (s/N)")
leer = input()

if(leer == "s"):
    plt.scatter(x, y, s=3, alpha=0.2)
    plt.xlabel("Ingreso mediano $x$ (decenas de miles de USD)")
    plt.ylabel("Valor mediano $y$ (cientos de miles de USD)")
    plt.title("Datos de entrenamiento")
    plt.show()


print("===================AJUSTE LINEAL==============")
print("    ŷ = w * x + b")
print("\n- x: la entrada (ingreso)")
print('ŷ : la predicción.')
print('\nParámetros')
print("- w (peso) and  b (sesgo) ")

print('\n Ingrese valores de los parámetros')
print('Ingrese el valor del peso b:')
w = float(input ())    #Peso
print('Ingrese el valor del sesgo w:')
b = float(input ())    #Sesgo

dibujar_recta( w,b)

df.to_csv('california_housing_train.csv', index = False)   


