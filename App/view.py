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
from datetime import datetime
import time
assert cf
default_limit = 1000
sys.setrecursionlimit(default_limit*10)


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
def printartists(artistas, incluirObras):
    size = lt.size(artistas)
    if size:
        for artista in lt.iterator(artistas):
            print("____________________________________________---")
            print(' Nombre: ' +artista["DisplayName"] + ' Fecha de inicio: '+ 
                    artista["BeginDate"]+' Fecha fin: '+ artista["EndDate"]+
                  ' Nacionalidad: '+ artista["Nationality"]+ ' Género: '+artista["Gender"])
            if incluirObras:
                obras=artista["Artworks"]
                if lt.size(obras)>0:
                    print("    Obras del artista:")
                    printobras(obras)
                else:
                    print("No")
    else:
        print('No se han cargado artistas')

def printobras(obras):
    size = lt.size(obras)
    if size:
        for obra in lt.iterator(obras):
            print("--------------------------------------------")
            print( ' Título: ' + obra["Title"] + ' Fecha: ' + obra["DateAcquired"] +
             ' Medio: ' + obra["Medium"] + ' Dimensiones: ' + obra["Dimensions"] +
             " Artistas:" )
    else:
        print('No se han cargado obras')
def printPrimerosyUltimosartistas(lista):
    if lt.size(listaEnRango)>3:
            primeros= lt.subList(listaEnRango,1,3)
            ultimos= lt.subList(listaEnRango,lt.size(listaEnRango)-2,3)
            print("\n* Primeros 3 artisas")
            printartists(primeros,True)
            print("\n* Utlimos 3 artisas")
            printartists(ultimos,False)
    elif lt.size(listaEnRango)<=3:
            print("Como solo hay 3 o menos artistas, estos son:")
            printartists(listaEnRango,False)
def printPrimerosyUltimosobras(lista):
    if lt.size(listaEnRango)>3:
            primeros= lt.subList(listaEnRango,1,3)
            ultimos= lt.subList(listaEnRango,lt.size(listaEnRango)-2,3)
            print("\n* Primeras 3 obras ")
            printobras(primeros)
            print("\n* Utlimos 3 obras ")
            printobras(ultimos)
    elif lt.size(listaEnRango)<=3:
            print("Como solo hay 3 o menos obras, estas son:")
            printobras(listaEnRango)
def printUltimos5obras(lista,tipo):
    if lt.size(listaEnRango)>5:
            ultimos= lt.subList(listaEnRango,lt.size(listaEnRango)-4,5)
            print("Obras más "+str(tipo))
            printobras(ultimos)
    elif lt.size(listaEnRango)<=5:
            print("Como solo hay 5 o menos obras, estos son:")
            printobras(listaEnRango)

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        start_time = time.process_time()
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
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))

    elif int(inputs[0]) == 2:
        start_time = time.process_time()
        date1 = input("Indique año inicial (formato YYYY): ")
        date2 = input("Indique año final (formato YYYY): ")
        listaEnRango= controller.sortArtistInDateRange(catalog,date1,date2)
        if lt.size(listaEnRango)==0:
            print("No hay artistas nacidos en el rango")
        else:
            print("Hay "+ str(lt.size(listaEnRango))+ " artistas que nacieron entre "+ str(date1) +" y "+ str(date2))
            printPrimerosyUltimosartistas(listaEnRango)
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))

    elif int(inputs[0]) == 3:
        start_time = time.process_time()
        inicial= input("Indique la fecha inicial: ")
        final= input("Indique la fecha final: ")
        listaOrdenada = controller.sortArtworksByDateAcquired(catalog["obras"])
        listaEnRango= controller.subslitArtworksInRange(listaOrdenada,inicial,final)
        numPurchased= 0 ###TODO#############
        if lt.size(listaEnRango)==0:
            print("No hay obras en el rango")
        else:
            print("Hay "+ str(lt.size(listaEnRango))+ " obras  entre "+ str(inicial) +" y "+ str(final))
            printPrimerosyUltimosobras(listaEnRango)
            print("Hay "+ str(numPurchased)+ " obras adquiridas por compra")
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))
        
    elif int(inputs[0]) == 4:
        start_time = time.process_time()
        nombre= input("Indique el nombre del artista: ")
        (obrasArtista, Tecnicas)= controller.ObrasPorArtistaPorTecnica(catalog,nombre)
        Tecnica= controller.buscarTecnicaMasRep(Tecnicas)
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))
    elif int(inputs[0])==5:
        start_time = time.process_time()
        obras=catalog["obras"]
        nacionalidades=controller.RankingCountriesByArtworks(catalog,obras)
        print("El top 10 de los países en el MoMa son: ")
        num=0
        for i in nacionalidades:
            print(str(i)+ ":"+ str(nacionalidades[i]))
            num+=1
            if num==10:
                break
        print ("La nacionalidad con mayor número de obras: ")
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))
    elif int(inputs[0])==6:
        start_time = time.process_time()
        departamento= input("Por favor ingrese el nombre del departamento:") 
        ObrasporDepartamento= controller.OrdenarDepartamentoAsignarPrecioyPeso(catalog, departamento)
        ObrasPorFecha= controller.sortArtworksByDateAcquired(ObrasporDepartamento)
        ObrasPorPrecio= controller.OrdenarPorPrecio(ObrasporDepartamento)
        print("El total de obras en el departamento "+ str(departamento)+ "es de: "+ lt.size(ObrasporDepartamento))
        print("5 Obras más antiguas a trasportar")
        printUltimos5obras(ObrasPorFecha," antiguas ")
        print("5 Obras más caras a transportar")
        printUltimos5obras(ObrasPorPrecio," cotosas ")
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))
    elif int(inputs[0]) >= 6 :
        print ("Lo sentimos, Requerimiento no disponible")
        pass
    else:
        sys.exit(0)
sys.exit(0)
