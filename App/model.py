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

def getLastxElements(catalog,category,number):
    """
    Retorna los 3 ultimos elementos dado un catalogo (catalog), categoría ("artistas" o  "obras") y una cantidad de posiciones (3)
    tienes que generar una lista donde almacenes los elementos a los que accedes por posición
    ideas:puedes usar get.element para obtener el elemento y size para obtener ultimas tres posiciones
    """
    elements= catalog[category]
    lastelements= lt.newList("ARRAY_LIST")
    tam1= lt.size(elements)
    tam2=tam1-number
    for pos in range (tam2,tam1+1):
        new=lt.getElement (elements,pos)
        lt.addLast (lastelements,new)
    return lastelements

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

def sortArtworksByDateAcquired(catalog,inicial,final):
    # req2
    inicial=datetime.strptime(str(inicial),"%Y-%m-%d")
    final=datetime.strptime(str(final),"%Y-%m-%d")
    sub_list =(catalog['obras'])
    lista_ordenada= ins.sort(sub_list,cmpArtworkByDateAcquired)
    final_list= lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista_ordenada):
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

    




