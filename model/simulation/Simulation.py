import inquirer
from rich.console import Console

# Classes
from controller.classes.Client import Client
from controller.classes.Desk import Desk


from controller.store.StoreData import StoreData


class Simulation:

    def execute_simulation(self):
        while self.simulate_attention():
            self.show_principal_info()
            question = [
                inquirer.List('menu',
                              message="Seleccione una opción",
                              choices=["Continuar", "Pausar"])]

            answer = inquirer.prompt(questions=question)
            if answer is not None:
                if answer['menu'] == "Continuar":
                    pass
                elif answer['menu'] == "Pausar":
                    break
                else:
                    print("No existe esta opción")

        Console().print("Simulación finalizada", style="bold green")

    def simulate_attention(self) -> bool:
        if StoreData.selected_office is not None and StoreData.selected_company is not None:
            if StoreData.selected_office.active_desks.get_size() > 0 and StoreData.selected_office.clients_in_queue > 0:
                self.assign_client_to_desk()
                return True
            else:
                Console().print("No hay escritorios activos", style="bold red")
                return False

    def show_principal_info(self):

        selected_company = StoreData.selected_company
        selected_office = StoreData.selected_office

        Console().print("Simulación de atención", style="bold green")
        Console().print(f'Empresa: {selected_company.name}', style="bold green")
        Console().print(f'Punto de atención: {selected_office.name}', style="bold green")


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
                    Console().print(f'Cliente {client.name} asignado a escritorio {desk.employee}', style="bold yellow")
                    return
                else:
                    Console().print("No hay clientes en cola", style="bold red")
                    return
            node = node.next
        
        Console().print("No hay escritorios disponibles", style="bold red")

        
    # Todo
    '''
    [ x ]Verificar si hay clientes en la cola
    [ x ]Si hay clientes en la cola, atender al primero
    [ x ]Si no hay clientes en la cola, mostrar mensaje
    [ x ]Si no hay escritorios activos, mostrar mensaje y no asignar cliente
    [  ]Si el escritorio activo, termina con su cliente, se le asigna uno nuevo
    [  ]Cuando termine de atender al cliente, el estado es None
    '''
