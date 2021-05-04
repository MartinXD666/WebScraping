# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#from urllib.request import urlopen
#from bs4 import BeautifulSoup
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

#Extraer info de StackOverflow: Preguntas.

class Pregunta(Item):
    pregunta = Field()
    id = Field()
    
class StackOverflowSpider(Spider):
    name = "MiPrimerScraping"
    
    start_urls = ['https://es.stackoverflow.com/']
    def parse(self, response):
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="question-mini-list"]/div/div')
        
        #iterar sobre las preguntas
        
        for i, elem in enumerate(preguntas):
            item = ItemLoader(Pregunta(), elem)
            item.add_xpath('pregunta', './/h3/a/text()')
            item.add_value('id', i)
            yield item.load_item()
