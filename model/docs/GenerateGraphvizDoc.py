import graphviz as gv
from rich.console import Console

from controller.base.NodeForSinglyList import NodeForSinglyList
from controller.classes.Client import Client
from controller.classes.Desk import Desk
from controller.store.StoreData import StoreData


class GenerateGraphvizDoc:

    def generate_doc(self):
        graph = gv.Digraph(
            f'Oficina {StoreData.selected_office.name}',
            filename=f'Oficina {StoreData.selected_office.name}',
            directory='docs',
        )

        self.subgraph_for_stats(graph)
        self.subgraph_for_desks(graph)
        self.subgraph_for_clients(graph)
        graph.view()

    def subgraph_for_clients(self, g: gv.Digraph):
        node: NodeForSinglyList = StoreData.selected_office.clients_attended.items.head

        if node is not None:
            g.attr('node', shape='box', style='filled', color='#FFEDBB')

            with g.subgraph(name='cluster_clients') as c:
                c.attr(style='filled', color='lightgrey',
                       label=f'Fila de espera', fontsize='14')
                for i in range(StoreData.selected_office.clients_attended.items.get_size()):
                    client: Client = node.data
                    c.node(f'C_{i}', f'{client.dpi} - {client.name}')
                    if node.next is not None:
                        c.edge(f'C_{i+1}', f'C_{i}', constraint='false')
                    node = node.next
        else:
            Console().print('No hay clientes atendidos', style='bold red')

    def subgraph_for_desks(self, g: gv.Digraph):
        node: NodeForSinglyList = StoreData.selected_office.get_head_active_desks()

        if node is not None:
            g.attr('node', shape='box', style='filled', color='#FFEDBB')

            with g.subgraph(name='cluster_desks') as c:
                c.attr(style='filled', color='lightgrey',
                       label=f'Escritorios activos', fontsize='14')
                c.attr(rankdir='LR')
                for i in range(StoreData.selected_office.active_desks.get_size()):
                    desk: Desk = node.data
                    c.node(f'D_{i}', f'{desk.employee} - Escritorio {i+1}')
                    if node.next is not None:
                        c.edge(f'D_{i+1}', f'D_{i}')
                    node = node.next
        else:
            Console().print('No hay escritorios activos', style='bold red')

    def subgraph_for_stats(self, g: gv.Digraph):
        with g.subgraph(name='cluster_stats') as c:
            c.attr(style='filled', color='lightgrey',
                   label=f'Estadísticas', fontsize='14')
            c.attr('node', shape='box', style='filled', color='#FFEDBB')
            c.attr(rankdir='LR')
            c.node(
                'stats', f'Clientes atendidos: {StoreData.selected_office.clients_attended.items.get_size()}\n Compañia: {StoreData.selected_company.name}\n Punto de atención: {StoreData.selected_office.name}\n Escritorios activos: {StoreData.selected_office.active_desks.get_size()}\n Escritorios inactivos: {StoreData.selected_office.inactive_desks.get_size()}')
