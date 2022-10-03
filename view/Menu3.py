import inquirer
from rich.console import Console

# Classes
from controller.classes.Company import Company
from controller.classes.Office import Office

# Controllers
from controller.store.StoreData import StoreData


class Menu3:

    def manage_point_menu(self) -> None:
        console = Console()
        if StoreData.selected_company is None:
            console.print("No hay una empresa seleccionada", style="bold red")
        elif StoreData.selected_office is None:
            console.print("No hay una oficina seleccionada", style="bold red")
        else:
            while True:
                options_main_menu = [
                    inquirer.List('menu',
                                message="Seleccione una opción",
                                choices=["1. Ver el estado del punto de antención",
                                        "2. Activar escritorio de servicio",
                                        "3. Desactivar escritorio de servicio",
                                        "4. Atender cliente",
                                        "5. Solicitud de atención",
                                        "6. Simular actividad de punto de atención",
                                        "7. Regresar"])]
                answer = inquirer.prompt(questions=options_main_menu)
                if answer is not None:
                    if answer['menu'] == "1. Ver el estado del punto de antención":
                        self._point_menu()
                    elif answer['menu'] == "2. Activar escritorio de servicio":
                        self._activate_desk()
                    elif answer['menu'] == "3. Desactivar escritorio de servicio":
                        self._deactivate_desk()
                    elif answer['menu'] == "4. Atender cliente":
                        self._attend_client()
                    elif answer['menu'] == "5. Solicitud de atención":
                        self._request_attend()
                    elif answer['menu'] == "6. Simular actividad de punto de atención":
                        self._simulate_activity()
                    elif answer['menu'] == "7. Regresar":
                        break
                    else:
                        print("No existe esta opción")

    def _point_menu(self) -> None:
        pass

    def _activate_desk(self) -> None:
        pass

    def _deactivate_desk(self) -> None:
        pass

    def _attend_client(self) -> None:
        pass

    def _request_attend(self) -> None:
        pass

    def _simulate_activity(self) -> None:
        pass
