""" """

class Player:
    """ A class to represent a Player. """
    
    def __init__(self, nickname: str, name: str, element: str,
                 gender: str, position: list[str], school_year: str) -> None:
        self.nickname = nickname
        self.name = name
        self.element = element
        self.gender = gender
        self.position = position
        self.school_year = school_year