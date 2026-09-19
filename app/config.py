# app/config.py
clave_clima = "123456789_clave_falsa_openweathermap"

lista_categorias = ["pinturas interior"]
sku_comercio = ["E-1121193", "E-1193368", "E-1166962", "E-1193369"]

destinatarios_compras = ["compras@easy.com", "gerencia@easy.com"]

prod_1 = {
    "sku" : "E-1121193",
    "nombre" :"Pintura Látex Interior Blanco Satinado 20 Lts Alba",
    "competidor": "Sodimac",
    "nombre_competidor": "Pintura Latex De Interior Blanco Satinado Lavable 20 L",
    "precio_comercio" : 290000,
    "link" : "https://www.sodimac.com.ar/sodimac-ar/product/1365959/pintura-latex-de-interior-blanco-satinado-lavable-20-l/1365959/",
    "clase" : "jsx-2816876583 primary"
}

prod_2 = {
    "sku" : "E-1193368",
    "nombre" : "Pintura Látex Interior Blanco Mate 4 Lts Alba",
    "competidor": "Sodimac",
    "nombre_competidor": "Pintura Latex De Interior Blanco Mate Ultralavable 4 L",
    "precio_comercio" : 70000,
    "link" : "https://www.sodimac.com.ar/sodimac-ar/product/2305453/pintura-latex-de-interior-blanco-mate-ultralavable-4-l/2305453/",
    "clase" : "jsx-2816876583 primary"
}

prod_3 = {
    "sku" : "E-1166962",
    "nombre" : "Pintura Látex Interior Blanco Extra Mate 20 Lts Alba",
    "competidor": "Sodimac",
    "nombre_competidor": "Pintura Latex Lavable Blanco Mate Interior 20 L",
    "precio_comercio" : 185000,
    "link" : "https://www.sodimac.com.ar/sodimac-ar/product/1345354/pintura-latex-lavable-blanco-mate-interior-20-l/1345354/",
    "clase" : "jsx-2816876583 primary"
}

prod_4 = {
    "sku" : "E-1193369",
    "nombre" : "Pintura Látex Interior Blanco Mate 20 Lts Alba",
    "competidor": "Sodimac",
    "nombre_competidor": "Pintura Latex De Interior Blanco Mate Ultralavable 20 L",
    "precio_comercio" : 230000,
    "link" : "https://www.sodimac.com.ar/sodimac-ar/product/230547X/pintura-latex-de-interior-blanco-mate-ultralavable-20-l/230547X/",
    "clase" : "jsx-2816876583 primary"
}

prod_5 = {
    "sku" : "E-1121193",
    "nombre" :"Pintura Látex Interior Blanco Satinado 20 Lts Alba",
    "competidor": "Rex",
    "nombre_competidor": "Latex Interior Albalatex Satinado Blanco 20 Lts Alba",
    "precio_comercio" : 290000,
    "link" : "https://somosrex.com/latex-interior-albalatex-satinado-blanco-20-lts-alba.html",
    "clase" : "price"
}

prod_6 = {
    "sku" : "E-1193368",
    "nombre" : "Pintura Látex Interior Blanco Mate 4 Lts Alba",
    "competidor": "Rex",
    "nombre_competidor": "Albalatex Ultralavable Interior Mate Blanco 04 Lt",
    "precio_comercio" : 70000,
    "link" : "https://somosrex.com/albalatex-ultralavable-interior-mate-blanco-04-lt.html",
    "clase" : "price"
}

prod_7 = {
    "sku" : "E-1166962",
    "nombre" : "Pintura Látex Interior Blanco Extra Mate 20 Lts Alba",
    "competidor": "Rex",
    "nombre_competidor": "Latex Interior Albalatex Mate Blanco 20 Lts Alba",
    "precio_comercio" : 185000,
    "link" : "https://somosrex.com/latex-interior-albalatex-mate-blanco-20-lts-alba.html",
    "clase" : "price"
}

prod_8 = {
    "sku" : "E-1193369",
    "nombre" : "Pintura Látex Interior Blanco Mate 20 Lts Alba",
    "competidor": "Rex",
    "nombre_competidor": "Latex Interior Albalatex Ultralavable Mate Blanco 20 Lts Alba",
    "precio_comercio" : 230000,
    "link" : "https://somosrex.com/latex-interior-albalatex-ultralavable-mate-blanco-20-lts-alba.html",
    "clase" : "price"
}

productos_competencia = [prod_1, prod_2, prod_3, prod_4, prod_5, prod_6, prod_7, prod_8]

headers_navegador = {"User-Agent": "Mozilla/5.0"}