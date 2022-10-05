from rich.table import Table
from rich.console import Console
from controller.base.NodeForSinglyList import NodeForSinglyList
from controller.base.Queue import Queue

# Structures
from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.base.Stack import Stack
from controller.classes.Client import Client

# Classes
from controller.classes.Company import Company
from controller.classes.Desk import Desk
from controller.classes.Office import Office
from controller.classes.TransactionClient import TransactionClient
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


def show_clients(clients: Queue) -> None:
    console = Console()
    if clients.is_empty():
        console.print("No hay clientes en cola", style="bold red")
    else:
        table = Table(show_header=True, header_style="bold blue",
                      title="Clientes en cola 📑")
        table.add_column("ID")
        table.add_column("Nombre")
        node = clients.items.head
        while node is not None:
            client: Client = node.data
            table.add_row(client.dpi, client.name)
            node = node.next
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
    table = Table(show_header=True, header_style="bold blue",
                  title="Punto de atención")
    table.add_column("ID")
    table.add_column("Nombre")
    table.add_column("Dirección")
    table.add_row(office.id_office, office.name, office.address)
    console.print(table)


def show_desks(list_of_desks: Stack, is_active: bool = False) -> None:
    console = Console()
    if list_of_desks.is_empty():
        console.print(
            "No hay escritorios registrados", style="bold red")
    else:

        # Create the table for the active desks
        title = "Escritorios activos" if is_active else "Escritorios inactivos"
        table = Table(show_header=True, header_style="bold blue",
                      title=f'{title}🖥')
        table.add_column("ID")
        table.add_column("Identificación")
        table.add_column("Encargado")
        node: NodeForSinglyList = list_of_desks.stack.head
        print(node.data)
        while node is not None:
            desk: Desk = node.data
            table.add_row(desk.id_desk, desk.correlative, desk.employee)
            node = node.next

        console.print(
            f'Cantidad de {"escritorios activos" if is_active else "escritorios inactivos"} {list_of_desks.get_size()}')
        console.print(table)


def show_desk(desk: Desk) -> None:
    console = Console()
    table = Table(show_header=True, header_style="bold blue",
                  title="Escritorio")
    table.add_column("ID")
    table.add_column("Identificación")
    table.add_column("Encargado")
    table.add_row(desk.id_desk, desk.correlative, desk.employee)
    console.print(table)


def show_transaction(transaction: TransactionCompany) -> None:
    console = Console()
    table = Table(show_header=True, header_style="bold blue",
                  title="Transacción 📑")
    table.add_column("ID")
    table.add_column("Nombre")
    table.add_column("Tiempo de atención")
    table.add_row(transaction.id_transaction,
                  transaction.name, transaction.time)
    console.print(table)


def show_office_state(office: Office) -> None:
    console = Console()

    table = Table(show_header=True, header_style="bold blue",
                  title="Estado del punto de atención seleccionado")
    table.add_column("Escritorios activos")
    table.add_column("Escritorios inactivos")
    table.add_column("Clientes en cola")
    table.add_column("Tiempo promedio de espera")
    table.add_column("Tiempo máximo de espera")
    table.add_column("Tiempo mínimo de espera")
    table.add_column("Tiempo promedio de atención")
    table.add_column("Tiempo máximo de atención")
    table.add_column("Tiempo mínimo de atención")

    table.add_row(
        f'{office.active_desks.get_size()}',
        f'{office.inactive_desks.get_size()}',
        f'{office.clients.get_size()}',
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        # office.average_waiting_time,
        # office.max_waiting_time,
        # office.min_waiting_time,
        # office.average_attendance_time,
        # office.max_attendance_time,
        # office.min_attendance_time
    )
    console.print(table)


def show_client_transactions(client: Client) -> None:
    console = Console()
    if client.transactions.is_empty():
        console.print("No hay transacciones registradas", style="bold red")
    else:
        table = Table(show_header=True, header_style="bold blue",
                      title=f"Transacciones 📑 de { client.name }")
        table.add_column("ID")
        table.add_column("Tiempo de atención")
        node = client.transactions.head
        while node is not None:
            transaction: TransactionClient = node.data
            table.add_row(transaction.get_id_transaction(),
                          transaction.get_quantity())
            node = node.next
        console.print(table)
