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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import  iterator, newList, size
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

def addArtist(catalog, artista):
    """
    Adiciona un artista a lista de artistas, se hace un diccionario vacio y luego 
    se llena con los atributos que necesitamos en el reto, tambien se asigna un espacio
    para las obras con una lista vacia.
    """
    artist= {}
    artist["ConstituentID"]= artista["ConstituentID"]
    artist["DisplayName"]= artista["DisplayName"]
    artist["BeginDate"]= artista["BeginDate"]
    artist["EndDate"]= artista["EndDate"]
    artist["Nationality"]= artista["Nationality"]
    artist["Gender"]= artista["Gender"]
    artist["Artworks"]= lt.newList("ARRAY_LIST",cmpfunction= compareObraId)
    lt.addLast(catalog['artistas'], artist)

def addObra(catalog, obra):
    """
    Adiciona una obra a lista de obras, se hace un diccionario vacio y luego 
    se llena con los atributos que necesitamos en el reto, tambien se asigna un espacio
    para las obras con una lista vacia.
    """
    artwork={}
    artwork["ObjectID"]= obra["ObjectID"]
    artwork["Title"]= obra["Title"]
    artwork["Medium"]= obra["Medium"]
    artwork["Date"]= obra["Date"]
    artwork["DateAcquired"]= obra["DateAcquired"]
    artwork["Department"]= obra["Department"]
    artwork["CreditLine"]= obra["CreditLine"]
    artwork["Dimensions"]= obra["Dimensions"]
    artwork["Depth (cm)"]= obra["Depth (cm)"]
    artwork["Diameter (cm)"]= obra["Diameter (cm)"]
    artwork["Height (cm)"]= obra["Height (cm)"]
    artwork["Length (cm)"]= obra["Length (cm)"]
    artwork["Weight (kg)"]= obra["Weight (kg)"]
    artwork["Width (cm)"]= obra["Width (cm)"]
    artwork["Seat Height (cm)"]= obra["Seat Height (cm)"]
    artwork["Artists"]= lt.newList("ARRAY_LIST",cmpfunction=compareArtistId)
    """en obras los artistas estan como constituente id, en un formato [,] separado por comas, 
    vamos a obtener de este formato el int del ID para cada artista y lo almacenaremos en una lista
    primero quitamos los corchetes del string y luego haremos la lista usando , como separador
    """
    codigosArtistas= obra['ConstituentID']
    codigosArtistas= codigosArtistas.replace("[","")
    codigosArtistas= codigosArtistas.replace("]","")
    codigosArtistas= codigosArtistas.replace(" ","")
    codigosArtistas= codigosArtistas.split(",")
    artwork["ConstituentID"]= codigosArtistas
    """
    vamos a hacer la conexión de referencias entre obras y artistas
    al artista se le adiciona la info de la obra a la lista artworks
     y viceversa con los artistas a la obra
    """
    #TODO pregunta cupi#
    for ID in codigosArtistas:
        ID= int(ID)
        for artista in lt.iterator(catalog["artistas"]):
            IDArtista=(artista["ConstituentID"]).replace(" ","")
            IDArtista= int(IDArtista)
            if ID == IDArtista:
                lt.addLast(artista["Artworks"],artwork)
                lt.addLast(artwork["Artists"],artista)
                
    lt.addLast(catalog['obras'], artwork)

# Funciones de consulta
def buscarTecnicaMasRep(dicTecnicas):
        TecnicaMas= " "
        size_mayor=0
        for tecnica in dicTecnicas:
            size= lt.size(dicTecnicas[tecnica]["obras"])
            if size>size_mayor:
                size_mayor= size
                TecnicaMas= tecnica
        return TecnicaMas
def ObrasPorArtistaPorTecnica(catalogo,nombre):
    artistas= catalogo["artistas"]
    for artista in lt.iterator(artistas):
        if nombre == artista["DisplayName"]:
            obrasArtista= artista["Artworks"]
            Tecnicas={}
            if lt.size(obrasArtista)> 0: 
                for obra in lt.iterator(obrasArtista):
                    tecnica= obra["Medium"]
                    if tecnica != "":
                        if tecnica not in Tecnicas:
                            Tecnicas[tecnica]={}
                            Tecnicas[tecnica]["nombre"]= tecnica
                            Tecnicas[tecnica]["obras"]= lt.newList("ARRAY_LIST")
                            lt.addLast(Tecnicas[tecnica]["obras"],obra)
                        else:
                            lt.addLast(Tecnicas[tecnica]["obras"],obra)
                break
        else:
            obrasArtista=None
            Tecnicas=None
    return (obrasArtista,Tecnicas) 
 
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
    #primero ordeno la lista#
    listaOrdenada= me.sort((catalog['artistas']),cmpArtistByDate)
    listaEnRango = lt.newList("ARRAY_LIST") #porque luego se accede por pos#s
    for i in lt.iterator(listaOrdenada):
        date= int(i['BeginDate'])
        if date != 0 and date >= date1 and date<=date2:
            lt.addLast(listaEnRango, i)
    return (listaEnRango)

