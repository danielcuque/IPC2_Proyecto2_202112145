from xml.dom.minidom import Element, parse


class InitConfig:

    def init_config(self, path_file):
        try:
            init_info: Element = parse(path_file)
        except FileNotFoundError:
            print("Ocurrió un error al leer el fichero")
