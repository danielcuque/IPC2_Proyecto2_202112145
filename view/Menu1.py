from wsgiref import validate
from rich.console import Console
from rich.table import Table
import inquirer

from controller.classes.Company import Company
from controller.classes.Office import Office
from controller.store.StoreData import StoreData

from model.simulation.InitConfig import InitConfig
from model.simulation.SystemConfig import SystemConfig

# Utils
from model.utils.Utils import get_file, ask_yes_no
from model.utils.ShowProperties import show_companies, show_company_by_id, show_company, show_offices, show_office, show_desks, show_desk, show_transaction


class Menu1:

    # Init instances
    system_config = SystemConfig()
    init_config = InitConfig()
    console = Console()

    # Main menu for the system
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
                    self._init_config()
                elif answer['menu'] == "5. Regresar":
                    break

    # Clear all the list of companies

    def _clear_system(self) -> None:
        if self.system_config.clear_system():
            self.console.print("Sistema limpio", style="bold green")
        else:
            print("No se pudo limpiar el sistema")

    # Load xml file with the system configuration

    def _system_config(self) -> None:
        path_file = get_file()
        if path_file:
            self.system_config.system_config(path_file)
        else:
            print("No existe el fichero")

    # Create a new company
    def _create_company_menu(self):
        while True:

            # Get the company fields
            self.console.print("Crear empresa", style="bold green")
            company_fields: list[inquirer.Text] = [
                inquirer.Text('id_company', message="Código de la empresa",
                              validate=lambda _, x: len(x) > 0 and not self.valite_if_company_exist(x)),
                inquirer.Text('name', message="Nombre de la empresa",
                              validate=lambda _, x: len(x) > 0),
                inquirer.Text('acronym', message="Acrónimo de la empresa",
                              validate=lambda _, x: len(x) > 0)]

            # Get the answers
            company_answers = inquirer.prompt(company_fields)

            # If the answers are not empty
            if company_answers is not None:

                # Create a new company
                new_company: Company = self.system_config.create_company(
                    company_answers['id_company'], company_answers['name'], company_answers['acronym'])

                # If the company is not None
                if new_company is not None:

                    # Show the company
                    self.console.print("Empresa creada", style="bold green")
                    show_company(new_company)

                    # Show menu to config company
                    self._company_config(new_company)
                else:
                    self.console.print("No se pudo crear la empresa",
                                       style="bold red")

            # Ask if the user wants to create a new company
            if not ask_yes_no("¿Desea crear una nueva empresa?"):
                break

    def _company_config(self, company) -> None:

        # Show the company until the user wants to exit
        while True:
            # Ask if the user wants to create a new office or new transaction
            questions_config = [
                inquirer.List("config_company",
                              message="Configuración de la empresa",
                              choices=["1. Crear oficina",
                                       "2. Crear transacción",
                                       "3. Regresar", ])]

            # Get the answer
            answer_config = inquirer.prompt(questions_config)

            # If the answer is not empty
            if answer_config is not None:

                # If the user wants to create a new office
                if answer_config['config_company'] == "1. Crear oficina":
                    self._create_office_menu(company)

                # If the user wants to create a new transaction
                elif answer_config['config_company'] == "2. Crear transacción":
                    self._create_transaction_menu(company)

                # If the user wants to go back
                elif answer_config['config_company'] == "3. Regresar":
                    break

    def _create_office_menu(self, company: Company) -> None:

        # Show the company until the user wants to exit
        while True:

            # Get the office fields
            self.console.print(
                "Puntos de atención de la empresa", style="bold green")
            office_fields: list[inquirer.Text] = [
                inquirer.Text('id_office', message="Código del punto de venta",
                              validate=lambda _, x: len(x) > 0),
                inquirer.Text('name', message="Nombre del punto de venta",
                              validate=lambda _, x: len(x) > 0),
                inquirer.Text('address', message="Dirección del punto de venta",
                              validate=lambda _, x: len(x) > 0)]

            # Get the answers
            office_answers = inquirer.prompt(office_fields)

            # If the answers are not empty
            if office_answers is not None:

                # Create a new office
                new_office = self.system_config.create_office(
                    office_answers['id_office'], office_answers['name'], office_answers['address'])

                # If the office is not None
                if new_office is not None:

                    # Show the office
                    self.console.print(
                        "Punto de venta creado", style="bold green")
                    show_office(new_office)

                    # Add the new office to the company
                    company.add_office(new_office)

                    # Show the menu to create a new desk for the office
                    self._create_desk_menu(new_office)
                else:
                    self.console.print("No se pudo crear el punto de venta",
                                       style="bold red")

            # Ask if the user wants to create a new office
            if not ask_yes_no("¿Desea crear un nuevo punto de venta?"):
                break

    # Menu to create a new desk active/inactive
    def _create_desk_menu(self, office: Office) -> None:
        while True:
            self.console.print("Nuevo escrotorio", style="bold green")
            desk_options = [
                inquirer.List('desk_type',
                              message="Seleccione el tipo de escritorio",
                              choices=["1. Activo",
                                       "2. Inactivo",
                                       "3. Regresar", ])]
            desk_answer = inquirer.prompt(desk_options)
            if desk_answer is not None:
                if desk_answer['desk_type'] == "1. Activo":
                    self._create_desk(office, True)
                elif desk_answer['desk_type'] == "2. Inactivo":
                    self._create_desk(office, False)
                elif desk_answer['desk_type'] == "3. Regresar":
                    break

            if not ask_yes_no("¿Desea crear un nuevo escritorio?"):
                break

    def _create_desk(self, office: Office, is_active: bool = False) -> None:
        desk_fields: list[inquirer.Text] = [
            inquirer.Text('id_desk', message="Código de escritorio",
                          validate=lambda _, x: len(x) > 0),
            inquirer.Text('name', message="Nombre de escritorio",
                          validate=lambda _, x: len(x) > 0),
            inquirer.Text('employee', message="Encargado de escritorio",
                          validate=lambda _, x: len(x) > 0),
        ]
        desk_answers = inquirer.prompt(desk_fields)
        if desk_answers is not None:
            new_desk = self.system_config.create_desk(
                desk_answers['id_desk'], desk_answers['name'], desk_answers['employee'])
            if new_desk is not None:
                self.console.print(
                    "Escritorio creado", style="bold green")
                show_desk(new_desk)
                if is_active:
                    office.add_active_desk(new_desk)
                    self.console.print(
                        "Escritorio activo creado", style="bold green")
                else:
                    office.add_inactive_desk(new_desk)
                    self.console.print(
                        "Escritorio inactivo creado", style="bold green")
            else:
                self.console.print(
                    "No se pudo crear el escritorio", style="bold red")

    def _create_transaction_menu(self, company: Company) -> None:
        # Show the menu until the user select the option to go back
        while True:
            # Ask if the user wants to create a new transaction
            transaction_fields: list[inquirer.Text] = [
                inquirer.Text('id_transaction', message="Código de la transacción",
                              validate=lambda _, x: len(x) > 0),
                inquirer.Text('name', message="Nombre de la transacción"),
                inquirer.Text('time', message="Tiempo de transacción", validate=lambda _, x: len(x) > 0 and x.isdigit())]

            transaction_answers = inquirer.prompt(transaction_fields)
            if transaction_answers is not None:
                new_transaction = self.system_config.create_transaction(
                    transaction_answers['id_transaction'], transaction_answers['name'], transaction_answers['time'])
                if new_transaction is not None:
                    self.console.print(
                        "Transacción creada", style="bold green")
                    show_transaction(new_transaction)
                    company.add_transaction(new_transaction)
                    self.console.print(
                        "Transacción agregada a la empresa", style="bold green")
                else:
                    self.console.print(
                        "No se pudo crear la transacción", style="bold red")

            if not ask_yes_no("¿Desear crear una nueva transacción?"):
                break

    def _init_config(self) -> None:
        if StoreData.list_of_companies.is_empty():
            self.console.print(
                "No hay empresas configuradas", style="bold red")
        else:
            path_file: str = get_file()
            if path_file is not None:
                self.init_config.init_config(path_file)
                self.console.print(
                    "Configuración inicializada", style="bold green")
            else:
                self.console.print("No se pudo inicializar la configuración",
                                   style="bold red")

    def valite_if_company_exist(self, id_company: str) -> bool:
        return self.system_config.search_company_by_id(id_company) is not None