def sortArtworksandRange(lista,inicial,final):
    inicial=datetime.strptime(str(inicial),"%Y-%m-%d")
    final=datetime.strptime(str(final),"%Y-%m-%d")
    listaEnRango= lt.newList("ARRAY_LIST")
    purchased=0
    for i in lt.iterator(lista):
        date=i['DateAcquired']
        if date=="":
            date="0001-01-01"
        date_format=datetime.strptime(str(date),"%Y-%m-%d")
        if date_format<= final and date_format>=inicial:
                lt.addLast(listaEnRango,i)
                credit_line= str(i["CreditLine"]).lower()
                if ("Purchase").lower() in credit_line or ("Purchased").lower() in credit_line :
                    purchased+=1
    lista_ordenada= ins.sort(listaEnRango,cmpArtworkByDateAcquired)
    return (lista_ordenada,purchased)

   
def RankingCountriesByArtworks (catalog,obras):
    #req4
    lista_artistas=catalog["artistas"]
    dict_nacionalidades= {}
    for i in obras:
        for n in lt.iterator(lista_artistas):
            if i in n["Artworks"]:
                nacionalidad= n["Nationality"]
                if nacionalidad not in dict_nacionalidades:
                    dict_nacionalidades[nacionalidad]=1
                else:
                    dict_nacionalidades[nacionalidad]+=1
    return (dict_nacionalidades)


#Requisito 5#
def AsignarPrecio(object):
    #considerar datos vacios revisar reglas#
    m3=-1
    if object["Width (cm)"]!="" and object["Height (cm)"]!="" and object["Depth (cm)"]!="":
        m3= ((object["Width (cm)"]/100)*(object["Height (cm)"]/100)*(object["Depth (cm)"]/100))
    m2=-1
    if object["Width (cm)"]!="" and object["Height (cm)"]!="":
        m2=(object["Width (cm)"]/100)*(object["Height (cm)"]/100)
    kg=object["Weight (kg)"]
    precio=-1
    if kg!="" and m3!=-1 and m2!=-1:
        if  72000*kg> precio:
            precio= 72000*kg
        if 72000*m3>precio:
            precio=72000*m3
        if 72000*m2>precio:
            precio=72000*m2
    elif kg!="" and m3!=-1 and m2==-1:
        if  72000*kg> precio:
            precio= 72000*kg
        if 72000*m3>precio:
            precio=72000*m3
    elif kg!="" and m2!=-1 and m3==-1:
        if  72000*kg> precio:
            precio= 72000*kg
        if 72000*m2>precio:
            precio=72000*m2
    elif kg=="" and m2!=-1  and 3!=-1:
        if 72000*m2>precio:
            precio=72000*m2
        if 72000*m3>precio:
            precio=72000*m2
    else:
        precio= 48000
    return precio

def OrdenarDepartamentoAsignarPrecioyPeso(catalogo, departamento):
    obrasPorDepartamento= lt.newList()
    lista_artwork= catalogo["artistas"]
    dict_rta={}
    precio=0
    peso=0
    for i in lt.iterator (lista_artwork):
        if i["Department"]== departamento:
            i["precio"]=AsignarPrecio(i)
            lt.addLast(obrasPorDepartamento,i)
            precio+=i["precio"]
            peso+=i["Weight (kg)"]
    dict_rta["Peso Total"]=peso
    dict_rta["Precio Total"]=precio
    dict_rta["lista artworks"]=obrasPorDepartamento
    return dict_rta

def cmpArtworkPorPrecio(Artwork1,Artwork2):
    precio1=Artwork1["precio"]
    precio2=Artwork2["precio"]
    return precio1< precio2
    
def OrdenarPorPrecio(dict_rta):
    lista=dict_rta["lista artworks"]
    return me.sort(lista,cmpArtworkPorPrecio)




