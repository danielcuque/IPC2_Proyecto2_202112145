from model.simulation.InitialConfig import InitialConfig


class Main:

    initial_config: InitialConfig = InitialConfig()

    def __init__(self) -> None:
        self.run()

    @staticmethod
    def _initial_menu() -> str:
        print("1. Configuración de empresas")
        print("2. Seleccionar empresa y punto de atención")
        print("3. Manejo de puntos de atención")
        print("4. Salir")
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

    def _company_menu(self) -> None:
        while True:
            print("1. Limpiar sistema")
            print("2. Cargar archivo de configuración")
            print("3. Crear nueva empresa")
            print("4. Cargar archivo de configuración inicial")
            print("5. Volver")
            option = input("Seleccione una opción: ")
            
            if option == "1":
                self.initial_config.clear_system()
            elif option == "2":
                self._system_config()
            elif option == "3":
                self._create_company()
            elif option == "4":
                self._system_init()
            elif option == "5":
                break
            else:
                print("No existe esta opción")


    def _create_company(self) -> None:
        name = input("Introduzca el nombre de la empresa: ")
        if name:
            self.initial_config.create_company(name)
        else:
            print("No existe el fichero")
    
    def _select_company(self) -> None:
        pass

    def _select_point(self) -> None:
        pass

    def run(self) -> None:
        while True:
            choice = self._initial_menu()
            if choice == "1":
                self._company_menu()
            elif choice == "2":
                self._system_init()
            elif choice == "3":
                self._exit()
            elif choice == "4":
                self._exit()
            else:
                print("No existe esta opción")

if __name__ == "__main__":
    Main()
