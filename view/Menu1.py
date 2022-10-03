from rich.console import Console
from rich.table import Table
import inquirer

from controller.classes.Company import Company
from controller.classes.Office import Office

from model.simulation.InitConfig import InitConfig
from model.simulation.SystemConfig import SystemConfig

# Utils
from model.utils.Utils import get_file


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
                    pass
                elif answer['menu'] == "5. Regresar":
                    break

    # Clear all the list of companies

    def _clear_system(self) -> None:
        if self.system_config.clear_system():
            print("Sistema limpio")
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
                              validate=lambda _, x: len(x) > 0),
                inquirer.Text('name', message="Nombre de la empresa",
                              validate=lambda _, x: len(x) > 0),
                inquirer.Text('acronym', message="Acrónimo de la empresa",
                              validate=lambda _, x: len(x) > 0),
            ]

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
                    self.system_config.show_company(new_company)

                    # Show menu to config company
                    self._company_config(new_company)
                else:
                    self.console.print("No se pudo crear la empresa",
                                       style="bold red")

            # Ask if the user wants to create a new company
            questions = [
                inquirer.List('menu',
                              message="¿Desea crear otra empresa?",
                              choices=["1. Si",
                                       "2. No"])]
            answer = inquirer.prompt(questions=questions)
            if answer is not None:
                if answer['menu'] == "1. Si":
                    pass
                elif answer['menu'] == "2. No":
                    break

    def _company_config(self, company) -> None:
        while True:
            # Ask if the user wants to create a new office
            questions_offices = [
                inquirer.List("create_office",
                              message="¿Desea crear una oficina?",
                              choices=["Sí", "No"])]
            answer_offices = inquirer.prompt(questions_offices)
            if answer_offices['create_office'] == "Sí":
                self._create_office_menu(company)
            else:
                break

    def _create_office_menu(self, company: Company) -> None:
        while True:
            self.console.print("Oficinas de la empresa", style="bold green")
            office_fields: list[inquirer.Text] = [
                inquirer.Text('id_office', message="Código de la oficina",
                              validate=lambda _, x: len(x) > 0),
                inquirer.Text('name', message="Nombre de la oficina",
                              validate=lambda _, x: len(x) > 0),
                inquirer.Text('acronym', message="Acrónimo de la oficina",
                              validate=lambda _, x: len(x) > 0),
            ]
            office_answers = inquirer.prompt(office_fields)
            if office_answers is not None:
                new_office = self.system_config.create_office(
                    office_answers['id_office'], office_answers['name'], office_answers['acronym'])
                if new_office is not None:
                    self.console.print("Oficina creada", style="bold green")
                    self.system_config.show_office(new_office)
                    company.add_office(new_office)
                else:
                    self.console.print("No se pudo crear la oficina",
                                       style="bold red")
            else:
                break

    def _create_desk(self, office: Office) -> None:
        while True:
            desk_fields: list[inquirer.Text] = [
                inquirer.Text('id_desk', message="Código de la mesa",
                              validate=lambda _, x: len(x) > 0),
                inquirer.Text('name', message="Nombre de la mesa",
                              validate=lambda _, x: len(x) > 0),
                inquirer.Text('acronym', message="Acrónimo de la mesa",
                              validate=lambda _, x: len(x) > 0),
            ]
            desk_answers = inquirer.prompt(desk_fields)
            if desk_answers is not None:
                new_desk = self.system_config.create_desk(
                    office, desk_answers['id_desk'], desk_answers['name'], desk_answers['acronym'])
                if new_desk is not None:
                    self.console.print("Mesa creada", style="bold green")
                    self.system_config.show_desk(new_desk)
                    office.add_desk(new_desk)
                else:
                    self.console.print(
                        "No se pudo crear la mesa", style="bold red")
            else:
                break

    def _create_transaction_menu(self, company: Company) -> None:
        while True:
            pass

    def _init_config(self) -> None:
        pass
