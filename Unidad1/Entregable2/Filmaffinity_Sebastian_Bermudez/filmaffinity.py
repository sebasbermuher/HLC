# pip install requests
import requests

# Terminator 2: The judgment day
#r = requests.get('https://www.filmaffinity.com/es/film576352.html')
# Monty Python's Life of Brian
# r = requests.get('https://www.filmaffinity.com/es/film612331.html')


class Filmaffinity:
    resultado = {"Título original: ": "",
                 "Año ": "",
                 "Duración ": "",
                 "País ": "",
                 "Dirección ": "",
                 "Guión ": "",
                 "Música ": "",
                 "Fotografía ": "",
                 "Reparto ": "",
                 "Productora ": "",
                 "Género ": "",
                 "Sipnosis ": ""
                 }

    url = ""
    html = ""

    def __init__(self, url):
        self.url = url

    def set_url(self, url):
        self.url = url

    def do_request(self):
        temp = requests.get(self.url)
        self.html = temp.text

    def get_result(self):
        return self.resultado

    def procesar(self):
        self.resultado = {"Título original: ": self.titulo_original(),
                          "Año ": self.year(),
                          "Duración ": self.duracion(),
                          "País ": self.pais(),
                          "Dirección ": self.direccion(),
                          "Guión ": self.guion(),
                          "Música ": self.musica(),
                          "Fotografía ": self.fotografia(),
                          "Reparto ": self.reparto(),
                          "Productora ": self.productora(),
                          "Género ": self.genero(),
                          "Sipnosis ": self.sinopsis()
                          }

    def titulo_original(self):
        etiqueta_titulo = "<dt>Título original</dt>"
        pos_etiqueta_titulo = self.html.find(etiqueta_titulo)
        titulo = self[pos_etiqueta_titulo:]
        #titulo = titulo[:titulo.find("<span")].splitlines()[2].lstrip().rstrip()
        titulo = titulo[:titulo.find(
            "</dd>")].splitlines()[2].lstrip().rstrip()
        return titulo

    def year(self):
        cadena_buscar = ("<dd itemprop=\"datePublished\">")
        long_cadena_buscar = len(cadena_buscar)
        pos_cadena = self.html.find(cadena_buscar)
        anio = self[pos_cadena + long_cadena_buscar: pos_cadena +
                    long_cadena_buscar + 4]
        return anio

    def duracion(self):
        cadena_buscar = ("<dd itemprop=\"duration\">")
        long_cadena_buscar = len(cadena_buscar)
        pos_cadena = self.html.find(cadena_buscar)
        cad = self[pos_cadena:]
        cad = cad[:cad.find("</dd>")]
        duration = cad[long_cadena_buscar:]
        return duration

    def pais(self):
        cadena_buscar = ("<dt>País</dt>")
        long_cadena_buscar = len("</span>")
        pos_cadena = self.html.find(cadena_buscar)
        quitarSpan = self[pos_cadena:]
        cad = quitarSpan.find("</span>")
        cadNueva = quitarSpan[cad + long_cadena_buscar:]
        fin_cad = cadNueva.find("</dd>")
        cadPais = cadNueva[:fin_cad]
        return cadPais

    def direccion(self):
        cadena_buscar = ("class=\"directors\"")
        pos_cadena = self.html.find(cadena_buscar)
        director = self[pos_cadena:]
        cadDirec = director.find("title=\"")
        lenTitle = len("titel=\"")
        etiqueta = director[cadDirec + lenTitle:]
        cadDirector = etiqueta.find("\">")
        cadFinal = etiqueta[:cadDirector]
        return cadFinal

    def guion(self):
        cadena_buscar = "<dt>Guion</dt>"
        pos_cadena = self.html.find(cadena_buscar)
        guion = self[pos_cadena:]
        guion = guion[:guion.find("</dd>")]
        guion == guion[guion.find('<span class="nb>'): guion.find('</div>')]
        actores = ""
        while guion.find("<span>") != -1:
            guion = guion[guion.find("<span>") + len("<span>"):]
            actores += guion[:guion.find("</span>")] + ", "
        actores = actores.rstrip(", ")
        return actores

    def musica(self):
        cadena_buscar = ("<dt>Música</dt>")
        long_cadena_buscar = len("</span>")
        pos_cadena = self.html.find(cadena_buscar)
        quitarSpan = self[pos_cadena:]
        cad = quitarSpan.find("<span>")
        cadNueva = quitarSpan[cad + (long_cadena_buscar-1):]
        fin_cad = cadNueva.find("</span>")
        cadMusica = cadNueva[:fin_cad]
        return cadMusica

    def fotografia(self):
        cadena_buscar = ("<dt>Fotografía</dt>")
        long_cadena_buscar = len("</span>")
        pos_cadena = self.html.find(cadena_buscar)
        quitarSpan = self[pos_cadena:]
        cad = quitarSpan.find("<span>")
        cadNueva = quitarSpan[cad + (long_cadena_buscar-1):]
        fin_cad = cadNueva.find("</span>")
        cadFoto = cadNueva[:fin_cad]
        return cadFoto

    def reparto(self):
        cadena_buscar = "<dt>Reparto</dt>"
        pos_cadena = self.html.find(cadena_buscar)
        etiqueta = self[pos_cadena + len("<dt>Reparto</dt>"):]
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

    def productora(self):
        cadena_buscar = ("<dt>Productora</dt>")
        long_cadena_buscar = len("</span>")
        pos_cadena = self.html.find(cadena_buscar)
        quitarSpan = self[pos_cadena:]
        cad = quitarSpan.find("<span>")
        cadNueva = quitarSpan[cad + (long_cadena_buscar-1):]
        fin_cad = cadNueva.find("</span>")
        cadProductora = cadNueva[:fin_cad]
        return cadProductora

    def genero(self):
        cadena_buscar = "<dt>Género</dt>"
        pos_cadena = self.html.find(cadena_buscar)
        etiqueta = self[pos_cadena:]
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

    def sinopsis(self):
        cadena_buscar = ("itemprop=\"description\">")
        long_cadena_buscar = len(cadena_buscar)
        pos_cadena = self.html.find(cadena_buscar)
        cad = self[pos_cadena:]
        cad = cad[:cad.find("</dd>")]
        cadSinopsis = cad[long_cadena_buscar:]
        return cadSinopsis
