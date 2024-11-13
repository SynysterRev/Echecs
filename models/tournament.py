from datetime import datetime


class Tournament:
    def __init__(self, name, place, date, players, description, number_rounds=4):
        """Construct a new tournament

        Parameters:
            name(string): name of the tournament
            place(string): where the tournament takes place
            date(date): beginning of the tournament
            players(list): participants
            description(string): some notes for the director
            number_rounds(int): number of rounds during the tournament, 4 by default
        """
        self.name = name
        self.place = place
        self.date_start = date
        self.players = players
        self.description = description
        self.number_rounds = number_rounds
        self.current_round = 1
        self.rounds = []
        self.date_end = ""
        self.is_finished = False
        self.points = {}
        for player in self.players:
            self.points[player] = 0

    def end_tournament(self):
        now = datetime.now()
        self.date_end = now.strftime("%d/%m/%Y %H:%M:%S")
        self.is_finished = True

    def change_round(self, new_round):
        self.current_round = new_round

    def modify_description(self, new_description):
        self.description = new_description

    def add_player(self, new_player):
        self.players.append(new_player)

    def change_date_start(self, new_date):
        self.date_start = new_date

    def add_round(self, new_round):
        self.rounds.append(new_round)

    def get_score(self, player):
        return self.points[player]
