import inquirer
from rich.console import Console

# Classes
from controller.classes.Client import Client
from controller.classes.TransactionClient import TransactionClient
from controller.classes.TransactionCompany import TransactionCompany

# Controllers
from controller.store.StoreData import StoreData
from model.docs.GenerateGraphvizDoc import GenerateGraphvizDoc
from model.simulation.Simulation import Simulation
from model.utils.ShowProperties import show_desk, show_desks
from model.utils.Utils import ask_yes_no


class Menu3:

    def manage_point_menu(self) -> None:
        if self.verify_if_data_exists():
            while True:
                options_main_menu = [
                    inquirer.List('menu',
                                  message="Seleccione una opción",
                                  choices=["1. Continuar/reanudar simulación de atención",
                                           "2. Activar escritorio de servicio",
                                           "3. Desactivar escritorio de servicio",
                                           "4. Atender cliente",
                                           "5. Solicitud de atención",
                                           "6. Simular actividad de punto de atención",
                                           "7. Regresar"])]
                answer = inquirer.prompt(questions=options_main_menu)
                if answer is not None:
                    if answer['menu'] == "1. Continuar/reanudar simulación de atención":
                        self._show_office_state()
                    elif answer['menu'] == "2. Activar escritorio de servicio":
                        self._activate_desk()
                    elif answer['menu'] == "3. Desactivar escritorio de servicio":
                        self._inactivate_desk()
                    elif answer['menu'] == "4. Atender cliente":
                        self._attend_client()
                    elif answer['menu'] == "5. Solicitud de atención":
                        self._create_new_client()
                    elif answer['menu'] == "6. Simular actividad de punto de atención":
                        self._simulate_activity()
                    elif answer['menu'] == "7. Regresar":
                        break
                    else:
                        print("No existe esta opción")

    def _show_office_state(self) -> None:
        if StoreData.selected_office is not None and StoreData.selected_company is not None:
            simulation = Simulation()
            simulation.execute_simulation()
        else:
            print("No hay un punto de atención seleccionado")

    def _activate_desk(self) -> None:
        if StoreData.selected_office.inactive_desks.get_size() > 0:
            Console().print("Escritorio activado", style="bold green")
            show_desks(StoreData.selected_office.active_desks, True)
            show_desk(StoreData.selected_office.active_desk_by_algorithm())
        else:
            Console().print("No hay escritorios disponibles", style="bold red")

    def _inactivate_desk(self) -> None:
        if StoreData.selected_office.active_desks.get_size() > 0:
            Console().print("Escritorio desactivado", style="bold green")
            show_desks(StoreData.selected_office.inactive_desks, False)
            show_desk(StoreData.selected_office.inactive_desk_by_algorithm())
        else:
            Console().print("No hay escritorios disponibles", style="bold red")

    def _attend_client(self) -> None:
        pass

    def _create_new_client(self) -> None:
        while True:
            Console().print("Creando nuevo cliente", style="bold blue")
            client_field: list[inquirer.Text] = [
                inquirer.Text('dpi', message="Ingrese el dpi del cliente"),
                inquirer.Text('name', message="Ingrese el nombre del cliente")]

            answer = inquirer.prompt(questions=client_field)
            if answer is not None:
                client = Client(answer['dpi'], answer['name'])
                StoreData.selected_office.add_client(client)
                Console().print("Cliente creado", style="bold green")
            self._create_transaction(client)
            if not ask_yes_no("¿Desea agregar otro cliente?"):
                break

    def _create_transaction(self, client: Client) -> None:
        while True:
            choices = []
            node = StoreData.selected_company.transactions.head
            for i in range(StoreData.selected_company.transactions.get_size()):
                choices.append(node.data.name)
                node = node.next

            Console().print(
                f"Agregar una nueva transacción para:{client.get_name()}")

            transaction_field: list[inquirer.Text] = [inquirer.List(
                'transaction', message="Seleccione una transacción", choices=choices)]

            quantity_field: list[inquirer.Text] = [inquirer.Text(
                'quantity', message="Ingrese la cantidad de transacciones", validate=lambda _, x: x.isdigit())]

            answer = inquirer.prompt(questions=transaction_field)
            answer_quantity = inquirer.prompt(questions=quantity_field)

            if answer is not None and answer_quantity is not None:
                transaction: TransactionCompany = StoreData.selected_company.search_transaction_by_name(
                    answer['transaction'])
                transaction_for_client: TransactionClient = TransactionClient(
                    transaction, answer_quantity['quantity'])

                client.add_transaction_for_client(transaction_for_client)
                Console().print("Transacción agregada", style="bold green")
                
                if not ask_yes_no("¿Desea agregar otra transacción?"):
                    break

    def _simulate_activity(self) -> None:
        Simulation().simulate_all()
        doc = GenerateGraphvizDoc()
        doc.generate_doc()

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
