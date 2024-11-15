from controllers.base_controller import BaseController
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from models.match import Match


class TournamentFlowController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.players_encounters = {}
        self.current_tournament = None
        self.accessible_menus = (Helper.get_start_round_menu(),
                                 Helper.get_main_menu())

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
        return player_two in players_encounters[player_one]

    def get_best_match(self, players_encounters, current_player, all_players):
        for player in all_players[1:]:
            if not self.is_match_already_done(players_encounters, current_player[0], player[0]):
                players_encounters[current_player[0]].append(player[0])
                players_encounters[player[0]].append(current_player[0])
                return Match(current_player, player)

    def create_matches(self, players_points, players_encounters, tournament):
        players_points.sort(key=self.sort_player_by_points, reverse=True)
        all_matches = []
        for round in tournament.rounds:
            for match in round.matches:
                all_matches.append(match)

        players_to_place = players_points
        current_player = players_to_place[0]
        new_matches = []
        while len(players_to_place) > 0:
            new_match = self.get_best_match(players_encounters, current_player, players_to_place)
            players_to_place.remove(new_match.players_score[0])
            players_to_place.remove(new_match.players_score[1])
            new_matches.append(new_match)
            if len(players_to_place) > 0:
                current_player = players_to_place[0]
        return new_matches

    def start_round(self):
        current_round = self.current_tournament.rounds[self.current_tournament.current_round]
        current_round.start_round()
        round_matches = current_round.matches

    def get_matches_current_round(self):
        print("")


    def run(self):
        self.view.accessible_menus = self.accessible_menus
        while True:
            choice = self.get_user_choice(self.view.show_main_menu)
            if self.accessible_menus[choice] == Helper.get_main_menu():
                return self.accessible_menus[choice]

    def start_tournament(self):
        tournaments = Deserializer.deserialize_tournament()
        self.view.tournaments = tournaments
        choice = self.get_user_choice(self.view.tournament_selection)
        if choice == len(tournaments) + 1:
            return