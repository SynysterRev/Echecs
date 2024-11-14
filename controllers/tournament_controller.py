import random

from controllers.base_controller import BaseController
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from helpers.serializer import Serializer
from models.match import Match
from models.round import Round
from models.tournament import Tournament


class TournamentController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.players_encounters = {}
        self.current_tournament = None
        self.accessible_menus = (Helper.get_new_tournament_menu(),
                                 Helper.get_modify_tournament_menu(),
                                 Helper.get_launch_tournament_menu(),
                                 Helper.get_main_menu())

    def get_all_tournaments(self):
        pass

    def get_tournament(self, tournament_name):
        pass

    def start_tournament(self, tournament: Tournament):
        self.current_tournament = tournament
        players = tournament.players
        players_encounters = {}
        if self.current_tournament.current_round == 1:
            for player in players:
                players_encounters[player] = []
            random.shuffle(players)
            matches = []
            for i in range(0, len(self.current_tournament.players), 2):
                match = Match(players[i], players[i + 1])
                players_encounters[players[i]].append(players[i + 1])
                players_encounters[players[i + 1]].append(players[i])
                matches.append(match)

            current_round = Round("Round 1", matches)
            self.current_tournament.add_round(current_round)
            # matches[0].set_winner(MatchResult.PLAYER_ONE)
            # matches[0].update_player_one_score(1)
            # matches[1].set_winner(MatchResult.PLAYER_TWO)
            # matches[1].update_player_one_score(1)

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

    def start_round(self, tournament: Tournament):
        current_round = tournament.rounds[tournament.current_round]
        current_round.start_round()
        round_matches = current_round.matches

    def get_matches_current_round(self):
        print("")

    def run(self):
        self.view.accessible_menus = self.accessible_menus
        choice = self.get_user_choice()
        if self.accessible_menus[choice] == Helper.get_main_menu():
            return self.accessible_menus[choice]
        if self.accessible_menus[choice] == Helper.get_new_tournament_menu():
            self.create_tournament()



    def create_tournament(self):
        pass
        tournament_name = self.get_string_from_user("Nom : ")
        tournament_place = self.get_string_from_user("Lieu : ")
        tournament_date = self.get_date_from_user(self.view.ask_for_date,
                                                  "Date de début (ex : 01/01/1900) : ")
        tournament_rounds = 4
        while True:
            try:
                tournament_rounds = self.view.ask_tournament_number_rounds()
            except ValueError:
                self.view.show_type_int_error()
            else:
                break
        tournament_description = self.view.ask_tournament_description()
        players = Deserializer.deserialize_players()
        # for player in players:
        #     self.players_encounters[player] = []

        new_tournament = Tournament(tournament_name, tournament_place, tournament_date, players,
                                    tournament_description, tournament_rounds)
        Serializer.serialize_tournament(new_tournament)
