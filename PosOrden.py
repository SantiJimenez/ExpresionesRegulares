#!/usr/bin/python
# -*- coding: utf-8 -*-
from Nodo import *
from Pila import Pila
from Verificador import *
import sys

intentos = 0


def leerCadena():
    cadena = raw_input('Ingrese la cadena de caracteres a operar:')
    listaCaracteres = cadena.split(' ')
    longitudCadena = len(listaCaracteres) 

    print longitudCadena 
    
    for i in range(0, longitudCadena):
        print i
        if verificarToken(listaCaracteres[i]) == False:
            print 'La cadena ha sido ingresada incorrectamente: \n'
            leerCadena()
        elif longitudCadena-1 == i:
            print 'listaCaracteres', listaCaracteres
            return listaCaracteres


# if verificarCadena(listaCaracteres) == True:
#       return listaCaracteres
# else:
#         if intentos >= 3:
#                 intentos += 1
#                 print 'La cadena ingresada es incorrecta. Verifique los caracteres ingresados'
#                 leerCadena()
#         else:
#                 sys.exit()

def crearArbol(lista, pila):
    for i in range(0, len(lista)):
        if lista[i] in '+-*/=':
            der = pila.sacarElemento()
            izq = pila.sacarElemento()
            nodoAux = Nodo(lista[i], izq, der)
            pila.agregarElemento(nodoAux)
        else:
            pila.agregarElemento(Nodo(lista[i], None, None))
    return pila.sacarElemento()


def imprimirArbolPostfijo(arbol):
    if arbol != None:
        imprimirArbolPostfijo(arbol.izq)
        imprimirArbolPostfijo(arbol.der)
        print arbol.valor


def ingresarArbol():
    while True:
        opcion = \
            raw_input('Desea ingresar una expresion matematica en posfijo: (Y/N)'
                      )
        if opcion == 'Y':
            cadena = leerCadena()
            print 'cadena' , cadena 
            pila = Pila()
            nodo = crearArbol(cadena, pila)
            print 'Resultado operacion: ', evaluar(nodo)
        if opcion == 'N':
            break
    imprimirDatos()
    return None


def main():
    ingresarArbol()
    return None


main()

                        
