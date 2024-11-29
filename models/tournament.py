from datetime import datetime

from models.player import Player


class Tournament:
    def __init__(self, name, place, date_start, players, description, number_rounds=4):
        """Construct a new tournament

        Parameters:
            name(string): name of the tournament
            place(string): where the tournament takes place
            date_start(date): beginning of the tournament
            players(list): participants
            description(string): some notes for the director
            number_rounds(int): number of rounds during the tournament, 4 by default
        """
        self.name = name
        self.place = place
        self.date_start = date_start
        self.players = players
        self.description = description
        self.number_rounds = number_rounds
        self.current_round_index = 1
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
        self.current_round_index = new_round

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

    def increase_score(self, player, points):
        self.points[player] += points

    def are_all_rounds_over(self) -> bool:
        return self.current_round_index > self.number_rounds

    def serialize(self):
        players_list = []
        for player in self.players:
            serialized_player = player.serialize()
            serialized_player["points"] = self.get_score(player)
            players_list.append(serialized_player)
        rounds_list = []
        for round in self.rounds:
            rounds_list.append(round.serialize())
        return {"name": self.name, "place": self.place, "date_start": self.date_start, "date_end":
            self.date_end, "players": players_list, "description": self.description,
                "number_rounds": self.number_rounds, "current_round_index": self.current_round_index,
                "rounds": rounds_list, "is_finished": self.is_finished}

    @staticmethod
    def deserialize(data) -> "Tournament":
        name = data["name"]
        place = data["place"]
        date_start = data["date_start"]
        date_end = data["date_end"]
        players = []
        points = {}
        for registered_player in data["players"]:
            player = Player(registered_player["player_id"], registered_player["name"],
                            registered_player["first_name"], registered_player["birth_date"])
            points[player] = registered_player["points"]
            players.append(player)
        description = data["description"]
        number_rounds = data["number_rounds"]
        current_round_index = data["current_round_index"]
        rounds = data["rounds"]
        is_finished = data["is_finished"]

        tournament = Tournament(name, place, date_start, players, description, number_rounds)
        tournament.players = players
        tournament.current_round_index = current_round_index
        tournament.rounds = rounds
        tournament.is_finished = is_finished
        tournament.points = points
        tournament.date_end = date_end
        return tournament
