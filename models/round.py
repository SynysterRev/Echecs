from models.match import Match
from datetime import datetime
from typing import List

class Round:
    def __init__(self, name, matches: List[Match]):
        """Construct a round

        Parameters:
            name(string): name of the round (ex : Round 1)
            matches(list): a list containing all the matches for this round
        """
        self.name = name
        self.matches = matches
        self.is_finished = False
        self.date_begin = ""
        self.date_end = ""

    def start_round(self):
        now = datetime.now()
        self.date_begin = now.strftime("%d/%m/%Y %H:%M:%S")

    def end_round(self):
        self.is_finished = True
        now = datetime.now()
        self.date_end = now.strftime("%d/%m/%Y %H:%M:%S")

    def is_started(self):
        return False if not self.date_begin else True

    def get_number_matches(self) -> int :
        return len(self.matches)

    def serialize(self):
        matches_list = []
        for match in self.matches:
            matches_list.append(match.serialize())
        return {"name": self.name, "matches": matches_list, "is_finished": self.is_finished, "date_begin": self.date_begin, "date_end": self.date_end}