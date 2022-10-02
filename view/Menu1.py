import inquirer

from model.simulation.InitConfig import InitConfig
from model.simulation.SystemConfig import SystemConfig
from model.utils.Utils import get_file


class Menu1:

    system_config = SystemConfig()
    init_config = InitConfig()

    def company_menu(self) -> None:
        while True:
            questions = [
                inquirer.List('menu',
                            message="Seleccione una opción",
                            choices=["1. Limpiar sistema",
                                    "2. Cargar archivo de configuración",
                                    "3. Crear empresa",
                                    "4. Cargar archivo de configuración inicial",
                                    "5. Regresar"])]
            answer = inquirer.prompt(questions=questions)
            if answer is not None:
                if answer['menu'] == "1. Limpiar sistema":
                    self._clear_system()
                elif answer['menu'] == "2. Cargar archivo de configuración":
                    self._system_config()
                elif answer['menu'] == "3. Crear empresa":
                    self._create_company_menu()
                elif answer['menu'] == "4. Cargar archivo de configuración inicial":
                    pass
                elif answer['menu'] == "5. Regresar":
                    break

    def _clear_system(self) -> None:
        if self.system_config.clear_system():
            print("Sistema limpio")
        else:
            print("No se pudo limpiar el sistema")

    def _system_config(self) -> None:
        path_file = get_file()
        if path_file:
            self.system_config.system_config(path_file)
        else:
            print("No existe el fichero")
    
    def _create_company_menu(self):
        pass

    def _init_config(self) -> None:
        pass
