from bs4 import BeautifulSoup
from notificacion import Notificacion
import logging
import properties
import re
import requests

logging.basicConfig(level=logging.INFO)


def formatear_texto(texto):
    texto = remove_extra_whitespace(texto)
    soup = BeautifulSoup(texto, 'html.parser')
    return soup.prettify()


def main():
    url = properties.get('url')
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        elemento = soup.select_one(".page_content")
        texto1 = formatear_texto(str(elemento))
        texto2 = formatear_texto(properties.get('contenido'))
        if texto2 != texto1:
            notificar('texto ha cambiado')
        else:
            logging.info('texto es igual')
    else:
        notificar("error %d al pedir página %s" % (response.status_code, url))


def notificar(mensaje):
    noti = Notificacion()
    noti.publicar(mensaje)


def remove_extra_whitespace(texto):
    cleaned_string = re.sub(r'\s+', ' ', texto)
    return cleaned_string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
