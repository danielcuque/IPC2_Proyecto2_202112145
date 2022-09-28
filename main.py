class Main:
    def __init__(self):
        self.run()

    def _initial_menu(self):
        print("1. Configuración del sistema")
        print("2. Inicialización del sistema")
        print("3. Exit")
        return input("Enter your choice: ")

    def _get_file(self):
        path_file = input("Introduzca la ruta del fichero: ")
        return path_file

    def _system_config(self):
        path_file = self._get_file()
        info = open(path_file, "r")
        for line in info:
            print(line)
        info.close()

    def _system_init(self):
        path_file = self._get_file()
        info = open(path_file, "r")
        for line in info:
            print(line)
        info.close()

    def _exit(self):
        print("Bye!")
        exit()

    def run(self):
        while True:
            choice = self._initial_menu()
            if choice == "1":
                self._system_config()
            elif choice == "2":
                self._system_init()
            elif choice == "3":
                self._exit()
            else:
                print("Invalid choice")


if __name__ == "__main__":
    Main()
