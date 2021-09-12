"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from datetime import datetime
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido")
    print("1-Cargar información en el catálogo, y escoger el tipo de estructura")
    print("2-Listar cronológicamente los artistas")
    print("3-Listar cronológicamente las adquisiciones ")
    print("4-Clasificar las obras de un artista por técnica")
    print("5-Clasificar las obras por la nacionalidad de sus creadores ")
    print("6-Transportar obras de un departamento ")
    print("7-Proponer una nueva exposición en el museo ")
    print("0-Salir ")
 
def initCatalog(estructura):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(estructura)

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    return controller.loadData(catalog)

#Funciones para imprimir#
def printartists(artistas):
    size = lt.size(artistas)
    if size:
        for artista in lt.iterator(artistas):
            print('ID Constituente: ' + artista["ConstituentID"] + '  Nombre: ' +
                  artista["DisplayName"] + ' Bio: ' + artista["ArtistBio"]+ 
                  ' Nacionalidad: '+ artista["Nationality"]+ ' Género: '+artista["Gender"] +
                  ' Fecha de inicio/Fecha fin: '+ artista["BeginDate"]+'/'+ artista["EndDate"]+
                 " Wiki QID: " +artista["Wiki QID"]+ ' ULAN: '+artista["ULAN"])
    else:
        print('No se han cargado artistas')

def printobras(obras):
    size = lt.size(obras)
    if size:
        for obra in lt.iterator(obras):
            print('ID: ' + obra["ObjectID"] + ' Título: ' + obra["Title"] + 
            ' ID Constituente: ' + obra["ConstituentID"] +  ' Fecha: ' + obra["Date"] +
             ' Medio: ' + obra["Medium"] + ' Dimensiones: ' + obra["Dimensions"] + 
             ' CreditLine: ' + obra["CreditLine"] + 'Número de Acceso' + obra["AccessionNumber"] +
             ' Clasificación' + obra["Classification"] + ' Departamento: ' + obra["Department"] +
             'Fecha de Adquisción' + obra["DateAcquired"])       
    else:
        print('No se han cargado obras')
"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        estructura= input('Seleccione una opción:\n 1.ARRAY_LIST\n 2.LINKED_LIST\n')
        if int(estructura)== 1:
            estructura="ARRAY_LIST"
        elif int(estructura)== 2:
            estructura="LINKED_LIST"
        else:
            print("No es una opciòn")
            sys.exit(0)
        print("Cargando información de los archivos ....")
        catalog = initCatalog(estructura)
        loadData(catalog)
        print('Obras cargadas: ' + str(lt.size(catalog['obras'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artistas'])))
        print('Ultimos 3 Artistas cargados: ')
        printartists(controller.get3lastartists(catalog))
        print('\nUltimas 3 Obras cargadas:')
        printobras(controller.get3lastobras(catalog))
        
    elif int(inputs[0]) == 3:
        size = input("Indique tamaño de la muestra: ")
        algoritmo= input('Seleccione tipo de algoritmo de ordenamiento iterativo:\n'+
                    ' 1.Insertion\n 2.Shell\n 3.Merge\n 4.Quick Sorts\n')
        if int(algoritmo)== 1:
            algoritmo="Insertion"
        elif int(algoritmo)== 2:
            algoritmo="Shell"
        elif int(algoritmo)== 3:
            algoritmo="Merge"
        elif int(algoritmo)== 4:
            algoritmo="quicksort"
        else:
            print("No es una opciòn")
            sys.exit(0)
        #TODO incluir el tipo de algoritmo en la respuesta en controller
        #  y module, aqui solo inclui las opciones en el menù pero no hacen nada#
        result = controller.sortArtworksByDateAcquired(catalog, int(size))
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result))
    elif int(inputs[0]) >= 3 or int(inputs[0]) ==2:
        print ("Lo sentimos, Requerimiento no disponible todavía")
        pass
    else:
        sys.exit(0)
sys.exit(0)
