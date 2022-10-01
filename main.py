import inquirer

from controller.base.Stack import Stack
from controller.base.SinglyLinkedList import SinglyLinkedList
from model.simulation.InitConfig import InitConfig
from model.simulation.SystemConfig import SystemConfig


class Main:
    system_config: SystemConfig = SystemConfig()
    init_config: InitConfig = InitConfig()

    def __init__(self) -> None:
        self.run()

    def run(self) -> None:
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
                self._company_menu()
            elif answer['menu'] == "2. Seleccionar empresa y punto de atención":
                pass
            elif answer['menu'] == "3. Manejo de puntos de atención":
                self._point_menu()
            elif answer['menu'] == "4. Salir":
                print("¡Adiós!")
            else:
                print("No existe esta opción")

    # Menu 1
    def _company_menu(self) -> None:
        questions = [
            inquirer.List('menu',
                          message="Seleccione una opción",
                          choices=["1. Limpiar sistema",
                                   "2. Cargar archivo de configuración",
                                   "3. Crear empresa",
                                   "4. Cargar archivo de configuración inicial",
                                   "5. Regresar"])]
        answer = inquirer.prompt(questions=questions)
        if answer is not None:
            if answer['menu'] == "1. Limpiar sistema":
                self._clear_system()
            elif answer['menu'] == "2. Cargar archivo de configuración":
                self._system_config()
            elif answer['menu'] == "3. Crear empresa":
                self._create_company_menu()
            elif answer['menu'] == "4. Cargar archivo de configuración inicial":
                pass
            elif answer['menu'] == "5. Regresar":
                self.run()

    # Option 1 for menu 1
    def _clear_system(self) -> None:
        print(f'\n{self.system_config.clear_system()}')

    # Option 2 for menu 1
    def _system_config(self) -> None:
        path_file = self._get_file()
        if path_file:
            self.system_config.system_config(path_file)
        else:
            print("No existe el fichero")

    # Option 3 for menu 1
    # Submenu 1.3
    def _create_company_menu(self) -> None:
        q = [
            inquirer.Text('id_company',
                          message="Ingrese el id de la empresa"),
            inquirer.Text('name',
                          message="Ingrese el nombre de la empresa"),
            inquirer.Text('acronym',
                          message="Ingrese la abreviatura de la empresa")]
        answers = inquirer.prompt(questions=q)

        print(answers)

        # while True:
        #     id_company: str = ""
        #     name: str = ""
        #     acronym: str = ""

        #     while id_company == "":
        #         id_company: str = input("Ingrese el id de la empresa: ")
        #     while name == "":
        #         name: str = input("Ingrese el nombre de la empresa: ")
        #     while acronym == "":
        #         acronym: str = input("Ingrese el acrónimo de la empresa: ")

        #     print("\n1. Nuevo punto de venta")
        #     print("2. Nueva transacción")
        #     option = input("Seleccione una opción: ")

        #     offices: SinglyLinkedList = SinglyLinkedList()
        #     transactions: SinglyLinkedList = SinglyLinkedList()

        #     if option == "1":
        #         new_office_list: SinglyLinkedList = self._create_office()
        #         if new_office_list is not None:
        #             offices = new_office_list
        #         else:
        #             print("No se pudo crear el punto de venta")
        #     elif option == "2":
        #         new_transaction_list: SinglyLinkedList = self._create_transaction()
        #         if new_transaction_list is not None:
        #             transactions = new_transaction_list
        #         else:
        #             print("No se pudo crear la transacción")
        #     else:
        #         print("No existe esta opción")

        #     if offices.get_size() == 0:
        #         print("No se puede crear la empresa sin puntos de venta")
        #     elif transactions == 0:
        #         print("No se puede crear la empresa sin transacciones")
        #     else:
        #         resp: str = self.system_config.create_company(
        #             id_company, name, acronym, offices, transactions)
        #         print(f'\n{resp}')

        #         print("\n ¿Desea agregar otra empresa?")
        #         print("1. Si")
        #         print("2. No")
        #         option = input("Seleccione una opción: ")
        #         if option == "1":
        #             continue
        #         elif option == "2":
        #             break
        #         else:
        #             print("No existe esta opción")

    # Option 1.3.1 for menu 1.1

    def _create_office(self) -> SinglyLinkedList:
        while True:
            new_offices_list: SinglyLinkedList = SinglyLinkedList()

            id_office: str = ""
            name: str = ""
            address: str = ""

            while id_office == "":
                id_office: str = input("Ingrese el id del punto de atención ")
            while name == "":
                name: str = input("Ingrese el nombre del punto de atención: ")
            while address == "":
                address: str = input(
                    "Ingrese la dirección del punto de atención: ")

            desks: Stack = self._create_desks()
            if desks is not None:
                new_office = self.system_config.create_office(
                    id_office, name, address, desks)
                new_offices_list.insert_at_end(new_office)

            else:
                print("No se pudo crear el punto de venta")

            print("\n ¿Desea agregar otro punto de atención?")
            print("1. Si")
            print("2. No")
            option = input("Seleccione una opción: ")
            if option == "1":
                continue
            elif option == "2":
                return new_offices_list

    # Option 1.3.1.1 for menu 1.1
    def _create_desks(self) -> Stack:
        while True:
            desks_list: Stack = Stack()
            id_desk: str = input("Ingrese el id del puesto del escritorio: ")
            correlative: str = input(
                "Ingrese el correlativo del escritorio: ")
            employee: str = input("Ingrese el nombre del empleado: ")
            res = self.system_config.create_desk(
                id_desk, correlative, employee)
            desks_list.push(res)
            print(f'\n{res}')

            print("\n ¿Desea agregar otro escritorio?")
            print("1. Si")
            print("2. No")
            option = input("Seleccione una opción: ")
            if option == "1":
                continue
            elif option == "2":
                return desks_list

    # Option 3.2 for menu 1.1
    def _create_transaction(self) -> SinglyLinkedList:
        while True:
            new_transaction_list: SinglyLinkedList = SinglyLinkedList()
            id_transaction: str = input("Ingrese el id de la transacción: ")
            name: str = input("Ingrese el nombre de la transacción: ")
            duration: str = input("Ingrese la duración de la transacción: ")
            new_transaction = self.system_config.create_transaction(
                id_transaction, name, duration)
            if new_transaction is not None:
                new_transaction_list.insert_at_end(new_transaction)
                print(f'\n{new_transaction}')
            else:
                print("No se pudo crear la transacción")

            print("\n ¿Desea agregar otra transacción?")
            print("1. Si")
            print("2. No")
            option = input("Seleccione una opción: ")
            if option == "1":
                continue
            elif option == "2":
                return new_transaction_list

    # Option 4 for menu 1
    def _system_init(self) -> None:
        path_file = self._get_file()
        if path_file:
            self.system_config.system_init(path_file)
        else:
            print("No existe el fichero")

    # Menu 2
    def _select_company_menu(self) -> None:
        while True:
            print("\n1. Mostrar empresas")
            print("2. Seleccionar empresa")
            print("3. Volver")
            option = input("Seleccione una opción: ")
            if "1" == option:
                self.system_config.show_companies()
            elif "2" == option:
                self._select_company()
            elif "3" == option:
                break
            else:
                print("No existe esta opción")

    def _select_company(self) -> None:
        id_company = input("Ingrese el id de la empresa: ")
        res = self.system_config.show_company_by_id(id_company)
        if res == "":
            self._select_office_menu(id_company)
        else:
            print(f'\n{res}')

    def _select_office_menu(self, id_company: str) -> None:
        while True:
            print("\n1. Mostrar puntos de venta")
            print("2. Seleccionar punto de venta")
            print("3. Volver")
            option = input("Seleccione una opción: ")
            if "1" == option:
                self.system_config.show_offices(id_company)
            elif "2" == option:
                self._select_office(id_company)
            elif "3" == option:
                break
            else:
                print("No existe esta opción")

    # Menu 3
    def _point_menu(self) -> None:
        pass

    # Menu 4
    @staticmethod
    def _exit():
        print("¡Adiós!")
        exit()

    # Auxiliar methods

    @staticmethod
    def _get_file() -> str:
        path_file = input("Introduzca la ruta del fichero: ")
        return path_file


if __name__ == "__main__":
    Main()
