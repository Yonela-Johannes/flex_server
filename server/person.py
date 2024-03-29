class Person:
    """
    Represents a person, holds, name, socket client and address
    """
    def __init__(self, addr, client):
        self.addr = addr
        self.client = client
        self.name = None
    """
    Sets the person's name
    "param name: str
    :return: None
    """
    def set_name(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"Person({self.addr}, {self.name})"
    
