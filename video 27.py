from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import time

class PostCrawler():
  def __init__(self,titulo,emoticono,contenido,imagen,link) -> None:
    self.titulo = titulo
    self.emoticono = emoticono
    self.contenido = contenido
    self.imagen = imagen
    self.link = link

class Extractor():

  docfinal = ""
  def __init__(self):
    self.urlBase = "http://python.beispiel.programmierenlernen.io/index.php"
    self.conexion_pagina = requests.get(self.urlBase)
    self.docfinal = BeautifulSoup(self.conexion_pagina.text, 'html.parser')
    
  def get_info(self):
    #lista= []
    while self.urlBase != "": #mientras url base no este vacia
      #conectando 
      self.conexion_pagina = requests.get(self.urlBase)
      self.docfinal = BeautifulSoup(self.conexion_pagina.text, 'html.parser')
      time.sleep(2)
      link = self.docfinal.select_one(".navigation a")
      if link:
        self.urlBase =  urljoin(self.urlBase,link.attrs['href'])
        print(self.urlBase)
      else:
        self.urlBase = "" 
      for card in self.docfinal.select(".card"): #dentro del buccle for 
        titulo = card.select(".card-title span")[1].text
        emoticono = card.select_one(".emoji").text
        contenido = card.select_one(".card-text").text
        img = urljoin(self.urlBase,card.select_one("img").attrs['src'])

        #generador
        
        yield PostCrawler(titulo,emoticono,contenido,img,link) 
        
        #Crawler = PostCrawler(titulo,emoticono,contenido,img,link) 
        #lista.append(Crawler)
      #fuera del bucle for 
   
    
        
    #return lista

#creando objeto

unPost = Extractor()

listaPost = unPost.get_info()
contador = 0
for elPost in  listaPost:
  if contador ==12: break
  contador = contador +1 
  print(elPost.emoticono)
  print(elPost.titulo)
  print(elPost.contenido)
  print(elPost.imagen)
  print(elPost.link)
  print("")



"""with open('Posts.csv', 'w', newline='',encoding="utf-8") as csvfile:
    postwriter = csv.writer(csvfile, delimiter=',', 
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for miPost in listaPost:
      postwriter.writerow([miPost.emoticono,miPost.titulo,miPost.contenido,miPost.imagen])""" 

