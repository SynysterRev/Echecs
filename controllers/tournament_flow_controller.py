import copy
import random

from controllers.base_controller import BaseController
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from helpers.serializer import Serializer
from models.match import Match, MatchResult
from models.round import Round


class TournamentFlowController(BaseController):

    def __init__(self, view):
        super().__init__(view)
        self.players_encounters = {}
        self.players = []
        self.tournaments = []
        self.current_tournament = None
        self.accessible_menus = (Helper.get_main_menu(),
                                 Helper.get_start_tournament_menu(),
                                 Helper.get_start_round_menu(),
                                 Helper.get_start_match_menu(),
                                 Helper.get_match_result_menu())
        self.current_round = None
        self.matches = None
        self.current_menu = 1
        self.current_match = None

    def check_previous_matches(self, current_player, all_matches, players_left):
        """check if we can pair current player with a player already paired
        check by reversed to keep score between players close"""

        for match in reversed(all_matches):
            player_one = match.get_player_one()
            player_two = match.get_player_two()
            if (len(self.players_encounters) == 0 or
                    current_player.player_id in self.players_encounters):
                if player_two.player_id not in self.players_encounters[current_player.player_id]:
                    all_matches.remove(match)
                    new_match = Match([player_two, 0], [current_player, 0])
                    all_matches.append(new_match)
                    players_left.append(player_one)
                    return new_match
                if player_one.player_id not in self.players_encounters[current_player.player_id]:
                    all_matches.remove(match)
                    new_match = Match([player_one, 0], [current_player, 0])
                    all_matches.append(new_match)
                    players_left.append(player_two)
                    return new_match
        return None

    def create_matches(self):
        players_points = self.current_tournament.players_points
        players_list = sorted(players_points, key=players_points.get, reverse=True)
        players_left = copy.deepcopy(players_list)
        new_matches = []
        while len(players_left) > 0:
            current_player = players_left[0]
            players_left.remove(current_player)
            new_match = None
            for player in players_left:
                if (len(self.players_encounters) == 0 or
                        player not in self.players_encounters[current_player]):
                    player_one = self.current_tournament.get_player_by_id(current_player)
                    player_two = self.current_tournament.get_player_by_id(player)
                    new_match = Match([player_one, players_points[current_player]],
                                      [player_two, players_points[player]])
                    new_matches.append(new_match)
                    players_left.remove(player)
                    break
            # no pairing found between players left
            if new_match is None:
                new_match = self.check_previous_matches(current_player, new_matches, players_left)
                # all pairing are already done, start over
                if new_match is None:
                    self.players_encounters.clear()
                    new_matches.clear()
                    players_left = copy.deepcopy(players_list)
        return new_matches

    def start_round(self):
        random.shuffle(self.players)
        matches = self.create_matches()
        self.matches = matches
        current_round = Round(f"Round {self.current_tournament.current_round_index + 1}", matches)
        self.current_tournament.rounds.append(current_round)
        self.current_round = current_round
        current_round.start_round()
        self.save()

    def run(self):
        self.tournaments = [tournament for tournament in Deserializer.deserialize_tournament() if
                            not tournament.is_finished]
        self.view.tournaments = self.tournaments
        available_menus = {0: None, 1: self.select_tournament, 2: self.select_round,
                           3: self.select_match, 4: self.select_match_result,
                           5: self.tournament_over}
        while True:
            self.current_selection = 0
            self.view.clear_view()
            function = available_menus[self.current_menu]
            if self.current_menu == 0:
                return Helper.get_main_menu()
            function()

    def save(self):
        if self.current_tournament is not None:
            Serializer.serialize_tournament(self.current_tournament)

    def get_encounters_for_players(self):
        self.players = self.current_tournament.players
        for player in self.players:
            self.players_encounters[player.player_id] = []
        for round in self.current_tournament.rounds:
            for match in round.matches:
                player_one = match.get_player_one()
                player_two = match.get_player_two()
                self.players_encounters[player_one.player_id].append(player_two.player_id)
                self.players_encounters[player_two.player_id].append(player_one.player_id)

    def select_tournament(self):
        self.max_selection = len(self.tournaments) + 1
        self.view.render_tournament_selection(self.current_selection)
        while self.current_tournament is None:
            self.handle_input()
            if self.current_selection != self.max_selection - 1:
                # get selected tournament and current round and go to the next menu
                if len(self.tournaments[self.current_selection].players) % 2 == 0:
                    self.current_tournament = self.tournaments[self.current_selection]
                    self.get_encounters_for_players()
                    self.view.current_tournament = self.current_tournament
                    self.view.current_round_index = self.current_tournament.current_round_index
                    self.current_menu = 2
                else:
                    self.view.clear_view()
                    self.view.render_tournament_selection(self.current_selection,
                                                          "Le nombre de joueurs n'est pas pair")
            else:
                self.current_menu = 0
                return

    def select_round(self):
        # current round and back menu
        self.max_selection = 2
        current_round_index = self.current_tournament.current_round_index
        round_started = False
        current_number_round = len(self.current_tournament.rounds)
        if current_round_index == current_number_round - 1:
            self.current_round = self.current_tournament.rounds[current_round_index]
            round_started = self.current_round.is_started()
        self.view.current_round_index = current_round_index
        self.view.render_start_round(self.current_selection)
        self.handle_input()
        if self.current_selection == 1:
            self.current_menu = 1
            self.current_tournament = None
        else:
            if not round_started:
                self.start_round()
            self.current_menu = 3
        self.save()

    def select_match(self):
        number_match_to_do = self.current_round.get_number_matches_not_played()
        self.max_selection = (number_match_to_do if number_match_to_do > 0 else 1) + 1
        self.view.matches = self.current_round.matches
        self.view.matches_not_played = self.current_round.get_matches_not_played()
        if self.are_all_matches_played():
            self.view.render_all_matches_played(self.current_selection)
        else:
            self.view.render_select_match(self.current_selection)
        self.handle_input()
        if self.current_selection == self.max_selection - 1:
            self.current_menu = 2
        else:
            if self.are_all_matches_played():
                self.prepare_next_round()
            else:
                self.current_menu = 4
                self.current_match = self.current_round.get_matches_not_played()[self.current_selection]

    def are_all_matches_played(self) -> bool:
        for match in self.current_round.matches:
            if not match.is_finished:
                return False
        return True

    def select_match_result(self):
        # player1/player2/draw/back
        self.max_selection = 4
        self.view.current_match = self.current_match
        self.view.render_match_result(self.current_selection)
        self.handle_input()

        match self.current_selection:
            case 0:
                self.current_match.set_winner(MatchResult.PLAYER_ONE)
                pass
            case 1:
                self.current_match.set_winner(MatchResult.PLAYER_TWO)
                pass
            case 2:
                self.current_match.set_winner(MatchResult.DRAW)
                pass
        score_p1 = self.current_match.get_player_one_and_score()
        score_p2 = self.current_match.get_player_two_and_score()
        self.current_tournament.change_score(score_p1[0], score_p1[1])
        self.current_tournament.change_score(score_p2[0], score_p2[1])
        self.current_menu = 3
        self.save()

    def prepare_next_round(self):
        self.current_round.end_round()
        self.current_tournament.current_round_index += 1
        if self.current_tournament.are_all_rounds_over():
            self.current_menu = 5
        else:
            self.current_menu = 2

    def tournament_over(self):
        # Ok
        self.max_selection = 1
        tournament_points = dict(sorted(self.current_tournament.players_points.items(),
                                        key=lambda item: item[1], reverse=True))
        self.view.tournament_finals_scores = tournament_points
        self.view.render_end_tournament(self.current_selection)
        self.handle_input()
        self.current_tournament.end_tournament()
        self.save()
        self.current_menu = 0

    def render_view(self):
        self.view.clear_view()
        if self.current_menu == 1:
            self.view.render_tournament_selection(self.current_selection)
        elif self.current_menu == 2:
            self.view.render_start_round(self.current_selection)
        elif self.current_menu == 3:
            if self.are_all_matches_played():
                self.view.render_all_matches_played(self.current_selection)
            else:
                self.view.render_select_match(self.current_selection)
        elif self.current_menu == 4:
            self.view.render_match_result(self.current_selection)
        elif self.current_menu == 5:
            self.view.render_end_tournament(self.current_selection)
