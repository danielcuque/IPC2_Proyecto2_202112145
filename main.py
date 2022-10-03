import inquirer

# Menus for app
from view.Menu1 import Menu1
from view.Menu2 import Menu2
from view.Menu3 import Menu3


class Main:
    def __init__(self) -> None:
        self.run()

    def run(self) -> None:
        menu1 = Menu1()
        menu2 = Menu2()
        menu3 = Menu3()

        while True:
            questions = [
                inquirer.List('menu',
                              message="Seleccione una opción",
                              choices=["1. Configuración del sistema",
                                       "2. Seleccionar empresa y punto de atención",
                                       "3. Manejo de puntos de atención",
                                       "4. Salir"])]
            answer = inquirer.prompt(questions=questions)
            if answer is not None:
                if answer['menu'] == "1. Configuración del sistema":
                    menu1.company_menu()
                elif answer['menu'] == "2. Seleccionar empresa y punto de atención":
                    menu2.select_company()
                elif answer['menu'] == "3. Manejo de puntos de atención":
                    menu3.manage_point_menu()
                elif answer['menu'] == "4. Salir":
                    self._exit()
                else:
                    print("No existe esta opción")

    # Menu 3
    def _point_menu(self) -> None:
        pass

    # Menu 4
    @staticmethod
    def _exit():
        print("¡Adiós!")
        exit()


if __name__ == "__main__":
    Main()
