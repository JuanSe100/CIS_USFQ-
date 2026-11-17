print("=" * 65)
print(" CURSO: INTRODUCCIÓN A LA INTELIGENCIA ARTIFICIAL")
print("=" * 65)
print('Calculo de la función de perdida para un ajuste lineal dado:')

#Importación de bibliotecas

import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Propiedades_Data_Frame(data):
    print('Número de filas: ', data.shape[0])
    print('Número de columnas: ', data.shape[1])
    print('\n====Tipos de variables====\n',data.dtypes)

def dibujar_recta(w, b):
    plt.scatter(x, y, s=3, alpha=0.15, label="datos")
    xs = np.linspace(0, 15, 100)
    plt.plot(xs, w * xs + b, color="C3", lw=2.5, label=f"$\\hat y = {w}x + {b}$")
    plt.ylim(0, 5.5)
    plt.xlabel("Ingreso $x$"); plt.ylabel("Valor $y$")
    plt.legend()
    plt.show()

#Importación de la Data
df = pd.read_csv ('california_housing_train.csv')
Propiedades_Data_Frame(df) #Propiedades del DataFrame

#Vales para el ajuste lineal y = x*w+b
print("\nIngrese los parámetros:")
print('Peso w:')
w = float(input ())    #Peso
print('Sesgo b:')
b = float(input ())    #Sesgo


