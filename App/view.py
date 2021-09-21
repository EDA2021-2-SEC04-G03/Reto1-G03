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
            print(' Nombre: ' +artista["DisplayName"] + ' Fecha de inicio: '+ 
                    artista["BeginDate"]+' Fecha fin: '+ artista["EndDate"]+
                  ' Nacionalidad: '+ artista["Nationality"]+ ' Género: '+artista["Gender"]+
                  " Obras" )
    else:
        print('No se han cargado artistas')

def printobras(obras):
    size = lt.size(obras)
    if size:
        for obra in lt.iterator(obras):
            print( ' Título: ' + obra["Title"] + ' Fecha: ' + obra["DateAcquired"] +
             ' Medio: ' + obra["Medium"] + ' Dimensiones: ' + obra["Dimensions"] +
             " Artistas:" + str(obra["Artists"]))       
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
    elif int(inputs[0]) == 2:
        date1 = input("Indique año inicial (formato YYYY): ")
        date2 = input("Indique año final (formato YYYY): ")
        listaEnRango= controller.sortArtistInDateRange(catalog,date1,date2)
        print("Hay "+ str(lt.size(listaEnRango))+ " artistas que nacieron entre "+ str(date1) +" y "+ str(date2))
        if lt.size(listaEnRango)>3:
            primeros= lt.subList(listaEnRango,1,3)
            ultimos= lt.subList(listaEnRango,lt.size(listaEnRango)-3,3)
            print("Utlimos 3 artistas")
            printartists(ultimos)
            print("Primeros 3 artistas")
            printartists(primeros)
        elif lt.size(listaEnRango)<=3:
            print("Como solo hay 3 o menos artistas, estos son:")
            printartists(listaEnRango)
    elif int(inputs[0]) == 3:
        inicial= input("Indique la fecha inicial: ")
        final= input("Indique la fecha final: ")
        listaOrdenada = controller.sortArtworksByDateAcquired(catalog["obras"])
        listaEnRango= controller.subslitArtworksInRange(listaOrdenada,inicial,final)
        num_obras= lt.size(listaEnRango)
        #num_purchase= controller.NumberOfPurchase(num_obras)
        print("Primeras 3 obras")
        printobras(controller.getFirstxElements(listaEnRango,3))
        print("Utlimas 3 obras")
        printobras(controller.getLastxElements(listaEnRango,3))
        #print("Número de obras adquiridas por compra: "+ str(num_purchase))
    elif int(inputs[0]) == 4:
        nombre= input("Indique el nombre del artista: ")
        
    elif int(inputs[0])==5:
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
    elif int(inputs[0])==6:
        departamento= input("Por favor ingrese el nombre del departamento:") 
        ObrasporDepartamento= controller.OrdenarDepartamentoAsignarPrecioyPeso(catalog, departamento)
        ObrasPorFecha= controller.sortArtworksByDateAcquired(ObrasporDepartamento)
        ObrasPorPrecio= controller.OrdenarPorPrecio(ObrasporDepartamento)
        print("El total de obras en el departamento "+ str(departamento)+ "es de: "+ lt.size(ObrasporDepartamento))
        print("5 Obras más antiguas a trasportar")
        printobras(controller.getLastxElements(ObrasPorFecha,5))
        print("5 Obras más caras a transportar")
        printobras(controller.getLastxElements(ObrasPorPrecio,5))
    elif int(inputs[0]) >= 6 :
        print ("Lo sentimos, Requerimiento no disponible")
        pass
    else:
        sys.exit(0)
sys.exit(0)
