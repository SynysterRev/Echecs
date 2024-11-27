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
            self.winner = self.players_score[0][0]
            self.players_score = ([self.winner, 1], [self.players_score[1][0], 0])
        elif result == MatchResult.PLAYER_TWO:
            self.winner = self.players_score[1][0]
            self.players_score = ([self.players_score[0][0], 0], [self.winner, 1])
        else:
            self.winner = "Match nul"
            self.players_score = ([self.players_score[0][0], 0.5], [self.players_score[1][0], 0.5])
        self.is_finished = True

    def __str__(self):
        return f"{self.players_score[0][0]} contre {self.players_score[1][0]}"

    def serialize(self):
        return {"players_score": [(self.players_score[0][0].player_id, self.players_score[0][1]),
                                  (self.players_score[1][0].player_id, self.players_score[1][1])],
                "is_finished": self.is_finished}
