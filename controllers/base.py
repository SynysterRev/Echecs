# from models.tournament import Tournament
# from models.round import Round
# from models.player import Player
# from models.match import Match
# from models.match import MatchResult
# import random
# from typing import List



class Controller:
    """Main controller"""

    def __init__(self, view, active_controller, controllers):
        self.view = view
        self.active_controller = active_controller
        self.controllers = controllers

    def run(self):
        self.active_controller.run()
