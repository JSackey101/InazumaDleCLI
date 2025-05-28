""" """

import os
import csv
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
        
class PlayerDatabase:
    """ A class to represent a Database of Players. """
    
    # Currently figuring out logic - do I want the database to be able to fill itself - so user doesn't NEED to input Players or not
    
    def __init__(self, players: list["Player"] | None = None,
                 player_file: str | None = None) -> None:
        self.players = []
        if players:
            self.players += players
        if player_file:
            self.players += self.read_player_data(player_file)
        
    @staticmethod
    def read_player_data(file_name: str) -> list[Player]:
        """ Reads the player data from the CSV file and 
            creates and returns a list of Player objects. """
        abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(abs_path, file_name), "r",
                  newline="", encoding="utf-8") as players:
            players_csv = csv.reader(players)
            players_data = list(row for row in players_csv)[1:]
            list_of_players = []
            for row in players_data:
                player = Player(row[0],
                                row[1],
                                row[2],
                                row[3],
                                row[4].split(','),
                                row[5])
                if not any(player == added_player for added_player in list_of_players):
                    list_of_players.append(player)
            return list_of_players
        

test = PlayerDatabase(player_file='players.csv')
print(test.players[0]==test.players[1])