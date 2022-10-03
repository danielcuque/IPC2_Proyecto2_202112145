import inquirer
from rich.console import Console

# Structures
from controller.base.SinglyLinkedList import SinglyLinkedList

# Classes
from controller.classes.Company import Company
from controller.classes.Office import Office

# Controllers
from model.simulation.SystemConfig import SystemConfig

# Utils
from model.utils.ShowProperties import show_companies, show_company_by_id, show_company, show_offices, show_office, show_desks


class Menu2:

    selected_office = None
    system_config = SystemConfig()

    def select_company(self) -> None:
        companies: SinglyLinkedList = self.system_config.list_of_companies
        choices = []
        if companies.is_empty():
            print("No hay empresas registradas")
        else:
            node = companies.head
            while node is not None:
                company: Company = node.data
                choices.append(company.name)
                node = node.next
        options = [
            inquirer.List('company', message="Seleccione una empresa", choices=choices)]
        answer = inquirer.prompt(questions=options)
        if answer is not None:
            company_name = answer['company']
            selected_company: Company = self.system_config.search_company_by_name(
                company_name)
            show_company(selected_company)
            self.select_office(selected_company.offices)

    def select_office(self, list_of_offices: SinglyLinkedList) -> None:
        console = Console()
        choices = []
        if list_of_offices.is_empty():
            console.print("No hay oficinas registradas", style="bold red")
        else:
            node = list_of_offices.head
            while node is not None:
                office: Office = node.data
                choices.append(office.name)
                node = node.next

            options = [
                inquirer.List('office', message="Seleccione una oficina", choices=choices)]
            answer = inquirer.prompt(questions=options)
            if answer is not None:
                office_name = answer['office']
                self.selected_office = self.system_config.search_office_by_name(
                    list_of_offices, office_name)
                    
                show_office(self.selected_office)
