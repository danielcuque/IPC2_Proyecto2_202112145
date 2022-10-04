from xml.dom.minidom import Element, parse
from rich.console import Console

# Classes
from controller.classes.Client import Client
from controller.classes.Company import Company
from controller.classes.Desk import Desk
from controller.classes.Office import Office
from controller.classes.TransactionClient import TransactionClient

from controller.store.StoreData import StoreData
from model.simulation.SystemConfig import SystemConfig

from model.utils.ShowProperties import show_company, show_office, show_companies, show_company_by_id


class InitConfig:

    console = Console()
    system_config = SystemConfig()

    def init_config(self, path_file):
        try:
            init_info: Element = parse(path_file)

            initial_config: Element = init_info.getElementsByTagName(
                "configInicial")

            if len(initial_config) > 0:
                initial_config: Element = initial_config[0]
                # id_config: str = initial_config.getAttribute("id")
                id_company: str = initial_config.getAttribute("idEmpresa")
                id_office: str = initial_config.getAttribute("idPunto")

                search_company = StoreData.search_company_by_id(id_company)
                if search_company is not None:
                    search_office = search_company.search_office_by_id(
                        id_office)
                    if search_office is not None:

                        # Active desks
                        self.get_active_desks(initial_config, search_office)

                        # Clients
                        self.get_clients(initial_config, search_office)
                    else:
                        self.console.print(
                            "No se encontro el punto de venta", style="bold red")

                self.get_clients(initial_config)
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
            id_active_desk: str = active_desk.getAttribute("idPunto")
            
            # Add the active desk to the list of active desks of the office
            desk_for_change_state: Desk = office.search_desk_by_id(id_active_desk)
            if desk_for_change_state is not None:
                pass

    def get_transactions_for_clients(self, list_of_transactions_element: Element, client: Client):
        list_of_transactions: Element = list_of_transactions_element.getElementsByTagName(
            "transaccion")

        for transaction in list_of_transactions:
            transaction: Element

            id_transaction: str = transaction.getAttribute("idTransaccion")
            quantity: str = transaction.getAttribute("cantidad")

            new_transaction: TransactionClient = self.create_transaction(
                id_transaction, quantity)
            client.add_transaction_for_client(new_transaction)

    def get_clients(self, config_element: Element, office: Office) -> None:
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
                    list_of_transactions, new_client)
            else:
                self.console.print("No hay transacciones", style="bold orange")

            # Add the client to the list of clients of the office
            office.add_client(new_client)
