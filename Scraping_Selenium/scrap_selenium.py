#---------------BOOKSTORES----------------------
import json
import random
from time import sleep
from selenium import webdriver

#---------------------FUNCTIONS------------------------
def cargarJson():

    with open('dataPeliculas.json', 'a') as file:
        json.dump(data, file, indent=4)

def cargarData(titulo, sinopsis, genero, precio):

    data['Peliculas'].append( {
        'Titulo' : titulo,
        'Sinopsis' : sinopsis,
        'Genero' : genero,
        'Precio' : precio
    })
    print(data)

def actualizarPrincipal():
    print("ACTUALIZANDO PAGINA PRINCIPAL...\n")
    driver.get('https://www.clarovideo.com/argentina/nv_catalogo')
    sleep(3)
    scrollFinal()
    url = driver.current_url
    print(url)

def scrollFinal():

    for i in range(8):
        driver.execute_script("window.scrollBy (0, 1000)")
        sleep(random.uniform(3.0, 6.0))

#------------------------------MAIN-----------------------------------------

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.clarovideo.com/argentina/nv_catalogo')
data = {}
data['Peliculas'] = []
sleep(3)
scrollFinal()
url=driver.current_url
print("COMENZANDO DESDE: ", url, "\n")
sections = driver.find_elements_by_xpath('//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
lengthSections = len(sections)
print(lengthSections)

for i in range(lengthSections):
    cantPeliculas = 0
    sections = driver.find_elements_by_xpath('//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
    print("--------------------------SECTION1--------------------------")
    if i == 0:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath('.//button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            cargarData(titulo, sinopsis, genero, precio)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[2]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION2--------------------------")
    if i == 1:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath('.//button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            cargarData(titulo, sinopsis, genero, precio)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[3]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION3--------------------------")
    if i == 2:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[4]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION4--------------------------")
    if i == 3:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[5]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION5--------------------------")
    if i == 4:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[6]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION6--------------------------")
    if i == 5:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[7]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION7--------------------------")
    if i == 6:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[8]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION8--------------------------")
    if i == 7:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[9]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION9--------------------------")
    if i == 8:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[10]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION10--------------------------")
    if i == 9:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[11]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION11--------------------------")
    if i == 10:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[12]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION12--------------------------")
    if i == 11:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[13]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION13--------------------------")
    if i == 12:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[14]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION14--------------------------")
    if i == 13:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[15]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION15--------------------------")
    if i == 14:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[16]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION16--------------------------")
    if i == 15:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[17]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION17--------------------------")
    if i == 16:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[18]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION18--------------------------")
    if i == 17:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[19]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    print("--------------------------SECTION19--------------------------")
    if i == 18:
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas += 1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url, "\n")

            titulo = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            sinopsis = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath(
                './/*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            precio = driver.find_element_by_xpath(
                './/button[@class="vcard vcard-blue-button btn btn-default btn-lg primary"]/span').text

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            cargarData(titulo, sinopsis, genero, precio)

            print(titulo)
            print(sinopsis)
            print(genero)
            print(precio)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div[2]/div/div/section[20]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))
cargarJson()
driver.quit()
exit()
