class Match:
    def __init__(self, player_one, player_two):
        """Construct a tuple with two lists

        Parameters:
            player_one(list): a list containing the first Player and his score
            player_two(list): a list containing the second Player and his score
        """
        self.players_score = ([player_one], [player_two])