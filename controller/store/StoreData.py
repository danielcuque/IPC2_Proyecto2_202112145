from controller.base.NodeForSinglyList import NodeForSinglyList
from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.classes.Company import Company
from controller.classes.Office import Office


class StoreData:

    # Store the companies and offices
    list_of_companies: SinglyLinkedList = SinglyLinkedList()

    # Store the companies and offices selected
    selected_office: None or Office = None
    selected_company: None or Company = None

    @staticmethod
    # Methods to saerch information about companies and offices
    def search_company_by_name(name: str) -> Company:
        node: NodeForSinglyList = StoreData.list_of_companies.head
        while node is not None:
            company: Company = node.data
            if company.name == name:
                return company
            node = node.next
        return None

    def search_company_by_id(id_company: str) -> Company:
        node: NodeForSinglyList = StoreData.list_of_companies.head
        while node is not None:
            company: Company = node.data
            if company.id_company == id_company:
                return company
            node = node.next
        return None
