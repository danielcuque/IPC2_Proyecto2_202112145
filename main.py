from model.simulation.InitialConfig import InitialConfig


class Main:

    initial_config: InitialConfig = InitialConfig()

    def __init__(self) -> None:
        self.run()

    @staticmethod
    def _initial_menu() -> str:
        print("1. Configuración del sistema")
        print("2. Inicialización del sistema")
        print("3. Exit")
        return input("Seleccione una opción: ")

    @staticmethod
    def _get_file() -> str:
        path_file = input("Introduzca la ruta del fichero: ")
        return path_file

    def _system_config(self) -> None:
        path_file = self._get_file()
        if path_file:
            self.initial_config.system_config(path_file)
        else:
            print("No existe el fichero")

    def _system_init(self) -> None:
        path_file = self._get_file()
        if path_file:
            self.initial_config.system_init(path_file)
        else:
            print("No existe el fichero")

    @staticmethod
    def _exit():
        print("¡Adiós!")
        exit()

    def run(self) -> None:
        while True:
            choice = self._initial_menu()
            if choice == "1":
                self._system_config()
            elif choice == "2":
                self._system_init()
            elif choice == "3":
                self._exit()
            else:
                print("No existe esta opción")


if __name__ == "__main__":
    Main()
