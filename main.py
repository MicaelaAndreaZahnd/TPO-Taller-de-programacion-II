# main.py
import time
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


from app.config import productos_competencia
from app.scraper import buscar_precio_web, limpiar_nombre
from app.api_client import buscar_dolar, buscar_clima, alerta_post
from app.etl import dataframe

print("Inicio del programa...")

el_dolar_de_hoy = buscar_dolar()
clima_hoy = buscar_clima()
print(f"El dolar esta a: {el_dolar_de_hoy} | Clima: {clima_hoy}")
print("---------------------------------")

lista_final = []

for producto in productos_competencia:
    print(f"Buscando el producto en {producto['competidor']}: {producto['nombre']}")
    
    el_precio = buscar_precio_web(producto["link"], producto["clase"])
    nombre_limpio = limpiar_nombre(producto["nombre_competidor"])
    
    if el_precio > 0 and el_precio < producto["precio_comercio"]:
        alerta_post(producto["nombre"])
    
    dato_nuevo = {
        "Competidor": producto["competidor"],
        "Código": producto["sku"],
        "Nombre_Nuestro": producto["nombre"],
        "Nombre_Competidor": nombre_limpio,
        "Precio_Nuestro": producto["precio_comercio"],
        "Precio_Competidor": el_precio
    }
    
    lista_final.append(dato_nuevo)
    
    time.sleep(2) 

tabla_final = dataframe(lista_final)

print("\nFinalizo la busqueda. Muestro la tabla:")
print("---------------------------------")
print(tabla_final)