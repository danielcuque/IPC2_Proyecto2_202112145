from xml.dom.minidom import Element, parse
from texttable import Texttable

from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.classes.Company import Company
from controller.classes.Desk import Desk
from controller.classes.Office import Office
from controller.classes.TransactionCompany import TransactionCompany


class InitialConfig:
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
                transactions_list: SinglyLinkedList = self.get_transactions(company)
                new_company = Company(
                    int(company_id), company_name, company_acronym, offices_list, transactions_list)
                self.companyList.append(new_company)

            self.show_companies()

        except FileNotFoundError:
            print("Ocurrió un error al leer el fichero")

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
            office_desks: SinglyLinkedList = self.get_desks(office)

            new_office = Office(office_id, office_name,
                                office_address, office_desks)
            offices_list.append(new_office)

        return offices_list

    @staticmethod
    def get_desks(office: Element) -> SinglyLinkedList:
        desk_list: SinglyLinkedList = SinglyLinkedList()
        desks_element = office.getElementsByTagName("escritorio")

        for desk in desks_element:
            desk: Element

            desk_id = desk.getAttribute("id")
            desk_correlative = desk.getElementsByTagName("identificacion")[
                0].firstChild.data
            desk_employee = desk.getElementsByTagName("encargado")[
                0].firstChild.data

            new_desk = Desk(int(desk_id), desk_correlative, desk_employee)
            desk_list.append(new_desk)

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
                int(transaction_id), transaction_name, transaction_time)
            transactions_list.append(new_transaction)

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

    def show_company_by_id(self, id_company: int):
        if self.companyList.is_empty():
            return "No hay empresas registradas"
        else:
            node = self.companyList.head
            while node is not None:
                company: Company = node.data
                if company.id_company == id_company:
                    table = Texttable()
                    table.set_deco(Texttable.HEADER)
                    table.set_max_width(100)
                    table.set_cols_align(["l", "l", "c"])
                    table.set_cols_valign(["m", "m", "m"])
                    table.header(["ID Empresa", "Nombre", "Abreviatura"])
                    table.add_row([
                        company.id_company,
                        company.name,
                        company.acronym,
                    ])
                    print(f'Empresa: {company.name}\n'
                          f'{table.draw()}\n'
                          f'Oficinas: {company.offices.size}\n'
                          f'{self.show_offices(company.offices)}\n'
                          f'Transacciones: {company.transactions.size}\n'
                          f'{self.show_transactions(company.transactions)}\n\n\n')
                    break
                node = node.next

    def show_offices(self, offices_list: SinglyLinkedList) -> str:
        if offices_list.is_empty():
            return "No hay puntos de atención registrados"
        else:
            table = Texttable()
            table.set_max_width(100)
            table.set_deco(Texttable.HEADER)
            table.set_cols_align(["l", "l", "l", "c"])
            table.set_cols_valign(["m", "m", "m", "m"])
            table.header(["ID Oficina", "Nombre", "Dirección", "Escritorios"])
            node = offices_list.head
            while node is not None:
                office: Office = node.data
                table.add_row([
                    office.id_office,
                    office.name,
                    office.address,
                    self.show_desks(office.desks)
                ])
                node = node.next

            return table.draw()

    @staticmethod
    def show_desks(desks_list: SinglyLinkedList) -> str:
        if desks_list.is_empty():
            return "No hay escritorios registrados"
        else:
            table = Texttable()
            table.set_deco(Texttable.HEADER)
            table.set_cols_align(["l", "l", "l"])
            table.set_cols_valign(["m", "m", "m"])

            table.header(["ID Escritorio", "Identificación", "Encargado"])
            node = desks_list.head
            while node is not None:
                desk: Desk = node.data
                table.add_row([
                    desk.id_desk,
                    desk.correlative,
                    desk.employee,
                ])

                node = node.next
            return table.draw()

    @staticmethod
    def show_transactions(transactions_list: SinglyLinkedList) -> str:
        if transactions_list.is_empty():
            return "No hay transacciones registradas"
        else:
            table = Texttable()
            table.set_deco(Texttable.HEADER)
            table.set_cols_align(["l", "l", "l"])
            table.set_cols_valign(["m", "m", "m"])

            table.header(["ID", "Nombre", "Tiempo de atención"])
            node = transactions_list.head
            while node is not None:
                transaction: TransactionCompany = node.data
                table.add_row([
                    transaction.id_transaction,
                    transaction.name,
                    transaction.time
                ])

                node = node.next
            return table.draw()

    def system_init(self, path_file):
        pass
