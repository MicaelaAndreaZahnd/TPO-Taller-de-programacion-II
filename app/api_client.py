#api_client
import requests
from app.config import clave_clima

def buscar_dolar():
    link_api = "https://dolarapi.com/v1/dolares/mayorista"
    try:
        respuesta = requests.get(link_api, timeout=5)
        if respuesta.status_code == 200:
            datos_json = respuesta.json() 
            return datos_json["venta"]
        else:
            return 0
    except Exception as error:
        print("Error en el dolar:", error)
        return 0

def buscar_clima():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Buenos Aires&appid={clave_clima}&units=metric&lang=es"
    try:
        respuesta = requests.get(url, timeout=5)
        if respuesta.status_code == 200:
            datos_json = respuesta.json()
            descripcion = datos_json["weather"][0]["description"]
            temperatura = datos_json["main"]["temp"]
            return f"{descripcion}, {temperatura}°C"
        else:
            return "Sin datos de clima"
    except Exception as error:
        print("Error en el clima:", error)
        return "Sin datos de clima"

def alerta_post(nombre_producto):
    url_prueba = "https://httpbin.org/post"
    datos_compilados = {"alerta": "Revisar precio", "producto": nombre_producto}
    try:
        requests.post(url_prueba, json=datos_compilados, timeout=5)
    except:
        pass