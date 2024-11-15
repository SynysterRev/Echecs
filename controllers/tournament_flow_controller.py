import random

from controllers.base_controller import BaseController
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from models.match import Match
from models.round import Round


class TournamentFlowController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.players_encounters = {}
        self.players = []
        self.current_tournament = None

    def get_all_tournaments(self):
        pass

    def get_tournament(self, tournament_name):
        pass

    def start_new_round(self):
        if self.current_tournament is None:
            raise NoTournamentException()

        current_round = self.current_tournament.rounds[self.current_tournament.current_round]
        current_round.start_round()

    def sort_player_by_points(self, player):
        return player[1]

    def is_match_already_done(self, players_encounters, player_one, player_two):
        if player_one in players_encounters:
            return player_two in players_encounters[player_one]
        return False

    def get_best_match(self, players_encounters, current_player, all_players):
        for player in all_players[1:]:
            if not self.is_match_already_done(players_encounters, current_player[0], player[0]):
                players_encounters[current_player[0]].append(player[0])
                players_encounters[player[0]].append(current_player[0])
                return Match(current_player, player)

    def create_matches(self):
        players_points = self.current_tournament.points
        players_points = sorted(players_points.items(), key=lambda item: item[1], reverse=True)
        current_player = players_points[0]
        new_matches = []
        while len(players_points) > 0:
            new_match = self.get_best_match(self.players_encounters, current_player, players_points)
            players_points.remove(new_match.players_score[0])
            players_points.remove(new_match.players_score[1])
            new_matches.append(new_match)
            if len(players_points) > 0:
                current_player = players_points[0]
        return new_matches

    def start_round(self):
        self.players = self.current_tournament.players
        if self.current_tournament.current_round == 1:
            for player in self.players:
                self.players_encounters[player] = []
                print(player)
        random.shuffle(self.players)
        matches = self.create_matches()
        # current_round = Round()
        # self.current_tournament.rounds
        # current_round.start_round()
        print(matches)
        # round_matches = current_round.matches

    def get_matches_current_round(self):
        print("")

    def run(self):
        while True:
            tournaments = Deserializer.deserialize_tournament()
            self.view.tournaments = tournaments
            choice = self.get_user_choice(self.view.tournament_selection)
            if choice == len(tournaments):
                return Helper.get_main_menu()
            self.current_tournament = tournaments[choice]
            choice = self.view.ask_start_round(self.current_tournament.current_round)
            if choice == 1:
                continue
            self.start_round()
            self.create_matches()
