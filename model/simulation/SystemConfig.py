from xml.dom.minidom import Element, parse
from rich.console import Console
from rich.table import Table

# Structures
from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.base.Stack import Stack

# Classes
from controller.classes.Company import Company
from controller.classes.Desk import Desk
from controller.classes.Office import Office
from controller.classes.TransactionCompany import TransactionCompany


class SystemConfig:
    companyList: SinglyLinkedList = SinglyLinkedList()
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

            self.show_companies()

        except FileNotFoundError:
            print("Ocurrió un error al leer el fichero")

    def clear_system(self) -> str:
        self.companyList.clear()
        if self.companyList.is_empty():
            return "Sistema limpio"
        else:
            return "No se pudo limpiar el sistema"

    def create_company(self, id_company: str, name: str, acronym: str) -> Company:
        new_company: Company = Company(id_company, name, acronym)
        self.companyList.insert_at_end(new_company)
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

    def show_companies(self) -> None:
        if self.companyList.is_empty():
            print("No hay empresas registradas")
        else:

            # Create the table for the companies
            table = Table(show_header=True, header_style="bold blue", title="Empresas")
            table.add_column("ID")
            table.add_column("Nombre")
            table.add_column("Abreviatura")

            node = self.companyList.head
            while node is not None:
                company: Company = node.data
                table.add_row(company.id_company,
                              company.name, company.acronym)
                node = node.next

            self.console.print(table)

    def show_company_by_id(self, id_company: str) -> str or None:
        node = self.companyList.head
        while node is not None:
            company: Company = node.data
            if company.id_company == id_company:
                return self.show_company(company)
            node = node.next

    def show_company(self, company: Company) -> None:
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("ID")
        table.add_column("Nombre")
        table.add_column("Abreviatura")
        table.add_row(company.id_company, company.name, company.acronym)
        self.console.print(table)

    def show_offices(self, company: Company) -> None:
        if company.offices.is_empty():
            print("No hay oficinas registradas")
        else:
            node = company.offices.head
            while node is not None:
                office: Office = node.data
                self.show_office(office)
                self.show_desks(office)
                node = node.next

    def show_office(self, office: Office) -> None:
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("ID")
        table.add_column("Nombre")
        table.add_column("Dirección")
        table.add_row(office.id_office, office.name, office.address)
        self.console.print(table)

    def show_desks(self, office: Office) -> None:
        if office.active_desks.is_empty() and office.inactive_desks.is_empty():
            self.console.print(
                "No hay escritorios registrados", style="bold red")
        else:
            self.console.print()
            node = office.get_head_active_desks()
            while node is not None:
                desk: Desk = node.data
                self.show_desk(desk)
                node = node.next

            node = office.get_head_inactive_desks()
            while node is not None:
                desk: Desk = node.data
                self.show_desk(desk)
                node = node.next

    def show_desk(self, desk: Desk) -> None:
        self.console = Console()
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("ID")
        table.add_column("Identificación")
        table.add_column("Encargado")
        table.add_row(desk.id_desk, desk.correlative, desk.employee)
        self.console.print(table)

    def show_transaction(self, transaction: TransactionCompany) -> None:
        self.console = Console()
        table = Table(show_header=True, header_style="bold blue", title="Transacción")
        table.add_column("ID")
        table.add_column("Nombre")
        table.add_column("Tiempo de atención")
        table.add_row(transaction.id_transaction,
                      transaction.name, transaction.time)
        self.console.print(table)

    def show_office_by_id_company(self, id_company: str, id_office: str) -> str or None:
        pass

    def show_desk_by_id_office(self, id_company: str, id_office: str, id_desk: str) -> str or None:
        pass

    def show_transaction_by_id_company(self, id_company: str, id_transaction: str) -> str or None:
        pass

    def clear_system(self) -> bool:
        self.companyList.clear()
        return self.companyList.is_empty()
