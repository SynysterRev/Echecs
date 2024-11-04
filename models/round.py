from match import Match
from datetime import datetime

class Round:
    def __init__(self, name, matches):
        """Construct a round

        Parameters:
            name(string): name of the round (ex : Round 1)
            matches(list): a list containing all the matches for this round
        """
        self.name = name
        self.matches = matches
        self.is_over = False
        self.date_begin = ""
        self.date_end = ""

    def start_match(self):
        now = datetime.now()
        self.date_begin = now.strftime("%d/%m/%Y %H:%M:%S")

    def end_match(self):
        self.is_over = True
        now = datetime.now()
        self.date_end = now.strftime("%d/%m/%Y %H:%M:%S")