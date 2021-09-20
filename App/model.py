"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import  size
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as sh
from DISClib.Algorithms.Sorting import mergesort as me
from DISClib.Algorithms.Sorting import quicksort as qu
from datetime import datetime
import time
assert cf
import operator



# Construccion de modelos
def newCatalog(estructura):

    catalog = {'obras': None,
               'artistas': None,
               }

    catalog['artistas'] = lt.newList(estructura, cmpfunction=compareArtistId)
    catalog['obras'] = lt.newList(estructura, cmpfunction=compareObraId)

    return catalog

# Funciones para agregar informacion al catalogo

def addObra(catalog, obra):
    """
    Se adiciona la obra a la lista de obras
    """
    lt.addLast(catalog['obras'], obra)


def addArtist(catalog, artist):
    """
    Adiciona un artista a lista de artistas, 
    """
    lt.addLast(catalog['artistas'], artist)


# Funciones para creacion de datos


# Funciones de consulta

def getLastxElements(lista,number):
    """
    Retorna los x ultimos elementos dado una LISTA"
    """
    elements= lista
    lastelements= lt.newList("ARRAY_LIST")
    tamañoLista= lt.size(elements)
    tam2=tamañoLista-(number-1)
    for pos in range (tam2,tamañoLista+1):
        new=lt.getElement (elements,pos)
        lt.addLast (lastelements,new)
    return lastelements
def getFirstxElements(lista,number):
    """
    Retorna los x primeros elementos dado una LISTA"
    """
    elements= lista
    firstlements= lt.newList("ARRAY_LIST")
    for pos in range (1,number+1):
        new=lt.getElement (elements,pos)
        lt.addLast (firstlements,new)
    return firstlements
# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtistId(artist1, artist2):
    if artist1["ConstituentID"] < artist2["ConstituentID"]:
        return -1 
    elif artist1["ConstituentID"] == artist2["ConstituentID"]:
        return 0
    else: 
        return 1
def compareObraId(obra1, obra2):
    if obra1["ObjectID"] < obra2["ObjectID"]:
        return -1 
    elif obra1["ObjectID"] == obra2["ObjectID"]:
        return 0
    else: 
        return 1

def cmpArtistByDate(artist1, artist2):
    #req 1, re utilizò la librerìa datetime
    ##tomaremos vacios como automaticamente menor
    fecha1= (artist1['BeginDate'])
    fecha2=(artist2['BeginDate'])
    temp=False
    if fecha1=="":
        fecha1=0 
    if fecha2=="":
        fecha2=0
    temp= int(fecha1)<int(fecha2)
    return temp

def cmpArtworkByDateAcquired(artwork1, artwork2):
    #req 2, re utilizò la librerìa datetime#
    fecha1= str(artwork1['DateAcquired'])
    fecha2=str(artwork2['DateAcquired'])
    if fecha1=="":
        fecha1="0001-01-01"
    if fecha2=="":
        fecha2="0001-01-01"
    
    date1 = datetime.strptime(fecha1, "%Y-%m-%d")
    date2 = datetime.strptime(fecha2, "%Y-%m-%d")
    return date1<date2
 

# Funciones de ordenamiento
def sortArtistInDateRange(catalog, date1,date2):
    # req1
    date1 = int(date1)
    date2 = int(date2)
    #primero ordeno toda la lista#
    start_time = time.process_time()
    listaOrdenada= me.sort((catalog['artistas']),cmpArtistByDate)
    listaEnRango = lt.newList()
    for i in lt.iterator(listaOrdenada):
        date= int(i['BeginDate'])
        if date != 0 and date >= date1 and date<=date2:
            lt.addLast(listaEnRango, i)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000   
    return (listaEnRango)
    
def sortArtworksByDateAcquired(lista):
    sub_list =(lista)
    lista_ordenada= ins.sort(sub_list,cmpArtworkByDateAcquired)
    return lista_ordenada

def subslitArtworksInRange(lista,inicial,final):
    inicial=datetime.strptime(str(inicial),"%Y-%m-%d")
    final=datetime.strptime(str(final),"%Y-%m-%d")
    final_list= lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista):
        date=i['DateAcquired']
        if date=="":
            date="0001-01-01"
        date_format=datetime.strptime(str(date),"%Y-%m-%d")
        if date_format<= final and date_format>=inicial:
                lt.addLast(final_list,i)
    return (final_list)

def NumberOfPurchase (lista_ordenada):
    num_purchase=0
    for n in lt.iterator(lista_ordenada):
        credit_line= n["Creditline"]
        if credit_line=="Purchase":
            num_purchase+=1
    return num_purchase
    
def RankingCountriesByArtworks (catalog,obras):
    #req4
    lista_obras= catalog["obras"]
    dict_obras={}
    lista_artistas=catalog["artistas"]
    for i in range (lt.size(obras)):
        for n in range (lt.size(lista_obras)):
            if obras[i]==lista_obras[n]["Título"]:
                dict_obras[obras[i]]=lista_obras[n]["ConstituentID"]
    dict_nacionalidades={}
    for valor in dict_obras.values:
       for j in range(lt.size(lista_artistas)):
           pos=lista_artistas[j]
           if valor== pos["ConstituentID"]:
               nacionalidad=pos["nacionalidad"]
               if nacionalidad not in dict_nacionalidades:
                   dict_nacionalidades[nacionalidad]=1
               else:
                   dict_nacionalidades[nacionalidad]+=1
    dict_ordenado=sorted(dict_nacionalidades.items(),key=operator.itemgetter(1), reverse=True)
    return (dict_ordenado)


#Requisito 5#
def AsignarPrecio(artwork):
    #considerar datos vacios revisar reglas#
    return None
def AsignarPeso(artwork):
    #considerar datos vacios revisar reglas#
    return None
def OrdenarDepartamentoAsignarPrecioyPeso(catalogo, departamento):
    obrasPorDepartamento= lt.newList()
    #recorrido que revise el departamento y añada la obra a la lista si es el dep y asigna precio#
    return obrasPorDepartamento
def cmpArtworkPorPrecio(Artwork1,Artwork2):
    return None
def OrdenarPorPrecio(lista):
    return None 




