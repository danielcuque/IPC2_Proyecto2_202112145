from xml.dom.minidom import Element, parse

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

                new_company = Company(
                    int(company_id), company_name, company_acronym, offices_list)
                self.companyList.append(new_company)

            print(self.companyList)

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

    def get_desks(self, office: Element) -> SinglyLinkedList:
        desk_list: SinglyLinkedList = SinglyLinkedList()
        desks_element = office.getElementsByTagName("listaEscritorios")

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

    def get_transactions(self, company: Element) -> SinglyLinkedList:
        transactions_list: SinglyLinkedList = SinglyLinkedList()
        transactions_element = company.getElementsByTagName(
            "listaTransacciones")

        for transaction in transactions_element:
            transaction: Element

            transaction_id = transaction.getAttribute("id")
            transaction_name = transaction.getElementsByTagName("nombre")[
                0].firstChild.data
            transaction_time = transaction.getElementsByTagName("tiempoAtencion")[
                0].firstChild.data

            new_transaction = TransactionCompany(
                int(transaction_id), transaction_name, transaction_time)
            transactions_list.append(new_transaction)

        return transactions_list

    def system_init(self, path_file):
        pass
