import inquirer
from rich.console import Console
from controller.base.SinglyLinkedList import SinglyLinkedList

# Classes
from controller.classes.Client import Client
from controller.classes.Desk import Desk
from controller.classes.TransactionClient import TransactionClient


from controller.store.StoreData import StoreData
from model.utils.ShowProperties import show_transaction_client


class Simulation:

    def execute_simulation(self):
        while self.verify_data():
            self.show_principal_info()
            question = [
                inquirer.List('menu',
                              message="Seleccione una opción",
                              choices=["Continuar", "Pausar"])]

            answer = inquirer.prompt(questions=question)
            if answer is not None:
                if answer['menu'] == "Continuar":
                    self.execute_all_methods()
                elif answer['menu'] == "Pausar":
                    break
                else:
                    print("No existe esta opción")

        Console().print("Simulación finalizada", style="bold green")

    def execute_all_methods(self):
        self.show_principal_info()
        self.assign_client_to_desk()
        self.reduce_time_in_desk()


    def show_principal_info(self):
        selected_company = StoreData.selected_company
        selected_office = StoreData.selected_office

        Console().print("Simulación de atención", style="bold green")
        Console().print(
            f'Empresa: {selected_company.name}', style="bold green")
        Console().print(
            f'Punto de atención: {selected_office.name}', style="bold green")

        # Show the value of clients in queue and out of queue
        Console().print(
            f'\nClientes en cola: {selected_office.get_clients_in_queue()}', style="bold yellow")
        Console().print(
            f'Clientes atendidos: {selected_office.clients_out_queue}', style="bold yellow")

        # Show how many active and inactive desks are
        Console().print(
            f'\nEscritorios activos: {selected_office.active_desks.get_size()}', style="bold yellow")
        Console().print(
            f'Escritorios inactivos: {selected_office.inactive_desks.get_size()}', style="bold yellow")

        # Show average time for attention
        Console().print(f'\nTiempo promedio de espera: 0', style="bold yellow")
        Console().print(f'Tiempo máximo de espera: 0', style="bold yellow")
        Console().print(f'Tiempo mínimo de espera: 0', style="bold yellow")

    def assign_client_to_desk(self) -> None:
        list_of_desks = StoreData.selected_office.active_desks

        node = list_of_desks.stack.head
        while node is not None:
            desk: Desk = node.data
            if desk.get_client_in_attention() is None:
                client_node = StoreData.selected_office.remove_client()
                if client_node is not None:
                    client: Client = client_node.data
                    desk.attend_client(client)
                    Console().print(
                        f'Cliente {client.name} asignado a escritorio {desk.employee}', style="bold yellow")
            node = node.next

    def reduce_time_in_desk(self) -> None:
        list_of_desks = StoreData.selected_office.active_desks

        node = list_of_desks.stack.head
        while node is not None:
            desk: Desk = node.data
            if desk.get_client_in_attention() is not None:
                self.show_desks_with_clients(desk)
                if self.next_step(desk.get_client_in_attention(), desk):
                    desk.attend_client(None)
            node = node.next

    def next_step(self, client: Client, desk: Desk) -> bool:
        list_of_transactions: SinglyLinkedList = client.transactions

        node = list_of_transactions.head
        if node is not None:
            transaction: TransactionClient = node.data
            if transaction.get_simulation_time() > 0:
                show_transaction_client(client, transaction)
                transaction.go_to_next_step_in_time()
                return
            else:
                client.get_transactions().remove_at_start()
                return self.next_step(client, desk)
        return True

    def show_desks_with_clients(self, desk: Desk):
        Console().print(f'Atendiendo: {desk.employee}\n'
                        f'Cliente: {desk.get_client_in_attention().name}\n'
                        f'Transacción: {desk.get_client_in_attention().get_first_transaction_name()}', style="bold bright_white")

        Console().print(f'Tiempo promedio de atención:{desk.average_time_attention}\n'
                        f'Tiempo máximo de atención:{desk.max_time_attention}\n'
                        f'Tiempo mínimo de atención:{desk.min_time_attention}\n', style="bold bright_white")

    def verify_data(self) -> bool:
        if StoreData.selected_company is not None and StoreData.selected_office is not None:
            if (StoreData.selected_office.active_desks.get_size() > 0 and self.verify_if_desk_is_attending()) or StoreData.selected_office.clients_in_queue > 0:
                return True
            else:
                Console().print(
                    "No hay escritorios activos o clientes en cola", style="bold red")
                return False
        else:
            Console().print("No hay empresa o punto de atención seleccionado", style="bold red")
            return False

    @staticmethod
    def verify_if_desk_is_attending() -> bool:
        list_of_active_desks = StoreData.selected_office.active_desks

        node = list_of_active_desks.stack.head
        while node is not None:
            desk: Desk = node.data
            if desk.get_client_in_attention() is not None:
                return True
            node = node.next
        return False

    def simulate_all(self):
        while self.verify_data():
            self.execute_all_methods()

        Console().print("Simulación finalizada", style="bold green")
    # Todo para simulacion
    '''
    [ x ]Verificar si hay clientes en la cola
    [ x ]Si hay clientes en la cola, atender al primero
    [ x ]Si no hay clientes en la cola, mostrar mensaje
    [ x ]Si no hay escritorios activos, mostrar mensaje y no asignar cliente
    [ x ]Si el escritorio activo, termina con su cliente, se le asigna uno nuevo
    [ x ]Cuando termine de atender al cliente, el estado es None
    '''

    # Todo para tiempos
    '''
    [ x ]Eliminar transaccion de la lista de transacciones del cliente si el tiempo es 0
    [ x ]Mostrar tiempo de atención
    [ x ]Mostrar tiempo promedio de atención
    [ x ]Mostrar tiempo máximo de atención
    [ x ]Mostrar tiempo mínimo de atención

    Cuando se ingrese un cliente 
    '''
