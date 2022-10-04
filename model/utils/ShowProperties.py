from rich.table import Table
from rich.console import Console

# Structures
from controller.base.SinglyLinkedList import SinglyLinkedList

# Classes
from controller.classes.Company import Company
from controller.classes.Desk import Desk
from controller.classes.Office import Office
from controller.classes.TransactionCompany import TransactionCompany


def show_companies(list_of_companies: SinglyLinkedList) -> None:
    console = Console()
    if list_of_companies.is_empty():
        print("No hay empresas registradas")
    else:
        # Create the table for the companies
        table = Table(show_header=True,
                      header_style="bold blue", title="Empresas")
        table.add_column("ID")
        table.add_column("Nombre")
        table.add_column("Abreviatura")
        node = list_of_companies.head
        while node is not None:
            company: Company = node.data
            table.add_row(company.id_company,
                          company.name, company.acronym)
            node = node.next
        console.print(table)


def show_company_by_id(list_of_companies: SinglyLinkedList, id_company: str) -> str or None:
    node = list_of_companies.head
    while node is not None:
        company: Company = node.data
        if company.id_company == id_company:
            return show_company(company)
        node = node.next


def show_company(company: Company) -> None:
    console = Console()
    table = Table(show_header=True, header_style="bold blue", title="Empresa")
    table.add_column("ID")
    table.add_column("Nombre")
    table.add_column("Abreviatura")
    table.add_row(company.id_company, company.name, company.acronym)
    console.print(table)


def show_offices(company: Company) -> None:
    if company.offices.is_empty():
        print("No hay oficinas registradas")
    else:
        node = company.offices.head
        while node is not None:
            office: Office = node.data
            show_office(office)
            show_desks(office)
            node = node.next


def show_office(office: Office) -> None:
    console = Console()
    table = Table(show_header=True, header_style="bold blue", title="Punto de atención")
    table.add_column("ID")
    table.add_column("Nombre")
    table.add_column("Dirección")
    table.add_row(office.id_office, office.name, office.address)
    console.print(table)


def show_desks(office: Office) -> None:
    console = Console()
    if office.active_desks.is_empty() and office.inactive_desks.is_empty():
        console.print(
            "No hay escritorios registrados", style="bold red")
    else:
        console.print()
        node = office.get_head_active_desks()
        while node is not None:
            desk: Desk = node.data
            show_desk(desk)
            node = node.next
        node = office.get_head_inactive_desks()
        while node is not None:
            desk: Desk = node.data
            show_desk(desk)
            node = node.next

def show_desk( desk: Desk) -> None:
    console = Console()
    table = Table(show_header=True, header_style="bold blue", title="Escritorio")
    table.add_column("ID")
    table.add_column("Identificación")
    table.add_column("Encargado")
    table.add_row(desk.id_desk, desk.correlative, desk.employee)
    console.print(table)

def show_transaction(transaction: TransactionCompany) -> None:
    console = Console()
    table = Table(show_header=True, header_style="bold blue",
                  title="Transacción")
    table.add_column("ID")
    table.add_column("Nombre")
    table.add_column("Tiempo de atención")
    table.add_row(transaction.id_transaction,
                  transaction.name, transaction.time)
    console.print(table)
