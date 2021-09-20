﻿"""
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
 """

import config as cf
import model
import csv
from datetime import datetime

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de obras
def initCatalog(estructura):
    catalog = model.newCatalog(estructura)
    return catalog
# Funciones para la carga de datos
def loadData(catalog):
    loadArtistas(catalog)
    loadObras(catalog)

def loadArtistas(catalog):
    """
    Carga todos los artistas del archivo y la agrega a la lista de obras en el catalogo general
    """
    Artistfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(Artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadObras(catalog):
    """
    Carga todas las obras del archivo y la agrega a la lista de obras en el catalogo general
    """
    Obrasfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(Obrasfile, encoding='utf-8'))
    for obra in input_file:
        model.addObra(catalog, obra)

# Funciones de ordenamiento
def sortArtworksByDateAcquired(catalog): 
    return model.sortArtworksByDateAcquired(catalog)
def subslitArtworksInRange(lista,inicial,final):
    return model.subslitArtworksInRange(lista,inicial,final)
def NumberOfPurchase (lista_ordenada):
    return model.NumberOfPurchase(lista_ordenada)

def sortArtistInDateRange(catalog, date1,date2):
    return model.sortArtistInDateRange(catalog, date1,date2)

def RankingCountriesByArtworks(catalog,obras):
    return model.RankingCountriesByArtworks(catalog,obras)
# Funciones de consulta sobre el catálogo
def getLastxElements(list, number):
    lastElements = model.getLastxElements(list, number)
    return lastElements
def getFirstxElements(list, number):
    lastElements = model.getFirstxElements(list, number)
    return lastElements
