# app/etl.py
import pandas as pd

def comparacion_precios(mi_precio, otro_precio):
    if otro_precio == 0.0:
        return "No hay precio"
    
    resta = otro_precio - mi_precio
    
    if resta > 0:
        return "Oportunidad"
    elif resta == 0:
        return "Igual"
    else:
        return "Costoso"

def dataframe(lista_de_datos):
    tabla = pd.DataFrame(lista_de_datos)
    
    lista_estados = []
    
    for index, fila in tabla.iterrows():
        estado = comparacion_precios(fila["Precio_Nuestro"], fila["Precio_Competidor"])
        lista_estados.append(estado)
        
    tabla["Estado"] = lista_estados
    
    tabla["Diferencia_Absoluta"] = tabla["Precio_Competidor"] - tabla["Precio_Nuestro"]
    
    tabla["Variación_Porcentual"] = (tabla["Diferencia_Absoluta"] / tabla["Precio_Nuestro"]) * 100
    
    return tabla