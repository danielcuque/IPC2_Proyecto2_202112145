from xml.dom.minidom import Element, parse
from rich.console import Console
from controller.base.NodeForSinglyList import NodeForSinglyList


# Structures
from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.base.Stack import Stack

# Classes
from controller.classes.Company import Company
from controller.classes.Desk import Desk
from controller.classes.Office import Office
from controller.classes.TransactionCompany import TransactionCompany
from controller.store.StoreData import StoreData

# Utils
from model.utils.ShowProperties import show_companies


class SystemConfig:
    console = Console()

    def system_config(self, path_file):
        try:
            system_info: Element = parse(path_file)
            company_list_element = system_info.getElementsByTagName("empresa")

            for company_element in company_list_element:
                company_element: Element

                company_id = company_element.getAttribute("id")
                company_name = company_element.getElementsByTagName("nombre")[
                    0].firstChild.data
                company_acronym = company_element.getElementsByTagName("abreviatura")[
                    0].firstChild.data

                new_company: Company = self.create_company(
                    company_id, company_name, company_acronym)

                self.get_offices(company_element, new_company)
                self.get_transactions(
                    company_element, new_company)

            show_companies(StoreData.list_of_companies)

        except FileNotFoundError:
            print("Ocurrió un error al leer el fichero")

    def clear_system(self) -> str:
        StoreData.list_of_companies.clear()
        if StoreData.list_of_companies.is_empty():
            return "Sistema limpio"
        else:
            return "No se pudo limpiar el sistema"

    def create_company(self, id_company: str, name: str, acronym: str) -> Company:
        new_company: Company = Company(id_company, name, acronym)
        StoreData.list_of_companies.insert_at_end(new_company)
        return new_company

    @staticmethod
    def create_office(id_office: str, name: str, address: str) -> Office:
        new_office: Office = Office(id_office, name, address)
        return new_office

    @staticmethod
    def create_desk(id_desk: str, correlative: str, employee: str) -> Desk:
        return Desk(id_desk, correlative, employee)

    @staticmethod
    def create_transaction(id_transaction: str, name: str,  duration: str) -> TransactionCompany:
        return TransactionCompany(id_transaction, name, duration)

    def get_offices(self, company_element: Element, company_to_insert: Company) -> bool:
        offices_element = company_element.getElementsByTagName("puntoAtencion")

        for office in offices_element:
            office: Element

            office_id = office.getAttribute("id")
            office_name = office.getElementsByTagName("nombre")[
                0].firstChild.data
            office_address = office.getElementsByTagName("direccion")[
                0].firstChild.data
            office_desks: Stack = self.get_desks(office)

            new_office: Office = self.create_office(
                office_id, office_name, office_address)

            new_office.set_inactive_desks(office_desks)

            company_to_insert.add_office(new_office)

        return company_to_insert.offices.is_empty()

    def get_desks(self, office: Element) -> Stack:
        desk_list: Stack = Stack()
        desks_element = office.getElementsByTagName("escritorio")

        for desk in desks_element:
            desk: Element

            desk_id = desk.getAttribute("id")
            desk_correlative = desk.getElementsByTagName("identificacion")[
                0].firstChild.data
            desk_employee = desk.getElementsByTagName("encargado")[
                0].firstChild.data

            new_desk = self.create_desk(
                desk_id, desk_correlative, desk_employee)
            desk_list.push(new_desk)
        return desk_list

    def get_transactions(self, company_element: Element, company_to_insert: Company) -> bool:
        transactions_element = company_element.getElementsByTagName(
            "transaccion")
        for transaction in transactions_element:
            transaction: Element

            transaction_id: str = transaction.getAttribute("id")
            transaction_name: str = transaction.getElementsByTagName("nombre")[
                0].firstChild.data
            transaction_time = transaction.getElementsByTagName("tiempoAtencion")[
                0].firstChild.data

            new_transaction = self.create_transaction(
                transaction_id, transaction_name, transaction_time)

            company_to_insert.add_transaction(new_transaction)

        return company_to_insert.transactions.is_empty()

    def clear_system(self) -> bool:
        StoreData.list_of_companies.clear()
        return StoreData.list_of_companies.is_empty()

    def search_company_by_name(self, name: str) -> Company:
        node: NodeForSinglyList = StoreData.list_of_companies.head
        while node is not None:
            company: Company = node.data
            if company.name == name:
                return company
            node = node.next
        return None

    def search_company_by_id(self, id_company: str) -> Company:
        node: NodeForSinglyList = StoreData.list_of_companies.head
        while node is not None:
            company: Company = node.data
            if company.id_company == id_company:
                return company
            node = node.next
        return None

    @staticmethod
    def search_office_by_name(list_of_offices: SinglyLinkedList, office_name: str) -> Office:
        node: NodeForSinglyList = list_of_offices.head
        while node is not None:
            office: Office = node.data
            if office.name == office_name:
                return office
            node = node.next
        return None

    @staticmethod
    def search_office_by_id(list_of_offices: SinglyLinkedList, id_office: str) -> Office:
        node: NodeForSinglyList = list_of_offices.head
        while node is not None:
            office: Office = node.data
            if office.id_office == id_office:
                return office
            node = node.next
        return None
