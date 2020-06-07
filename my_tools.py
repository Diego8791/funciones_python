#!/usr/bin/env python
'''
Módulos [Python]
Ejercicios de práctica
---------------------------
Autor: Diego Farias
Version: 1.1

Descripcion:
Módulo creado para la resolución de ejercicios de práctica
de funciones. 
'''

__author__ = "Diego Farias"
__email__ = "dfarias8791@gmail.com"
__version__ = "1.1"

import math
import random

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