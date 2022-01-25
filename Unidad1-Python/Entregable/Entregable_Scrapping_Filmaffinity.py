# pip install requests
import requests

# Terminator 2: The judgment day
#r = requests.get('https://www.filmaffinity.com/es/film576352.html')
# Monty Python's Life of Brian
r = requests.get('https://www.filmaffinity.com/es/film612331.html')

# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
t = r.text

# print(t)


def titulo_original(t):
    etiqueta_titulo = "<dt>Título original</dt>"
    pos_etiqueta_titulo = t.find(etiqueta_titulo)
    titulo = t[pos_etiqueta_titulo:]
    #titulo = titulo[:titulo.find("<span")].splitlines()[2].lstrip().rstrip()
    titulo = titulo[:titulo.find("</dd>")].splitlines()[2].lstrip().rstrip()
    return titulo
#print("Título original: " + titulo_original(t))


def year(t):
    cadena_buscar = ("<dd itemprop=\"datePublished\">")
    long_cadena_buscar = len(cadena_buscar)
    pos_cadena = t.find(cadena_buscar)
    anio = t[pos_cadena + long_cadena_buscar: pos_cadena + long_cadena_buscar + 4]
    return anio
#print("Año: " + year(t))


def duracion(t):
    cadena_buscar = ("<dd itemprop=\"duration\">")
    long_cadena_buscar = len(cadena_buscar)
    pos_cadena = t.find(cadena_buscar)
    cad = t[pos_cadena:]
    cad = cad[:cad.find("</dd>")]
    duration = cad[long_cadena_buscar:]
    return duration
#print("Duracion: " + duracion(t))


def pais(t):
    cadena_buscar = ("<dt>País</dt>")
    long_cadena_buscar = len("</span>")
    pos_cadena = t.find(cadena_buscar)
    quitarSpan = t[pos_cadena:]
    cad = quitarSpan.find("</span>")
    cadNueva = quitarSpan[cad + long_cadena_buscar:]
    fin_cad = cadNueva.find("</dd>")
    cadPais = cadNueva[:fin_cad]
    return cadPais
#print("País: " + pais(t))


def direccion(t):
    cadena_buscar = ("class=\"directors\"")
    pos_cadena = t.find(cadena_buscar)
    director = t[pos_cadena:]
    cadDirec = director.find("title=\"")
    lenTitle = len("titel=\"")
    etiqueta = director[cadDirec + lenTitle:]
    cadDirector = etiqueta.find("\">")
    cadFinal = etiqueta[:cadDirector]
    return cadFinal
#print("Direccion: " + direccion(t))


def guion(t):
    cadena_buscar = "<dt>Guion</dt>"
    pos_cadena = t.find(cadena_buscar)
    guion = t[pos_cadena:]
    guion = guion[:guion.find("</dd>")]
    guion == guion[guion.find('<span class="nb>'): guion.find('</div>')]
    actores = ""
    while guion.find("<span>") != -1:
        guion = guion[guion.find("<span>") + len("<span>"):]
        actores += guion[:guion.find("</span>")] + ", "
    actores = actores.rstrip(", ")
    return actores
#print("Guion: " + guion(t))


def musica(t):
    cadena_buscar = ("<dt>Música</dt>")
    long_cadena_buscar = len("</span>")
    pos_cadena = t.find(cadena_buscar)
    quitarSpan = t[pos_cadena:]
    cad = quitarSpan.find("<span>")
    cadNueva = quitarSpan[cad + (long_cadena_buscar-1):]
    fin_cad = cadNueva.find("</span>")
    cadMusica = cadNueva[:fin_cad]
    return cadMusica
#print("Música: " + musica(t))


def fotografia(t):
    cadena_buscar = ("<dt>Fotografía</dt>")
    long_cadena_buscar = len("</span>")
    pos_cadena = t.find(cadena_buscar)
    quitarSpan = t[pos_cadena:]
    cad = quitarSpan.find("<span>")
    cadNueva = quitarSpan[cad + (long_cadena_buscar-1):]
    fin_cad = cadNueva.find("</span>")
    cadFoto = cadNueva[:fin_cad]
    return cadFoto
#print("Fotografía: " + fotografia(t))


def reparto(t):
    cadena_buscar = "<dt>Reparto</dt>"
    pos_cadena = t.find(cadena_buscar)
    etiqueta = t[pos_cadena + len("<dt>Reparto</dt>"):]
    etiqueta = etiqueta[:etiqueta.find("</dd>")]
    etiqueta == etiqueta[etiqueta.find(
        '<span class="nb'): etiqueta.find('</div>')]
    cadReparto = ""
    while etiqueta.find("<span itemprop=\"name\">") != -1:
        etiqueta = etiqueta[etiqueta.find(
            "itemprop=\"name\">") + len("itemprop=\"name\">"):]
        cadReparto += etiqueta[:etiqueta.find("</span>")] + ", "
    cadReparto = cadReparto.rstrip(", ")
    return cadReparto
#print("Reparto: " + reparto(t))


def productora(t):
    cadena_buscar = ("<dt>Productora</dt>")
    long_cadena_buscar = len("</span>")
    pos_cadena = t.find(cadena_buscar)
    quitarSpan = t[pos_cadena:]
    cad = quitarSpan.find("<span>")
    cadNueva = quitarSpan[cad + (long_cadena_buscar-1):]
    fin_cad = cadNueva.find("</span>")
    cadProductora = cadNueva[:fin_cad]
    return cadProductora
#print("Productora: " + productora(t))


def genero(t):
    cadena_buscar = "<dt>Género</dt>"
    pos_cadena = t.find(cadena_buscar)
    etiqueta = t[pos_cadena:]
    etiqueta = etiqueta[:etiqueta.find("</dd>")]
    etiqueta_inicio = '<a href='
    etiqueta_cierre = "</a>"
    cadGeneros = ""
    while(etiqueta.find(etiqueta_inicio) != -1):
        etiqueta = etiqueta[etiqueta.find(
            etiqueta_inicio)+len(etiqueta_inicio):]
        etiqueta = etiqueta[etiqueta.find(">")+len(">"):]
        cadGeneros += etiqueta[:etiqueta.find(etiqueta_cierre)] + ". "
    return cadGeneros
#print("Genero: " + genero(t))


def sinopsis(t):
    cadena_buscar = ("itemprop=\"description\">")
    long_cadena_buscar = len(cadena_buscar)
    pos_cadena = t.find(cadena_buscar)
    cad = t[pos_cadena:]
    cad = cad[:cad.find("</dd>")]
    cadSinopsis = cad[long_cadena_buscar:]
    return cadSinopsis
#print("Sinopsis: " + sinopsis(t))


# -----------------------------------------------------------
diccionario = {"Titulo": titulo_original(t),
               "Año": year(t),
               "Duracion": duracion(t),
               "Pais": pais(t),
               "Dirección": direccion(t),
               "Guión": guion(t),
               "Música": musica(t),
               "Fotografía": fotografia(t),
               "Reparto": reparto(t),
               "Productora": productora(t),
               "Género": genero(t),
               "Sinopsis": sinopsis(t),
               }
print(diccionario)
