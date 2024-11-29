import random

from pynput import keyboard

from controllers.base_controller import BaseController
from helpers.deserializer import Deserializer
from helpers.helper import Helper
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

    def start_new_round(self):
        if self.current_tournament is None:
            raise NoTournamentException()

        current_round = self.current_tournament.rounds[self.current_tournament.current_round_index]
        current_round.start_round()

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
        if self.current_tournament.current_round_index == 1:
            for player in self.players:
                self.players_encounters[player] = []
        random.shuffle(self.players)
        matches = self.create_matches()
        self.matches = matches
        current_round = Round(f"Round {self.current_tournament.current_round_index}", matches)
        self.current_tournament.rounds.append(current_round)
        self.current_round = current_round
        current_round.start_round()
        self.save()

    def run(self):
        self.tournaments = Deserializer.deserialize_tournament()
        self.view.tournaments = self.tournaments
        test = {0: None, 1: self.select_tournament, 2: self.select_round,
                3: self.select_match, 4: self.select_match_result,
                5: self.tournament_over}
        while True:
            func = test[self.current_menu]
            if self.current_menu == 0:
                return Helper.get_main_menu()
            func()

    def save(self):
        pass
        # Serializer.serialize_tournament(self.current_tournament)

    def select_tournament(self):
        self.view.clear_view()
        self.max_selection = len(self.tournaments) + 1
        self.view.render_tournament_selection(self.current_selection)
        with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
            listener.join()
        if self.current_selection != self.max_selection - 1:
            # get selected tournament and current round and go to the next menu
            self.current_tournament = self.tournaments[self.current_selection]
            self.view.current_round_index = self.current_tournament.current_round_index
            self.current_menu = 2
        else:
            self.current_menu = 0

    def select_round(self):
        self.view.clear_view()
        self.current_selection = 0
        # current round and back menu
        self.max_selection = 2
        current_round_index = self.current_tournament.current_round_index
        round_started = False
        if current_round_index < len(self.current_tournament.rounds):
            self.current_round = self.current_tournament.rounds[current_round_index]
            round_started = self.current_round.is_started()
        self.view.current_round_index = current_round_index
        self.view.render_start_round(self.current_selection)
        with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
            listener.join()
        if self.current_selection == 1:
            self.current_menu = 1
        else:
            self.players = self.current_tournament.players
            if not round_started:
                self.start_round()
            self.current_menu = 3
        self.save()

    def select_match(self):
        self.view.clear_view()
        self.current_selection = 0
        number_match_to_do = self.current_round.get_number_matches_not_played()
        self.max_selection = (number_match_to_do if number_match_to_do > 0 else 1) + 1
        self.view.matches = self.current_round.matches
        self.view.matches_not_played = self.current_round.get_matches_not_played()
        if self.are_all_matches_played():
            self.view.render_all_matches_played(self.current_selection)
        else:
            self.view.render_select_match(self.current_selection)
        with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
            listener.join()
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
        self.view.clear_view()
        self.current_selection = 0
        # player1/player2/draw/back
        self.max_selection = 4
        self.view.current_match = self.current_match
        self.view.render_match_result(self.current_selection)
        with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
            listener.join()

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
        self.current_tournament.increase_score(score_p1[0], score_p1[1])
        self.current_tournament.increase_score(score_p2[0], score_p2[1])
        self.current_menu = 3
        self.save()

    def prepare_next_round(self):
        self.current_tournament.current_round_index += 1
        if self.current_tournament.are_all_rounds_over():
            self.current_menu = 5
        else:
            self.current_menu = 2

    def tournament_over(self):
        self.view.clear_view()
        self.current_selection = 0
        # Ok
        self.max_selection = 1
        self.current_tournament.points = dict(sorted(self.current_tournament.points.items(), key=lambda item: item[1],
                                                 reverse=True))
        self.view.tournament_finals_scores = self.current_tournament.points
        self.view.render_end_tournament(self.current_selection)
        with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
            listener.join()

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
