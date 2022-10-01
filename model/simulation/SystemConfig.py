from xml.dom.minidom import Element, parse
from rich.console import Console
from rich.table import Table

from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.base.Stack import Stack
from controller.classes.Company import Company
from controller.classes.Desk import Desk
from controller.classes.Office import Office
from controller.classes.TransactionCompany import TransactionCompany


class SystemConfig:
    companyList: SinglyLinkedList = SinglyLinkedList()

    def system_config(self, path_file):
        try:
            system_info: Element = parse(path_file)
            company_list_element = system_info.getElementsByTagName("empresa")

            for company in company_list_element:
                company: Element

                company_id = company.getAttribute("id")
                company_name = company.getElementsByTagName("nombre")[
                    0].firstChild.data
                company_acronym = company.getElementsByTagName("abreviatura")[
                    0].firstChild.data
                offices_list: SinglyLinkedList = self.get_offices(company)
                transactions_list: SinglyLinkedList = self.get_transactions(
                    company)

                self.create_company(
                    company_id, company_name, company_acronym, offices_list, transactions_list)
            self.show_companies()

        except FileNotFoundError:
            print("Ocurrió un error al leer el fichero")

    def clear_system(self) -> str:
        self.companyList.clear()
        if self.companyList.is_empty():
            return "Sistema limpio"
        else:
            return "No se pudo limpiar el sistema"

    def create_company(self, id_company: str, name: str, acronym: str, offices: SinglyLinkedList,
                       transactions: SinglyLinkedList) -> str:
        if self.companyList.is_empty():
            new_company = Company(
                id_company, name, acronym, offices, transactions)
            self.companyList.insert_at_end(new_company)
            return "Empresa creada"
        else:
            node = self.companyList.head
            while node is not None:
                company: Company = node.data
                if company.id_company == id_company:
                    return "Ya existe una empresa con ese ID"
                node = node.next

            new_company = Company(
                id_company, name, acronym, offices, transactions)
            self.companyList.insert_at_end(new_company)
            return "Empresa creada"

    @staticmethod
    def create_office(id_office: str, name: str, address: str, desks: Stack) -> Office:
        new_office: Office = Office(id_office, name, address)
        new_office.set_inactive_desks(desks)
        return new_office

    @staticmethod
    def create_desk(id_desk: str, correlative: str, employee: str) -> Desk:
        return Desk(id_desk, correlative, employee)

    @staticmethod
    def create_transaction(id_transaction: str, name: str,  duration: str) -> TransactionCompany:
        return TransactionCompany(id_transaction, name, duration)

    def get_offices(self, company: Element) -> SinglyLinkedList:
        offices_list: SinglyLinkedList = SinglyLinkedList()
        offices_element = company.getElementsByTagName("puntoAtencion")

        for office in offices_element:
            office: Element

            office_id = office.getAttribute("id")
            office_name = office.getElementsByTagName("nombre")[
                0].firstChild.data
            office_address = office.getElementsByTagName("direccion")[
                0].firstChild.data
            office_desks: Stack = self.get_desks(office)

            new_office: Office = self.create_office(
                office_id, office_name, office_address, office_desks)

            offices_list.insert_at_end(new_office)

        return offices_list

    @staticmethod
    def get_desks(office: Element) -> Stack:
        desk_list: Stack = Stack()
        desks_element = office.getElementsByTagName("escritorio")

        for desk in desks_element:
            desk: Element

            desk_id = desk.getAttribute("id")
            desk_correlative = desk.getElementsByTagName("identificacion")[
                0].firstChild.data
            desk_employee = desk.getElementsByTagName("encargado")[
                0].firstChild.data

            new_desk = Desk(desk_id, desk_correlative, desk_employee)
            desk_list.push(new_desk)

        return desk_list

    @staticmethod
    def get_transactions(company: Element) -> SinglyLinkedList:
        transactions_list: SinglyLinkedList = SinglyLinkedList()
        transactions_element = company.getElementsByTagName(
            "transaccion")

        for transaction in transactions_element:
            transaction: Element

            transaction_id: str = transaction.getAttribute("id")
            transaction_name: str = transaction.getElementsByTagName("nombre")[
                0].firstChild.data
            transaction_time = transaction.getElementsByTagName("tiempoAtencion")[
                0].firstChild.data

            new_transaction = TransactionCompany(
                transaction_id, transaction_name, transaction_time)
            transactions_list.insert_at_end(new_transaction)

        return transactions_list

    def show_companies(self):
        if self.companyList.is_empty():
            return "No hay empresas registradas"
        else:
            node = self.companyList.head
            while node is not None:
                company: Company = node.data
                self.show_company_by_id(company.id_company)
                node = node.next
    
    def show_company_by_id(self, id_company: str) -> str or None:
        pass

    def show_office_by_id_company(self, id_company: str, id_office: str) -> str or None:
        pass

    def show_desk_by_id_office(self, id_company: str, id_office: str, id_desk: str) -> str or None:
        pass

    def show_transaction_by_id_company(self, id_company: str, id_transaction: str) -> str or None:
        pass

    def clear_system(self) -> bool:
        self.companyList.clear()
        if self.companyList.is_empty():
            return True
        
