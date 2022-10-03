from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.classes.Company import Company
from controller.classes.Office import Office


class StoreData:

    # Store the companies and offices
    list_of_companies: SinglyLinkedList = SinglyLinkedList()

    # Store the companies and offices selected
    selected_office: None or Office = None
    selected_company: None or Company = None