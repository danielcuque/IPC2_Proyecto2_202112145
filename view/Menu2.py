import inquirer

# Structures
from controller.base.SinglyLinkedList import SinglyLinkedList

# Classes
from controller.classes.Company import Company

# Controllers
from model.simulation.SystemConfig import SystemConfig

# Utils
from model.utils.ShowProperties import show_companies, show_company_by_id, show_company, show_offices, show_office, show_desks


class Menu2:

    selected_office = None
    companies: SinglyLinkedList = SystemConfig().list_of_companies

    def select_company(self) -> None:
        while True:
            choices = []

            if self.companies.is_empty():
                print("No hay empresas registradas")
                break
            else:
                node = self.companies.head
                while node is not None:
                    company = node.data
                    choices.append(company.name)
                    node = node.next

            options = [
                inquirer.List('company', message="Seleccione una empresa", choices=choices)]

            answer = inquirer.prompt(questions=options)
            if answer is not None:
                company: Company = answer['company']
                self.selected_office = company.offices
