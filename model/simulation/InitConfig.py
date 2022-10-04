from xml.dom.minidom import Element, parse
from rich.console import Console

# Classes
from controller.classes.Client import Client

from controller.store.StoreData import StoreData
from model.simulation.SystemConfig import SystemConfig

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
                id_config: str = initial_config.getAttribute("id")
                id_company: str = initial_config.getAttribute("idEmpresa")
                id_office: str = initial_config.getAttribute("idPunto")

                self.console.print(f"ID Configuración: {id_config}")
                self.console.print(f"ID Empresa: {id_company}")
                self.console.print(f"ID Punto: {id_office}")

                self.get_clients(initial_config)
            else:
                self.console.print("No hay configuración inicial")

        except FileNotFoundError:
            print("Ocurrió un error al leer el fichero")

    def get_clients(self, config_element: Element) -> None:
        # Get the list of clients
        list_of_clients: Element = config_element.getElementsByTagName(
            "listadoClientes")

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
                self.get_client_transactions(list_of_transactions)
            else:
                self.console.print("No hay transacciones", style="bold orange")

    def get_client_transactions(self, list_of_transactions: Element) -> None:
        # Get the list of transactions of the client
        transactions: Element = list_of_transactions.getElementsByTagName(
            "transaccion")

        # Traverse the list of transactions
        for transaction in transactions:

            # Set transaction as an Minidom Element
            transaction: Element

            # Get the attributes of the transaction
            id_transaction: str = transaction.getAttribute("id")
            date_transaction: str = transaction.getAttribute("fecha")
            amount_transaction: str = transaction.getAttribute("monto")
            type_transaction: str = transaction.getAttribute("tipo")

            self.console.print(f"ID Transacción: {id_transaction}")
            self.console.print(f"Fecha: {date_transaction}")
            self.console.print(f"Monto: {amount_transaction}")
            self.console.print(f"Tipo: {type_transaction}")

    def create_client(self, dpi: str, name: str) -> Client:
        new_client: Client = Client(dpi, name)
        return new_client

    def get_active_desks(self, config_element: Element) -> None:
        # Get the list of active desks
        list_of_active_desks: Element = config_element.getElementsByTagName(
            "listadoPuntosActivos")

        # Traverse the list of active desks
        for active_desk in list_of_active_desks:

            # Set active desk as an Minidom Element
            active_desk: Element

            # Get the attributes of the active desk
            id_active_desk: str = active_desk.getAttribute("idPunto")
            id_active_company: str = active_desk.getAttribute("idEmpresa")

            self.console.print(f"ID Punto: {id_active_desk}")
            self.console.print(f"ID Empresa: {id_active_company}")

    def get_transactions_list(self):
        pass
