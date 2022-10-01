import inquirer

from controller.base.Stack import Stack
from controller.base.SinglyLinkedList import SinglyLinkedList

from view.Menu1 import Menu1
from view.Menu2 import Menu2
from view.Menu3 import Menu3


class Main:
    def __init__(self) -> None:
        self.run()

    def run(self) -> None:
        menu1 = Menu1()
        menu2 = Menu2()
        menu3 = Menu3()

        while True:
            questions = [
                inquirer.List('menu',
                            message="Seleccione una opción",
                            choices=["1. Configuración del sistema",
                                    "2. Seleccionar empresa y punto de atención",
                                    "3. Manejo de puntos de atención",
                                    "4. Salir"])]
            answer = inquirer.prompt(questions=questions)
            if answer is not None:
                if answer['menu'] == "1. Configuración del sistema":
                    menu1.company_menu()
                elif answer['menu'] == "2. Seleccionar empresa y punto de atención":
                    pass
                elif answer['menu'] == "3. Manejo de puntos de atención":
                    self._point_menu()
                elif answer['menu'] == "4. Salir":
                    self._exit()
                else:
                    print("No existe esta opción")


    # Option 3 for menu 1
    # Submenu 1.3
    # def _create_company_menu(self) -> None:
    #     q = [
    #         inquirer.Text('id_company',
    #                       message="Ingrese el id de la empresa",
    #                       validate=lambda _, x: len(x) > 0 and x.isalnum()),
    #         inquirer.Text('name',
    #                       message="Ingrese el nombre de la empresa",
    #                       validate=lambda _, x: len(x) > 0 and x.isalnum()),
    #         inquirer.Text('acronym',
    #                       message="Ingrese la abreviatura de la empresa",
    #                       validate=lambda _, x: len(x) > 0 and x.isalnum())]
    #     answers = inquirer.prompt(questions=q)
    #     if answers is not None:
    #         id_company: str = answers['id_company']
    #         name: str = answers['name']
    #         acronym: str = answers['acronym']
    #         offices: SinglyLinkedList = self._create_office()
    #         transactions: SinglyLinkedList = self._create_transaction()
    #         if offices is not None and transactions is not None:
    #             r = self.system_config.create_company(
    #                 id_company, name, acronym, offices, transactions)
    #             print(r)
    #         else:
    #             print("No se pudo crear la empresa")

    # # Option 1.3.1 for menu 1.1
    # def _create_office(self) -> SinglyLinkedList:
    #     offices: SinglyLinkedList = SinglyLinkedList()
    #     while True:
    #         q = [
    #             inquirer.Text('id_office',
    #                           message="Ingrese el id del punto de atención",
    #                           validate=lambda _, x: len(x) > 0 and x.isalnum()),
    #             inquirer.Text('name',
    #                           message="Ingrese el nombre del punto de atención",
    #                           validate=lambda _, x: len(x) > 0 and x.isalnum()),
    #             inquirer.Text('address',
    #                           message="Ingrese la dirección del puesto de atención",
    #                           validate=lambda _, x: len(x) > 0 and x.isalnum())]
    #         answers = inquirer.prompt(questions=q)
    #         if answers is not None:
    #             id_office: str = answers['id_office']
    #             name: str = answers['name']
    #             address: str = answers['address']
    #             desks: Stack = self._create_desks()
    #             offices.insert_at_end(self.system_config.create_office(
    #                 id_office, name, address, desks))

    #         q = [
    #             inquirer.Confirm('continue',
    #                              message="¿Desea agregar otro punto de atención?",
    #                              default=False)]
    #         answer = inquirer.prompt(questions=q)
    #         if answer is not None:
    #             if not answer['continue']:
    #                 break
    #     return offices

    # # Option 1.3.1.1 for menu 1.1

    # def _create_desks(self) -> Stack:

    #     desks: Stack = Stack()
    #     while True:
    #         q = [
    #             inquirer.Text('id_desk',
    #                           message="Ingrese el id del puesto",
    #                           validate=lambda _, x: len(x) > 0 and x.isalnum()),
    #             inquirer.Text('name',
    #                           message="Ingrese el nombre del puesto",
    #                           validate=lambda _, x: len(x) > 0 and x.isalnum())]
    #         answers = inquirer.prompt(questions=q)
    #         if answers is not None:
    #             id_desk: str = answers['id_desk']
    #             name: str = answers['name']
    #             desks.push(self.system_config.create_desk(id_desk, name))

    #         q = [
    #             inquirer.Confirm('continue',
    #                              message="¿Desea agregar otro puesto?",
    #                              default=False)]
    #         answer = inquirer.prompt(questions=q)
    #         if answer is not None:
    #             if not answer['continue']:
    #                 break
    #     return desks

    # # Option 3.2 for menu 1.1
    # def _create_transaction(self) -> SinglyLinkedList:
    #     while True:
    #         new_transaction_list: SinglyLinkedList = SinglyLinkedList()
    #         id_transaction: str = input("Ingrese el id de la transacción: ")
    #         name: str = input("Ingrese el nombre de la transacción: ")
    #         duration: str = input("Ingrese la duración de la transacción: ")
    #         new_transaction = self.system_config.create_transaction(
    #             id_transaction, name, duration)
    #         if new_transaction is not None:
    #             new_transaction_list.insert_at_end(new_transaction)
    #             print(f'\n{new_transaction}')
    #         else:
    #             print("No se pudo crear la transacción")

    #         print("\n ¿Desea agregar otra transacción?")
    #         print("1. Si")
    #         print("2. No")
    #         option = input("Seleccione una opción: ")
    #         if option == "1":
    #             continue
    #         elif option == "2":
    #             return new_transaction_list

    # # Option 4 for menu 1
    # def _system_init(self) -> None:
    #     path_file = self._get_file()
    #     if path_file:
    #         self.system_config.system_init(path_file)
    #     else:
    #         print("No existe el fichero")

    # # Menu 2
    # def _select_company_menu(self) -> None:
    #     while True:
    #         print("\n1. Mostrar empresas")
    #         print("2. Seleccionar empresa")
    #         print("3. Volver")
    #         option = input("Seleccione una opción: ")
    #         if "1" == option:
    #             self.system_config.show_companies()
    #         elif "2" == option:
    #             self._select_company()
    #         elif "3" == option:
    #             break
    #         else:
    #             print("No existe esta opción")

    # def _select_company(self) -> None:
    #     id_company = input("Ingrese el id de la empresa: ")
    #     res = self.system_config.show_company_by_id(id_company)
    #     if res == "":
    #         self._select_office_menu(id_company)
    #     else:
    #         print(f'\n{res}')

    # def _select_office_menu(self, id_company: str) -> None:
    #     while True:
    #         print("\n1. Mostrar puntos de venta")
    #         print("2. Seleccionar punto de venta")
    #         print("3. Volver")
    #         option = input("Seleccione una opción: ")
    #         if "1" == option:
    #             self.system_config.show_offices(id_company)
    #         elif "2" == option:
    #             self._select_office(id_company)
    #         elif "3" == option:
    #             break
    #         else:
    #             print("No existe esta opción")

    # Menu 3
    def _point_menu(self) -> None:
        pass

    # Menu 4
    @staticmethod
    def _exit():
        print("¡Adiós!")
        exit()


if __name__ == "__main__":
    Main()
