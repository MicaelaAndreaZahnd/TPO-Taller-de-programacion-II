# app/scraper.py
import requests
from bs4 import BeautifulSoup
from app.config import headers_navegador

def limpiar_nombre(nombre_bruto):
    texto_1 = nombre_bruto.strip()
    texto_final = texto_1.lower()
    return texto_final

def limpiar_numero(texto_precio):
    a = texto_precio.replace("$", "")
    b = a.replace(".","")
    c = b.replace(",","")
    d = c.strip()

    if d.isdigit() == True:
        numero_final = float(d)
        return numero_final
    else:
        return 0.0

def buscar_precio_web(link, nombre_clase):
    try:
        respuesta = requests.get(link, headers=headers_navegador, timeout=10)

        if respuesta.status_code == 200:
            html_pagina = respuesta.text
            sopa = BeautifulSoup(html_pagina, 'html.parser')

            etiquetas = sopa.find_all(lambda etiqueta: etiqueta.name in ['div', 'span'] and etiqueta.has_attr('class') and (nombre_clase in etiqueta['class'] or nombre_clase == " ".join(etiqueta['class'])))
            
            if len(etiquetas) > 0:
                texto = etiquetas[0].text
                id_html = etiquetas[0].get('id', 'Sin ID')
                precio_listo = limpiar_numero(texto)
                return precio_listo
            else:
                return 0.0
        else:
            print("Error en la página")
            return 0.0
            
    except Exception as error:
        print("Error de conexion:", error)
        return 0.0