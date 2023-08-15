# %%
import requests
import time 

import datetime
import pandas as pd
from bs4 import BeautifulSoup

# %%
pagina_web = requests.get("https://es-us.noticias.yahoo.com/clima/mexico/chihuahua/ciudad-juarez-116556")
soup = BeautifulSoup(pagina_web.text, 'html.parser')
print(soup.prettify())

# %%
def extraer():
   
    fecha_actual = datetime.datetime.now()
    dia=fecha_actual.strftime('%A %d %b %Y')
    hora=fecha_actual.strftime("%H:%M")
    fecha= dia+" " +hora

    tempsf=[]
    tempf_items = soup.find_all('span', class_="Va(t) D(b) fahrenheit celsius_D(n)")
    for item in tempf_items:
        tempf= item.text
        tempsf.append(tempf)


    tempsc=[]
    tempc_items = soup.find_all('span', class_="Va(t) D(n) celsius celsius_D(b)")
    for item in tempc_items:
        tempc= item.text
        tempsc.append(tempc)


    detalles=[]
    detalle_items = soup.find_all('p', class_="Fz(1.40rem)--miw1024 Fz(1.12rem)")
    for item in detalle_items:
        detalle= item.text
        detalles.append(detalle)

    
    datos=[]
    datos.append({"Fecha": fecha, "Temperatura Celsius":tempsc, "Temperatura Fahrenheit":tempsf,"Condicion":detalles})
    
    df = pd.DataFrame(datos)
    
    
    archivo=open("datos-clima.csv","a")

    archivo.write(f"{datos}\n")
    archivo.close()
    



# %%

extraer()


