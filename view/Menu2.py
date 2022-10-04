import inquirer
from rich.console import Console

# Structures
from controller.base.SinglyLinkedList import SinglyLinkedList

# Classes
from controller.classes.Company import Company
from controller.classes.Office import Office
from controller.store.StoreData import StoreData

# Controllers
from model.simulation.SystemConfig import SystemConfig

# Utils
from model.utils.ShowProperties import show_companies, show_company_by_id, show_company, show_offices, show_office, show_desks


class Menu2:

    system_config = SystemConfig()

    def select_company(self) -> None:
        companies: SinglyLinkedList = StoreData.list_of_companies
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
            StoreData.selected_company = StoreData.search_company_by_name(
                company_name)
            show_company(StoreData.selected_company)
            self.select_office(StoreData.selected_company)

    def select_office(self, company: Company) -> None:
        console = Console()
        choices = []
        if company.offices.is_empty():
            console.print("No hay oficinas registradas", style="bold red")
        else:
            node = company.offices.head
            while node is not None:
                office: Office = node.data
                choices.append(office.name)
                node = node.next

            options = [
                inquirer.List('office', message="Seleccione una oficina", choices=choices)]
            answer = inquirer.prompt(questions=options)
            if answer is not None:
                office_name = answer['office']
                StoreData.selected_office = company.search_office_by_name(office_name)

                show_office(StoreData.selected_office)
