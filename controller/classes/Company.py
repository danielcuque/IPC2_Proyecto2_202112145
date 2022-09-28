from controller.base.SimplyList import SimplyList

class Company:
    def __init__(self, id_company, name, acronym):
        self.id_company: int = id_company
        self.name: str = name
        self.acronym: str = acronym
        self.offices: SimplyList = SimplyList()
        