from enum import Enum


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
        self.winner = None
        self.is_finished = False

    def set_winner(self, result: MatchResult):
        if result == MatchResult.PLAYER_ONE:
            self.winner = self.players_score[0]
        elif result == MatchResult.PLAYER_TWO:
            self.winner = self.players_score[1]
        else:
            self.winner = None
        self.is_finished = True

    def update_player_one_score(self, value_to_add):
        self.players_score[0][1] += value_to_add

    def update_player_two_score(self, value_to_add):
        self.players_score[1][1] += value_to_add

    def __str__(self):
        return f"{self.players_score[0][0]} contre {self.players_score[1][0]}"

