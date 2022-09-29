from controller.base.SinglyLinkedList import SinglyLinkedList
from model.simulation.InitConfig import InitConfig
from model.simulation.SystemConfig import SystemConfig


class Main:

    system_config: SystemConfig = SystemConfig()
    init_config: InitConfig = InitConfig()

    def __init__(self) -> None:
        self.run()

    def run(self) -> None:
        while True:
            choice = self._initial_menu()
            if choice == "1":
                self._company_menu()
            elif choice == "2":
                self._select_company()
            elif choice == "3":
                self._point_menu()
            elif choice == "4":
                self._exit()
            else:
                print("No existe esta opción")

    # Main menu
    @staticmethod
    def _initial_menu() -> str:
        print("\n1. Configuración de empresas")
        print("2. Seleccionar empresa y punto de atención")
        print("3. Manejo de puntos de atención")
        print("4. Salir")
        return input("Seleccione una opción: ")

    # Menu 1

    def _company_menu(self) -> None:
        while True:
            print("\n1. Limpiar sistema")
            print("2. Cargar archivo de configuración")
            print("3. Crear nueva empresa")
            print("4. Cargar archivo de configuración inicial")
            print("5. Volver")
            option = input("Seleccione una opción: ")

            if option == "1":
                self._clear_system()
            elif option == "2":
                self._system_config()
            elif option == "3":
                self._create_company_menu()
            elif option == "4":
                self._system_init()
            elif option == "5":
                break
            else:
                print("No existe esta opción")

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
        id_company: str = ""
        name: str = ""
        acronym: str = ""

        while True:
            while id_company == "":
                id_company: str = input("Ingrese el id de la empresa: ")
            while name == "":
                name: str = input("Ingrese el nombre de la empresa: ")
            while acronym == "":
                acronym: str = input("Ingrese el acrónimo de la empresa: ")

            offices: SinglyLinkedList
            transactions: SinglyLinkedList

            print("\n1. Nuevo punto de venta")
            print("2. Nueva transacción")
            print("3. Volver")
            option = input("Seleccione una opción: ")
            if option == "1":
                res = self._create_office()
                if res is not None:
                    offices = res
                else:
                    print("No se pudo crear el punto de venta")
            elif option == "2":
                res = self._create_transaction()
                if res is not None:
                    transactions = res
                else:
                    print("No se pudo crear la transacción")
            elif option == "3":
                break
            else:
                print("No existe esta opción")

        res = self.system_config.create_company(
            id_company, name, acronym, offices, transactions)
        print(f'\n{res}')

        # res = self.system_config.create_company(
        #     id_company, name, acronym, offices, transactions)
        # print(f'\n{res}')

    # Option 1.3.1 for menu 1.1
    def _create_office(self) -> SinglyLinkedList:
        offices_list: SinglyLinkedList = SinglyLinkedList()
        while True:
            while id_office == "":
                id_office: str = input("Ingrese el id del punto de venta: ")
            while name == "":
                name: str = input("Ingrese el nombre del punto de venta: ")
            while address == "":
                address: str = input(
                    "Ingrese la dirección del punto de venta: ")

            desks: SinglyLinkedList = self._create_desks()
            if desks is not None:
                res = self.system_config.create_office(
                    id_office, name, address, desks)
                offices_list.insert_at_end(res)
                print(f'\n{res}')
            else:
                print("No se pudo crear el punto de venta")

            print("\n ¿Desea agregar otro punto de venta?")
            print("1. Si")
            print("2. No")
            option = input("Seleccione una opción: ")
            if option == "1":
                continue
            elif option == "2":
                return offices_list

    # Option 1.3.1.1 for menu 1.1
    def _create_desks(self) -> SinglyLinkedList:
        desks_list: SinglyLinkedList = SinglyLinkedList()
        while True:
            id_desk: str = input("Ingrese el id del puesto de atención: ")
            correlative: str = input(
                "Ingrese el correlativo del puesto de atención: ")
            employee: str = input("Ingrese el nombre del empleado: ")
            res = self.system_config.create_desk(
                id_desk, correlative, employee)
            desks_list.insert_at_end(res)
            print(f'\n{res}')

            print("\n ¿Desea agregar otro puesto de atención?")
            print("1. Si")
            print("2. No")
            option = input("Seleccione una opción: ")
            if option == "1":
                continue
            elif option == "2":
                return desks_list

    # Option 3.2 for menu 1.1
    def _create_transaction(self) -> None:
        transaction_list: SinglyLinkedList = SinglyLinkedList()
        while True:
            id_transaction: str = input("Ingrese el id de la transacción: ")
            name: str = input("Ingrese el nombre de la transacción: ")
            res = self.system_config.create_transaction(
                id_transaction, name)
            transaction_list.insert_at_end(res)
            print(f'\n{res}')

            print("\n ¿Desea agregar otra transacción?")
            print("1. Si")
            print("2. No")
            option = input("Seleccione una opción: ")
            if option == "1":
                continue
            elif option == "2":
                return transaction_list

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
