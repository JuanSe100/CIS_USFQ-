# Ejercicios
print("=" * 65)
print(" EJERCICIOS")
print("=" * 65)

#======================Funciones=========================================
def comprobar(prueba, mensaje):
    """Ejecuta una prueba y muestra ✅ o ❌ sin detener el notebook."""
    try:
        ok = bool(prueba())
    except Exception as e:
        ok = False
        mensaje += f"  (error: {type(e).__name__}: {e})"
    print(("✅ " if ok else "❌ ") + mensaje)
    return ok
#=======================================================================

#Importacion de bibliotecas
import pandas as pd
import numpy as np 
import os

#Importación de datos
df = pd.read_csv ('california_housing_train.csv')
x = df["median_income"].to_numpy()                # decenas de miles de USD
y = df["median_house_value"].to_numpy() / 100_000 # cientos de miles de USD



print('\nEjercicio 1')

def media_lista(valores):
    # sum() suma todos los números de la lista
    # len() cuenta cuántos números hay
    return sum(valores) / len(valores)

# Pruebas de validación
comprobar(lambda: abs(media_lista([1, 2, 3, 4]) - 2.5) < 1e-12, "media_lista([1,2,3,4]) == 2.5")
comprobar(lambda: abs(media_lista(list(y[:100])) - np.mean(y[:100])) < 1e-9, "coincide con np.mean")


print('\nEjercicio 2')

