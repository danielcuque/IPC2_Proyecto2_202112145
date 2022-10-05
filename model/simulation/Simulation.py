from ast import Store
import inquirer
from rich.console import Console


from controller.store.StoreData import StoreData
from model.utils.ShowProperties import show_client, show_company, show_office


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
            if StoreData.selected_office.active_desks.get_size() > 0:
                show_company(StoreData.selected_company)
                show_office(StoreData.selected_office)
                client = StoreData.selected_office.remove_client()
                if client is not None:
                    show_client(client.data)
                    return True
                else:
                    Console().print("No hay clientes en la cola", style="bold red")
                    return False
            else:
                Console().print("No hay escritorios activos", style="bold red")
                return False

    def calculate_average_time(self):
        pass

    def calculate_average_time_by_client(self):
        pass

    def show_principal_info(self):
        Console().print("Simulación de atención", style="bold green")
        Console().print(f'Empresa: {StoreData.selected_company.name}', style="bold green")
        Console().print(f'Punto de atención: {StoreData.selected_office.name}', style="bold green")

        
        # Show the value of clients in queue and out of queue
        Console().print(
            f'\nClientes en cola: {self.clients_in_queue}', style="bold yellow")
        Console().print(
            f'Clientes atendidos: {self.clients_out_of_queue}', style="bold yellow")

        # Show how many active and inactive desks are
        Console().print(
            f'\nEscritorios activos: {StoreData.selected_office.active_desks.get_size()}', style="bold yellow")
        Console().print(
            f'Escritorios inactivos: {StoreData.selected_office.inactive_desks.get_size()}', style="bold yellow")


        # Show average time for attention
        Console().print(f'\nTiempo promedio de espera: 0', style="bold yellow")
        Console().print(f'Tiempo máximo de espera: 0', style="bold yellow")
        Console().print(f'Tiempo mínimo de espera: 0', style="bold yellow")

        
    # Todo
    '''
    [  ]Verificar si hay clientes en la cola
    [  ]Si hay clientes en la cola, atender al primero
    [  ]Si no hay clientes en la cola, mostrar mensaje
    [  ]Si no hay escritorios activos, mostrar mensaje y no asignar cliente
    [  ]Si el escritorio activo, termina con su cliente, se le asigna uno nuevo
    [  ]Cuando termine de atender al cliente, el estado es None
    '''
