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
def newCatalog():
    estructura= "ARRAY_LIST"
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
    artwork["Classification"]= obra["Classification"]
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
            if lt.isEmpty(obrasArtista)==False: 
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
def cmpArtworkByDate(artwork1, artwork2):
    fecha1= (artwork1['Date'])
    fecha2=(artwork2['Date'])
    temp=False
    if fecha1=="" and fecha2 =="":
        temp= False
    elif fecha1=="" and fecha2 !="":
        temp= False
    elif fecha2=="" and fecha1 !="":
        temp= True
    else:
        temp= int(fecha1)<int(fecha2)
    return temp
def cmpArtworktByPrice(obra1, obra2):
    precio1= float(obra1["precio"])
    precio2=float(obra2["precio"])
    return precio1<precio2

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
def sortArtworksByDate(lista):
    lista_ordenada= lista.copy()
    lista_ordenada= me.sort(lista_ordenada,cmpArtworkByDate)
    return lista_ordenada

def sortArtworksByPrice(listaog):
    lista= listaog.copy()
    me.sort(lista,cmpArtworktByPrice)
    return lista

def cmpfunction_nacionalidades (num1,num2):
    return num1>num2
def RankingCountriesByArtworks (catalog):
    #req4
    obras=catalog["obras"]
    dict_nacionalidades= {}
    for n in lt.iterator(obras):
        artista= n["Artists"]
        for nacionalidad in lt.iterator(artista):
            nationality=nacionalidad["Nationality"]
            if nationality not in dict_nacionalidades:
                dict_nacionalidades[nationality]=lt.newList("ARRAY_LIST")
                lt.addLast(dict_nacionalidades[nationality],1)
                lt.addLast(dict_nacionalidades[nationality],n)
                
                
            else:
                element=lt.getElement(dict_nacionalidades[nationality],1)+1
                lt.changeInfo(dict_nacionalidades[nationality],1,element)
                lt.addLast(dict_nacionalidades[nationality],n["Title"])
    num=1
    lista=lt.newList("ARRAY_LIST")
    for i in range (10):
        for key,value in dict_nacionalidades.items():
            value=lt.getElement(value,1)
            if value>num:
                num=value
                nombre=key
        lista[nombre]=lt.getElement(dict_nacionalidades[nationality],2)
        

    return (lista)


#Requisito 5#
def AsignarPrecio(object):
    #considerar datos vacios revisar reglas#
    m3=-1
    if object["Width (cm)"]!="" and object["Height (cm)"]!="" and object["Depth (cm)"]!="":
        m3= ((float(object["Width (cm)"]))*(float(object["Height (cm)"]))*(float(object["Depth (cm)"])))
        m3= m3/1000000
    m2=-1
    if object["Width (cm)"]!="" and object["Height (cm)"]!="":
        m2=(float(object["Width (cm)"]))*(float(object["Height (cm)"]))
        m2=m2/10000
    precio=-1
    preciom3= 0
    preciom2= 0
    precioKg= 0
    if object["Weight (kg)"] != "":
        precioKg= 72* float(object["Weight (kg)"])
    if m3>0:
        preciom3= 72* float(m3)
    if m2>0:
        preciom2= 72* float(m2)
    if preciom3 ==0 and preciom2==0 and precioKg==0:
        precio=48
    elif preciom2> preciom3 and preciom2> precioKg:
        precio= preciom2
    elif preciom3> preciom2 and preciom3> precioKg:
        precio= preciom3
    elif precioKg> preciom2 and precioKg> preciom3:
        precio= precioKg 
    return (precio)

def OrdenarDepartamentoAsignarPrecioyPeso(catalogo, departamento):
    obrasPorDepartamento= lt.newList()
    lista_artwork= catalogo["obras"]
    listaR = lt.newList("ARRAY_LIST") #la lista R va a tener peso,precio,listaobras#
    precio=0
    peso=0
    for obra in lt.iterator (lista_artwork):
        if obra["Department"]== departamento:
            obra["precio"]=AsignarPrecio(obra)
            lt.addLast(obrasPorDepartamento,obra)
            precio+=float(obra["precio"])
            if obra["Weight (kg)"] != "":
                peso+=float(obra["Weight (kg)"])
    lt.addLast(listaR, peso)
    lt.addLast(listaR, round(precio,3))
    lt.addLast(listaR, obrasPorDepartamento)
    return listaR

def cmpArtworkPorPrecio(Artwork1,Artwork2):
    precio1=Artwork1["precio"]
    precio2=Artwork2["precio"]
    return precio1< precio2
    





