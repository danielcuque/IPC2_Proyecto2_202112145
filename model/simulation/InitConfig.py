from xml.dom.minidom import Element, parse
from rich.console import Console

# Classes
from controller.classes.Client import Client
from controller.classes.Company import Company
from controller.classes.Desk import Desk
from controller.classes.Office import Office
from controller.classes.TransactionClient import TransactionClient
from controller.classes.TransactionCompany import TransactionCompany

from controller.store.StoreData import StoreData
from model.simulation.SystemConfig import SystemConfig

from model.utils.ShowProperties import show_client_transactions, show_clients, show_company, show_desk, show_desks, show_office, show_companies, show_company_by_id, show_transaction_company


class InitConfig:

    console = Console()
    system_config = SystemConfig()

    def init_config(self, path_file):
        try:
            init_info: Element = parse(path_file)

            initial_config: Element = init_info.getElementsByTagName(
                "configInicial")

            for config in initial_config:
                config: Element
                id_company: str = config.getAttribute("idEmpresa")
                id_office: str = config.getAttribute("idPunto")

                search_company = StoreData.search_company_by_id(id_company)
                if search_company is not None:
                    search_office = search_company.search_office_by_id(
                        id_office)
                    if search_office is not None:
                        # Active desks
                        self.get_active_desks(config, search_office)

                        # Clients
                        self.get_clients(config, search_office, search_company)
                        show_clients(search_office.clients)
                    else:
                        self.console.print(
                            "No se encontro el punto de venta", style="bold red")
            else:
                self.console.print("No hay configuración inicial")

        except FileNotFoundError:
            print("Ocurrió un error al leer el fichero")

    def create_client(self, dpi: str, name: str) -> Client:
        new_client: Client = Client(dpi, name)
        return new_client

    def create_transaction(self, id_transaction: str, quantity: str) -> TransactionClient:
        new_transaction: TransactionClient = TransactionClient(
            id_transaction, quantity)
        return new_transaction

    def get_active_desks(self, config_element: Element, office: Office) -> None:
        # Get the list of active desks
        list_of_active_desks: Element = config_element.getElementsByTagName(
            "escritorio")
        # Traverse the list of active desks
        for active_desk in list_of_active_desks:

            # Set active desk as an Minidom Element
            active_desk: Element

            # Get the attributes of the active desk
            id_active_desk: str = active_desk.getAttribute("idEscritorio")

            # Search the active desk in the list of inactive desks
            desk_for_change_state: Desk = office.search_desk_by_id(
                id_active_desk)

            # If the desk is not None, change the state of the desk
            if desk_for_change_state is not None:

                # Pop by index due the desk could not be ordered
                inactive_desk_for_change = office.inactive_desks.pop_by_index(
                    office.get_index_of_desk(desk_for_change_state))

                # Change the state of the desk
                desk: Desk = inactive_desk_for_change.data
                office.add_active_desk(desk)
            else:
                self.console.print(
                    f'No se encontró el escritorio {id_active_desk}', style="bold red")
        show_desks(office.active_desks, True)

    def get_clients(self, config_element: Element, office: Office, company: Company) -> None:
        # Get the list of clients
        list_of_clients: Element = config_element.getElementsByTagName(
            "cliente")

        # Traverse the list of clients
        for client in list_of_clients:

            # Set client as an Minidom Element
            client: Element

            # Get the attributes of the client
            dpi_client: str = client.getAttribute("dpi")
            name_client: str = client.getElementsByTagName("nombre")[
                0].firstChild.data

            new_client: Client = self.create_client(dpi_client, name_client)

            # Get the list of transactions of the client
            list_of_transactions: Element = client.getElementsByTagName(
                "listadoTransacciones")

            if len(list_of_transactions) > 0:
                list_of_transactions: Element = list_of_transactions[0]
                self.get_transactions_for_clients(
                    list_of_transactions, new_client, company)

            else:
                self.console.print("No hay transacciones", style="bold orange")

            show_client_transactions(new_client)

            # Add the client to the list of clients of the office
            office.add_client(new_client)

    def get_transactions_for_clients(self, list_of_transactions_element: Element, client: Client, company: Company) -> None:
        list_of_transactions: Element = list_of_transactions_element.getElementsByTagName(
            "transaccion")

        for transaction in list_of_transactions:
            transaction: Element

            id_transaction: str = transaction.getAttribute("idTransaccion")
            quantity: str = transaction.getAttribute("cantidad")

            transaction_company: TransactionCompany = company.search_transaction_by_id(
                id_transaction)

            if transaction_company is not None:
                new_transaction: TransactionClient = self.create_transaction(
                    id_transaction, quantity)
                client.add_transaction_for_client(new_transaction)
            else:
                self.console.print(
                    f'No se encontró la transacción {id_transaction}', style="bold red")
