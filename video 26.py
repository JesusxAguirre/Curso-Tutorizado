#trabajando con crawlers

from bs4 import BeautifulSoup
import requests

miReq = requests.get("http://python.beispiel.programmierenlernen.io/index.php")

#print(miReq.status_code)

#print(miReq.headers)

#print(miReq.text)

docfinal = BeautifulSoup(miReq.text, 'html.parser')


variable = docfinal.select("img")

for i in range(0,len(variable)): 
    print(variable[i].attrs["src"])
    print("")