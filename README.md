# Trabajo Práctico: Plataforma Inteligencia Retail

Este proyecto es un script en Python para monitorear los precios de nuestro catálogo interno contra la competencia (Sodimac y Pinturerías Rex). El programa extrae precios web, consulta el dólar mayorista y el clima actual, y genera un reporte comparativo en Pandas.

## Estructura del Código
* `app/config.py`: Lista de destinatarios y diccionarios con SKUs, links de la competencia y etiquetas HTML.
* `app/scraper.py`: Conexión web (con timeout) y extracción usando BeautifulSoup. Incluye limpieza de texto y captura de atributos HTML.
* `app/api_client.py`: Consultas mediante método GET a DolarAPI (pública abierta) y OpenWeatherMap (con API Key). Incluye una alerta simulada con método POST a httpbin.
* `app/etl.py`: Generación del DataFrame y cálculo de diferencias absolutas y porcentuales.
* `main.py`: Ejecución del programa, con pausas de 2 segundos entre consultas.

## Documentación de Scraping y APIs
* **Sodimac (`www.sodimac.com.ar`):** El precio se encuentra dentro de un contenedor con la clase `jsx-2816876583 primary`. 
* **Pinturerías Rex (`somosrex.com`):** El precio está en una etiqueta con la clase `price`. Adicionalmente capturamos su atributo `id`.
* **Políticas de uso:** Se revisaron manualmente los archivos `robots.txt` de ambos dominios. Para evitar saturar los servidores de la competencia y respetar los límites de frecuencia, implementamos un delay (`time.sleep`) en el ciclo principal.

### API Pública vs. API Privada
* **API Pública:** Es abierta para que la consuma cualquier desarrollador, muchas veces sin necesidad de registrarse. En nuestro proyecto, usamos la API pública **DolarAPI** para traer la cotización del dólar mayorista de forma libre.
* **API Privada (o interna):** Es un servicio restringido al que solo pueden acceder los empleados o sistemas de una empresa mediante tokens de alta seguridad. Un ejemplo sería si tuviéramos que conectarnos al sistema de inventario (SAP/ERP) de nuestra propia empresa para consultar el stock real de los tachos de pintura.

## Seguridad y Variables de Entorno (N17)
Para cumplir con las buenas prácticas de seguridad, las credenciales (como la API Key de OpenWeatherMap) no se exponen en el código fuente. Se implementó la librería `os` para leer las claves desde un archivo `.env` local, el cual está protegido y excluido del control de versiones gracias al archivo `.gitignore`.