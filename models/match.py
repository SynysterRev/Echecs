from enum import Enum

from models.player import Player


class MatchResult(Enum):
    PLAYER_ONE = 1
    PLAYER_TWO = 2
    DRAW = 3


class Match:
    def __init__(self, player_one, player_two):
        """Construct a tuple with two lists

        Parameters:
            player_one(list): a list containing the first Player and his score
            player_two(list): a list containing the second Player and his score
        """
        self.players_score = (player_one, player_two)
        self.winner = ""
        self.is_finished = False

    def set_winner(self, result: MatchResult):
        if result == MatchResult.PLAYER_ONE:
            self.winner = f"{self.players_score[0][0].first_name} {self.players_score[0][0].name}"
            new_points_one = self.players_score[0][1] + 1
            self.players_score = ([self.players_score[0][0], new_points_one],
                                  [self.players_score[1][0], self.players_score[1][1]])
        elif result == MatchResult.PLAYER_TWO:
            self.winner = f"{self.players_score[1][0].first_name} {self.players_score[1][0].name}"
            new_points_two = self.players_score[1][1] + 1
            self.players_score = ([self.players_score[0][0], self.players_score[0][1]],
                                  [self.players_score[1][0], new_points_two])
        else:
            self.winner = "Match nul"
            new_points_one = self.players_score[0][1] + 0.5
            new_points_two = self.players_score[1][1] + 0.5
            self.players_score = ([self.players_score[0][0], new_points_one],
                                  [self.players_score[1][0], new_points_two])
        self.is_finished = True

    def get_player_one(self):
        return self.players_score[0][0]

    def get_player_two(self):
        return self.players_score[1][0]

    def get_player_one_score(self):
        return self.players_score[0][1]

    def get_player_two_score(self):
        return self.players_score[1][1]

    def get_player_one_and_score(self):
        return self.players_score[0]

    def get_player_two_and_score(self):
        return self.players_score[1]

    def __str__(self):
        return f"{self.players_score[0][0]} contre {self.players_score[1][0]}"

    @staticmethod
    def deserialize(json_text) -> "Match":
        """Deserialize a match from a json"""
        player_one = Player.deserialize(json_text["player_one"][0])
        player_one_point = json_text["player_one"][1]
        player_two = Player.deserialize(json_text["player_two"][0])
        player_two_point = json_text["player_two"][1]
        winner = json_text["winner"]
        is_finished = json_text["is_finished"]
        match = Match([player_one, player_one_point], [player_two, player_two_point])
        match.winner = winner
        match.is_finished = is_finished
        return match

    def serialize(self):
        """Serialize a match to a json"""
        return {"player_one": (self.players_score[0][0].serialize(), self.players_score[0][1]),
                "player_two": (self.players_score[1][0].serialize(), self.players_score[1][1]),
                "winner": self.winner,
                "is_finished": self.is_finished}
