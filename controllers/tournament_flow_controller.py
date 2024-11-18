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
        self.current_menu = "tournament_selection"
        self.accessible_menus = (Helper.get_main_menu(),
                                 "tournament_selection",
                                 "round_start",
                                 "matches_result")
        self.current_round = None
        self.matches = None

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
        if self.current_tournament.current_round == 1:
            for player in self.players:
                self.players_encounters[player] = []
                print(player)
        random.shuffle(self.players)
        matches = self.create_matches()
        self.matches = matches
        self.view.matches = matches
        current_round = Round(f"Round {self.current_tournament.current_round}", matches)
        self.current_tournament.rounds.append(current_round)
        self.current_round = current_round
        current_round.start_round()
        self.save()


    def get_matches_current_round(self):
        print("")

    def run(self):
        while True:
            tournaments = Deserializer.deserialize_tournament()
            self.view.tournaments = tournaments
            match self.current_menu:
                case "main_menu":
                    return Helper.get_main_menu()

                case "tournament_selection":
                    choice = self.get_user_choice(self.view.tournament_selection)
                    if choice == len(tournaments):
                        self.current_menu = Helper.get_main_menu()
                    else:
                        # get selected tournament and current round and go to the next menu
                        self.current_tournament = tournaments[choice]
                        self.view.current_round = self.current_tournament.current_round
                        self.current_menu = "round_start"

                case "round_start":
                    current_round = self.current_tournament.current_round
                    round_started = False
                    if current_round < len(self.current_tournament.rounds):
                        self.current_round = self.current_tournament.rounds[current_round]
                        round_started = self.current_round.is_started()
                    if round_started:
                        choice = self.get_user_choice(self.view.ask_continue_round)
                    else:
                        choice = self.get_user_choice(self.view.ask_start_round)
                    # go back to tournament selection
                    if choice == 1:
                        self.current_menu = "tournament_selection"
                    else:
                        self.players = self.current_tournament.players
                        if not round_started:
                            self.start_round()
                        else:
                            self.view.matches = self.current_round.matches
                        self.current_menu = "match_selection"

                case "match_selection":
                    choice = self.get_user_choice(self.view.matches_selection)
                    if choice == len(tournaments):
                        self.current_menu = "tournament_selection"
                    else:
                        self.current_menu = "match_result"
                        self.view.current_match = self.matches[choice]

                case "match_result":
                    choice = self.get_user_choice(self.view.ask_match_result)
                    print(choice)


    def save(self):
        pass

# rich python
# simple term menu