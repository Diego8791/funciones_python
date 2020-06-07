#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import random
import math


def promedio(numeros):
    if len(numeros) == 0:
        # print('la lista esta vacia')
        promedio_lista = 'la lista esta vacia'
        return promedio_lista
    else:
        promedio_lista= sum(numeros) / len(numeros)
        # print('El promedio es', promedio_lista)
        return promedio_lista


def lista_aleatoria(inicio, fin, cantidad):
    numeros = []
    for numero in range(cantidad):
        numero = random.randrange(inicio, fin+1)
        numeros.append(numero)
    # print(numeros)
    return numeros


def ordenar(numeros):
    opcion = input('Indique el el orden a implementar (a-Descendente/b-Ascendente): ')
    if opcion == 'a':
        numeros.sort(reverse=True)
    elif opcion == 'b':
        numeros.sort()
    else:
        print('Opcion no valida')

# Inove: Sugerimos que cuando el elemento no está en
# la lista aún así se retorne "0" para que el codigo
# que llame a esta función pueda manejar ese caso
def contar(numeros, elemento):
    if (elemento in numeros) == False:
        cant_rep = 0
    else:
        cant_rep = numeros.count(elemento)
    return cant_rep 


def buscar(numeros, index_elem):
    lista_index = []
    for i in range(len(numeros)):
        if index_elem == numeros[i]:
            lista_index.append(i)
    return lista_index
    

def ej1():
    # Ejercicios con funciones del sistema
    numeros = [2, 4, 6, 8, 10, 12] 

    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros

    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle
    https://docs.python.org/3.7/library/functions.html

    La función debe retornar el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado
    '''
    
    promedio_lista = promedio(numeros)
    print('El promedio de la lista es',promedio_lista)


def ej2():
    # Ejercicios con modulos del sistema

    inicio = 0
    fin = 10
    cantidad = int(input('Indique la cantidad de numeros aleatorios: '))

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    # numero = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html

    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.
    def lista_aleatoria (inicio, fin, cantidad)
    Dicha función debe retornar la lista de elementos random generados.
    '''
    # numeros = lista_aleatoria (inicio, fin, cantidad)
    
    numeros = lista_aleatoria(inicio, fin, cantidad)

    # Imprima en pantalla la lista de elementos generados
    # print(....)
    print('Lista de numeros:',numeros)

    # Utilice el método random.choice para obtener 2 numeros
    # de la lista de elementos generados
    # numero_1 = random.choice(...)
    numero_1 = random.choice(numeros)    
    print('El primer numero elegido de', numeros,'es',numero_1)
    
    # numero_2 = random.choice(...)
    numero_2 = random.choice(numeros)
    print('El segundo numero elegido de',numeros,'es',numero_2)
    
    # Importar en este programa/documento el modulo "math"
    # Calcular la raiz cuadrada (square root) de esos
    # dos numeros obtenidos utilizando el método del
    # módulo "math" que crea correspondiente
    # Documentación oficial de math
    # https://docs.python.org/3.7/library/math.html
    # NOTA: Puede buscar en el medio que prefiera la info
    # solicitada

    # raiz_cuadrada_1 = ....
    raiz_cuadrada_1 = math.sqrt(numero_1)
    # raiz_cuadrada_2 = ....
    raiz_cuadrada_2 = math.sqrt(numero_2)
    print('La raiz cuadrada de',numero_1,'es',round(raiz_cuadrada_1, 2))
    print('La raiz cuadrada de',numero_2,'es',round(raiz_cuadrada_2, 2))


def ej3():     
    # Ejercicios de listas y métodos
    
    numeros = [2, 4, 6, 8, 10, 12]
    ordenar(numeros)
    print(numeros)
    
    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python
    La función no hace falta que retorne la lista ordenada,
    ya que al tratarce de una lista se pasa como referencia
    a la función (es decir que las modificaciones realizadas
    en la función afectan a la variable pasada como argumento)

    '''


def ej4():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    inicio = 1
    fin = 9
    cantidad = cantidad_numeros
    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado 
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''
    numeros = lista_aleatoria(inicio, fin, cantidad)
    print(numeros)

    elemento = int(input('Indique el elemento a contar: '))
    cant_rep = contar(numeros, elemento)
    print('La cantidad de veces que se repite',elemento,'es',cant_rep)

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)

def ej5():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5
    cantidad = cantidad_numeros
    inicio = 1
    fin = 9
    
    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive
    '''
    numeros = lista_aleatoria(inicio, fin, cantidad)
    print(numeros)
    index_elem = int(input('Indique el elemento a buscar el indice: '))
    
    '''
    Generar una una nueva funcion que se llame "buscar",
    que genere una lista con los índice de las posiciones
    en donde se encuentra dicho elemento en la lista.
    Si el elemento en la lista no existe, la función
    debe retornar una lista vacia.
    Para encontrar los índices del elemento en la lista
    puede usar el método "index" o bucles.
    Recuerde que el elemento puede repetirse más de una
    vez en la lista.
    '''
    lista_index = buscar(numeros, index_elem)
    print(lista_index)
    print('La cantidad de veces que se repite',index_elem,'es',len(lista_index))

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    #ej5()
