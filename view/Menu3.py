import inquirer
from rich.console import Console

# Classes
from controller.classes.Company import Company
from controller.classes.Office import Office

# Controllers
from controller.store.StoreData import StoreData
from model.utils.ShowProperties import show_desk, show_desks, show_office_state


class Menu3:

    def manage_point_menu(self) -> None:
        if self.verify_if_data_exists():
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
                        self._show_office_state()
                    elif answer['menu'] == "2. Activar escritorio de servicio":
                        self._activate_desk()
                    elif answer['menu'] == "3. Desactivar escritorio de servicio":
                        self._inactivate_desk()
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

    def _show_office_state(self) -> None:
        show_office_state(StoreData.selected_office) if StoreData.selected_office is not None else print(
            "No hay un punto de atención seleccionado")

    def _activate_desk(self) -> None:
        Console().print("Escritorio activado", style="bold green")
        show_desks(StoreData.selected_office.active_desks, True)
        show_desks(StoreData.selected_office.inactive_desks, False)
        show_desk(StoreData.selected_office.active_desk_by_algorithm())

    def _inactivate_desk(self) -> None:
        Console().print("Escritorio desactivado", style="bold green")
        show_desks(StoreData.selected_office.active_desks, True)
        show_desks(StoreData.selected_office.inactive_desks, False)
        show_desk(StoreData.selected_office.inactive_desk_by_algorithm())

    def _attend_client(self) -> None:
        pass

    def _request_attend(self) -> None:
        pass

    def _simulate_activity(self) -> None:
        pass

    def verify_if_data_exists(self) -> bool:

        Console().print("Verificando si hay empresas registradas", style="bold yellow")

        # Check if there are companies
        if StoreData.list_of_companies.get_size() == 0:
            Console().print("No hay empresas registradas", style="bold red")
            return False

        # Check if there are offices
        elif StoreData.selected_company is None:
            Console().print("No hay una empresa seleccionada", style="bold red")
            return False
        else:
            return True
