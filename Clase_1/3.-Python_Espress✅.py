import numpy as pd
import math

#Funciones en Python
def valor_promedio(lista):
    contador = sumador = 0
    for p in lista:
        contador = contador +1
        sumador += p

    promedio = sumador/contador
    return promedio

print('========REPASO PYTHON EXPRESS =======')
print('')

print('Tipos de variables en Python')
print('================================')


n_casas = 17000       # int
precio = 2.5          # double
ciudad = "Quito"      # String
es_caro = precio > 3  # bool

print()
print('17000        int: ', type(n_casas))
print('2.5          double: ', type(precio))
print('Quito        String: ', type(ciudad))
print('True/False   bool: ', type(es_caro))

print('\nListas indices y rebandas')
print('================================')
print('Listas:  [1.2, 3.4, 2.2, 5.0, 0.9] ')
precios = [1.2, 3.4, 2.2, 5.0, 0.9]
print('\nImpresión del primer y último elemento de una lista')
print('Primer elemento', precios[0], '   Último elemento', precios[-1])

print('\nElementos 1 y 2:')
print(precios[1:3])

print('Tamaño de la lista(# de elementos):')
print(len(precios))

print('\n Agregar un elemento más al final de la lista lista.append(value)')
precios.append(4.1)
print(precios)


print('\nCICLOS CONDICIONALES Y COMPRESIONES DE LISTA')
print('==============================================')
print('Usando un ciclo for encontrar el valor de la suma de una lista')
total1 = 0
total2 = 0
for p in precios:
    if p > 2:
        total2 += p
    total1 += p

print('La suma de los valores de la lista es  : ', total1 )
print('La suma de los valores mayores qeu 2 es: ', total2 )


print('\nEncontrar la norma de la lista Precios')
xx = 0; 
for x in precios:
    xx += x**2
print('Norma de la lista precios: ', math.sqrt(xx))


print('\nCompresión de lista:')
print('print(sum([p for p in precios if p > 2]))')


print('\nFUNCIONES BÁSICAS EN PYTHON')
print('==============================================')
print('Genera un función en python que devuelva el promedio de la lista precios y que reciba a lista precios como entrada no usar len() o sum()')
print('\nValor promedio: ',valor_promedio(precios))
