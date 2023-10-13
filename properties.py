class Properties:

    def __init__(self):
        self.llaves = {}
        self.leer_configuracion()
        self.leer_contenido()

    def leer_configuracion(self):
        file = open('croacia.properties', 'r')
        for line in file:
            partes = line.rstrip().split('=')
            self.llaves[partes[0]] = partes[1]
        file.close()

    def leer_contenido(self):
        with open('croacia.contenido', 'r') as file:
            self.llaves['contenido'] = file.read()

    def get(self, llave):
        return self.llaves[llave]


if 'props' not in locals():
    props = Properties()


def get(llave):
    return props.get(llave)
