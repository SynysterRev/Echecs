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
        self.winner = ""
        self.is_finished = False

    def set_winner(self, result: MatchResult):
        if result == MatchResult.PLAYER_ONE:
            self.winner = f"{self.players_score[0][0].first_name} {self.players_score[0][0].name}"
            self.players_score = ([self.players_score[0][0], 1], [self.players_score[1][0], 0])
        elif result == MatchResult.PLAYER_TWO:
            self.winner = f"{self.players_score[1][0].first_name} {self.players_score[1][0].name}"
            self.players_score = ([self.players_score[0][0], 0], [self.players_score[1][0], 1])
        else:
            self.winner = "Match nul"
            self.players_score = ([self.players_score[0][0], 0.5], [self.players_score[1][0], 0.5])
        self.is_finished = True

    def get_player_one(self):
        return self.players_score[0][0]

    def get_player_two(self):
        return self.players_score[1][0]

    def get_player_one_and_score(self):
        return self.players_score[0]

    def get_player_two_and_score(self):
        return self.players_score[1]

    def __str__(self):
        return f"{self.players_score[0][0]} contre {self.players_score[1][0]}"

    def serialize(self):
        print(self.players_score[0][0].player_id)
        return {"players_score": [(self.players_score[0][0].player_id, self.players_score[0][1]),
                                  (self.players_score[1][0].player_id, self.players_score[1][1])],
                "is_finished": self.is_finished}
