# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:38:40 2021

@author: MartinXD
"""

#---------Librerias---------------------------

import requests
from bs4 import BeautifulSoup
import ExportDatExcel2
import sendMail

#------------------------Funciones----------------------------------------

def buscar(text, c):
    
    newText = ""
    encontrada = False
    flag = False
    for t in text:
        if t == c or encontrada:
            newText = newText + t
            encontrada = True
            if t == ' ' or flag:
                newText = newText + ''
                flag = True
    if not encontrada:
        return text
    return newText

def select(elem, dic, datos, lis):
    
    for dato in datos:
        texto = dato.find(elem, dic)
        texto = buscar(texto.text, "$")
        lis.append(texto)

def convertirAEntero(string):
    
    integer = int(string)
    
    return integer


def limpiarTexto(text):
    
    quitar = "$"
    textNew = ""
    flag = True
    for q in quitar:
        text = text.replace(q, '')
    
    for l in text:
        if(l != ',' and flag):
            textNew = textNew + l
        else:
            textNew = textNew + ''
            flag = False
            
    return textNew

def cargarDiccionario(dic, dataKey, dataValue):
    
    for i in range(len(dataKey)):
        """
        if isinstance(dataKey[i], str):
            textoClave = limpiarTexto(dataKey[i])
        else:
            textoClave = limpiarTexto(dataKey[i].text)
        if isinstance(dataValue[i], str):
            textoValor = limpiarTexto(dataValue[i])
        else:
            textoValor = limpiarTexto(dataValue[i].text)
            
        valorEntero = convertirAEntero(textoValor)
        """
        if isinstance(dataKey[i], str):
            dic[dataKey[i]] = dataValue[i].text
        elif isinstance(dataValue[i], str):
            dic[dataKey[i].text] = dataValue[i]
        else:
            dic[dataKey[i].text] = dataValue[i].text

#----------------------Main------------------------------------

#Levanto las paginas utilizando la libreria requests
page1 = requests.get("https://www.jumbo.com.ar/coca-cola/coca%20cola")
page2 = requests.get("https://diaonline.supermercadosdia.com.ar/bebidas/coke-cocacola/coca%20cola?PS=15")
page3 = requests.get("https://www.cotodigital3.com.ar/sitios/cdigi/browse/brand-coca-cola/_/N-5ff815?Dy=1&Nf=product.startDate%7CLTEQ%2B1.6176672E12%7C%7Cproduct.endDate%7CGTEQ%2B1.6176672E12&Nr=AND(product.sDisp_200%3A1004%2Cproduct.language%3Aespa%C3%B1ol%2COR(product.siteId%3ACotoDigital))")
page4 = requests.get("https://www.walmart.com.ar/coca-cola")

"""Creo variables de tipo BeautifulSoup, donde le paso como parametros el 
 contenido de la pagina (el HTML) y el tipo de estructura a parcelar""" 
soup1 = BeautifulSoup(page1.content, 'html.parser')
soup2 = BeautifulSoup(page2.content, 'html.parser')
soup3 = BeautifulSoup(page3.content, 'html.parser')
soup4 = BeautifulSoup(page4.content, 'html.parser')


#Creo dos listas auxiliares
lisAux1 = list()
lisAux2 = list()

#Creo los diccionarios que almacenaran los datos extraidos de cada pagina
diccioJumbo = {}
diccioDia = {}
diccioCoto = {}
diccioWalmart = {}

"""En las variables voy a almacenar la busqueda de todas las etiquetas dentro
 el HTML con tal criterio especificado en la funcion findAll()"""

#---------------jumbo---------------------------
jumboNameProduct = soup1.findAll("a", {"class":"product-item__name"})
jumboPriceProduct = soup1.findAll("span", {"class":"product-prices__value product-prices__value--best-price"})
cargarDiccionario(diccioJumbo , jumboNameProduct , jumboPriceProduct)

#--------------dia-----------------------------
diaNameProduct = soup2.findAll("div", {"class":"product-name"})
diaPriceProduct = soup2.findAll("span", {"class":"best-price"})
select("a", {}, diaNameProduct , lisAux1)
cargarDiccionario(diccioDia, lisAux1, diaPriceProduct)
#implements: select(elem ,dic, nameProd)-->  dic = {}
#                                     -->  etiq = "a"

#-------------coto------------------------------
cotoNameProduct = soup3.findAll("div", {"class":"descrip_full"})
cotoPriceProduct = soup3.findAll("div", {"class":"info_discount"})
select("span", {"class":["atg_store_newPrice", "price_regular_precio"]}, cotoPriceProduct, lisAux2)
cargarDiccionario(diccioCoto, cotoNameProduct, lisAux2)
#implements: select(elem ,dic, priceProd)-->  dic = {"class":["atg_store_newPrice", "price_regular_precio"]}
#                                     -->  elem = "span"
#implements: buscar(text, '$') dentro de select(elem, dic, priceProd)

#------------walmart-------------------------
walmartNameProduct = soup4.findAll("a", {"class":"prateleira__name"})
walmartPriceProduct = soup4.findAll("span", {"class":"prateleira__best-price"})
cargarDiccionario(diccioWalmart, walmartNameProduct, walmartPriceProduct)

#-----------------Crear hoja de Excel y cargar los datos-------------------

ruta = "C:/Users\MartinXD\.spyder-py3\Scraping Web/infoPreciosSuperMarket.xlsx"
iniciales = ['Productos', 'Jumbo', 'Dia', 'Coto', 'Walmart', 'Fecha']

#ExportDatExcel2.crearExcel(ruta)
#ExportDatExcel2.cargarIniciales(ruta, iniciales)
#ExportDatExcel2.cargarAExcel(ruta, 2, diccioJumbo)
#ExportDatExcel2.cargarAExcel(ruta, 3, diccioDia)
#ExportDatExcel2.cargarAExcel(ruta, 4, diccioCoto)
#ExportDatExcel2.cargarAExcel(ruta, 5, diccioWalmart)
#print(ExportDatExcel2.tamanioColumna(ruta, 'Productos'))
#ExportDatExcel2.leerExcel(ruta)

#---------------Enviar Correo----------------------------

#archivo = "infoPreciosSuperMarket.xlsx"
#descripcion = "Information COCA-COLA price"
#sendMail.enviarCorreo(archivo, descripcion)
