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


from DISClib.DataStructures.arraylist import size
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """"
    se genera un catalogo con dos listas,
    se utilizó array list en vez de single linked porque hasta el momento 
    solo se va a acceder a los elementos por posición lo que resulta o(1) con array 
    y o(n) con single linked

    """
    catalog = {'obras': None,
               'artistas': None,
               }

    catalog['artistas'] = lt.newList('ARRAY_LIST', cmpfunction=compareArtistId)
    catalog['obras'] = lt.newList('ARRAY_LIST', cmpfunction=compareObraId)

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

#TODO hacer funciones para agregar datos
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
    for pos in range (tam2,tam1):
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

# Funciones de ordenamiento