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

    def get_number_matches_not_played(self) -> int :
        return sum(not match.is_finished for match in self.matches)

    def get_matches_not_played(self):
        return [match for match in self.matches if not match.is_finished]

    @staticmethod
    def deserialize(json_text) -> "Round":
        name = json_text["name"]
        is_finished = json_text["is_finished"]
        date_begin = json_text["date_begin"]
        date_end = json_text["date_end"]
        matches = []
        for match in json_text["matches"]:
            matches.append(Match.deserialize(match))
        rnd = Round(name, matches)
        rnd.is_finished = is_finished
        rnd.date_begin = date_begin
        rnd.date_end = date_end
        return rnd

    def serialize(self):
        matches_list = []
        for match in self.matches:
            matches_list.append(match.serialize())
        return {"name": self.name, "matches": matches_list, "is_finished": self.is_finished, "date_begin": self.date_begin, "date_end": self.date_end}