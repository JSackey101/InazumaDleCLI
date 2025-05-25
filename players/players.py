""" """

class Player:
    """ A class to represent a Player. """
    
    def __init__(self, nickname: str, name: str, element: str,
                 gender: str, position: list[str], school_year: str) -> None:
        self.nickname = nickname.lower()
        self.name = name.lower()
        self.element = element.lower()
        self.gender = gender.lower()
        self.position = [pos.upper() for pos in position]
        self.school_year = school_year.upper()
    
    def __str__(self) -> str:
        """ Human-Readable String Representation """
        return f"{self.nickname.title()} ({self.name.title()})"
    
    def __eq__(self, other: "Player") -> bool:
        """ Checks for equality between 2 Player objects. """
        return all(self.compare_players(other))

    def compare_players(self, other_player: "Player") -> list[bool]:
        """ Returns a list containing True/False representing the comparison
            of 2 Player Objects"""
        return [self.nickname == other_player.nickname,
                self.name == other_player.name,
                self.element == other_player.element,
                self.gender == other_player.gender,
                self.position == other_player.position,
                self.school_year == other_player.school_year]
