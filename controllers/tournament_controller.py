import sys

from pynput import keyboard
import re

from controllers.base_controller import BaseController
from custom_exception import EmptyStringException, IDException
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from helpers.serializer import Serializer
from models.player import Player
from models.tournament import Tournament


class TournamentController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.accessible_menus = (Helper.get_new_tournament_menu(),
                                 # Helper.get_modify_tournament_menu(),
                                 Helper.get_main_menu())
        self.tournaments_list = []
        self.players_list = []
        self.wanted_players = []
        self.render_new_player = False
        self.current_menu = 0
        self.searched_player = None

    def run(self):
        self.tournaments_list = Deserializer.deserialize_tournament()
        self.players_list = Deserializer.deserialize_players()
        self.view.tournaments = self.tournaments_list
        self.max_selection = len(self.accessible_menus)
        self.view.accessible_menus = self.accessible_menus
        self.current_menu = 0
        while True:
            self.view.clear_view()
            self.view.render(self.current_selection)
            with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
                listener.join()

            if self.accessible_menus[self.current_selection] == Helper.get_main_menu():
                return Helper.get_main_menu()

            self.create_tournament()


    def handle_information_tournament_input(self):
        self.view.clear_view()
        self.view.render_new_tournament()

    def create_tournament(self):
        index_field = 0
        self.view.clear_view()
        self.view.render_new_tournament()
        method_per_index = {0: (self.is_input_not_empty, EmptyStringException),
                            1: (self.is_input_not_empty, EmptyStringException),
                            2: (self.validate_date, ValueError),
                            3: (self.is_input_not_empty, EmptyStringException),
                            4: (self.is_input_int, ValueError)}
        new_tournament_informations = []
        while True:
            default_input_value = "4" if index_field == 4 else ""
            while True:
                try:
                    final_input = self.get_user_input(self.handle_information_tournament_input,
                                              method_per_index[index_field][0], default_input_value)
                except method_per_index[index_field][1] as exception:
                    default_input_value = self.view.current_input
                    self.view.clear_view()
                    self.view.render_new_tournament(exception)
                else:
                    break
            self.view.current_input = ""
            new_tournament_informations.append(final_input)
            index_field += 1
            if index_field == len(method_per_index):
                break
            self.view.change_information_input_index(index_field)
            self.view.validate_information(final_input, index_field - 1)
            self.handle_information_tournament_input()
        self.ask_for_players()
        #ask for players
        new_tournament = Tournament(new_tournament_informations[0],
                                    new_tournament_informations[1],
                                    new_tournament_informations[2],
                                    self.wanted_players,
                                    new_tournament_informations[3],
                                    new_tournament_informations[4])
        Serializer.serialize_tournament(new_tournament)
        self.tournaments_list.append(new_tournament)
        self.view.clear_tournament_informations()
        index_field = 0
        default_input_value = ""
        new_tournament_informations = []
        self.current_selection = 0
        self.current_menu = 0

    def ask_for_players(self):
        self.view.accessible_menus = [Helper.get_import_players_menu(), Helper.get_select_players_menu(),
                                      Helper.get_add_player(), Helper.get_validate()]
        self.current_menu = 1
        self.render_new_player = True
        players_imported = False
        self.current_selection = 0
        self.view.players_list = self.wanted_players
        self.max_selection = len(self.view.accessible_menus)
        while True:
            self.view.clear_view()
            # display array with all selected players
            self.view.render_players_to_add(self.current_selection)
            with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
                listener.join()
            if self.current_selection == 0:
                if not players_imported:
                    self.wanted_players += self.players_list
                    players_imported = True
            elif self.current_selection == 1:
                self.wanted_players.append(self.selection_players())
                self.current_menu = 1
                self.view.accessible_menus = [Helper.get_import_players_menu(), Helper.get_select_players_menu(),
                                              Helper.get_add_player(), Helper.get_validate()]
                self.max_selection = len(self.view.accessible_menus)
            elif self.current_selection == 2:
                self.wanted_players.append(self.add_new_player())
            elif self.current_selection ==3:
                break
        self.accessible_menus = (Helper.get_new_tournament_menu(),
                                 # Helper.get_modify_tournament_menu(),
                                 Helper.get_main_menu())
        self.max_selection = len(self.accessible_menus)
        self.view.accessible_menus = self.accessible_menus

    def selection_players(self):
        self.view.clear_view()
        self.view.render_selection_player()
        default_input_value = self.view.current_input
        player_id = ""
        while True:
            try:
                player_id = self.get_user_input(self.handle_player_selection_input,
                                          self.does_player_id_exist, default_input_value)
            except IDException as exception:
                default_input_value = self.view.current_input
                self.view.clear_view()
                self.view.render_selection_player(exception)
            else:
                break
        self.searched_player = next(player for player in self.players_list if player.player_id == player_id)
        searched_player_name = f"{self.searched_player.first_name} {self.searched_player.name}"
        self.current_selection = 0
        self.current_menu = 2
        self.max_selection = 2
        self.view.accessible_menus = [Helper.get_validate(), Helper.get_back()]
        self.view.clear_view()
        self.view.render_validate_player(searched_player_name, self.current_selection)
        with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
            listener.join()
        if self.current_selection == 0:
            self.view.current_input = ""
            return self.searched_player
        else:
            return self.selection_players()


    def add_new_player(self):
        index_field = 0
        self.view.index_field = 0
        self.view.clear_view()
        self.view.render_new_player()
        method_per_index = {0: (self.is_player_id_valid, IDException),
                            1: (self.is_input_not_empty, EmptyStringException),
                            2: (self.is_input_not_empty, EmptyStringException),
                            3: (self.validate_date, ValueError)}
        new_player_informations = []
        while True:
            last_input = ""
            while True:
                try:
                    final_input = self.get_user_input(self.handle_information_player_input,
                                                      method_per_index[index_field][0], last_input)
                except method_per_index[index_field][1] as exception:
                    last_input = self.view.current_input
                    self.view.clear_view()
                    self.view.render_new_player(exception)
                else:
                    break
            self.view.current_input = ""
            new_player_informations.append(final_input)
            index_field += 1
            if index_field == 4:
                break
            self.view.change_information_player_input_index(index_field)
            self.view.validate_player_information(final_input, index_field - 1)
            self.handle_information_player_input()
        new_player = Player(new_player_informations[0],
                            new_player_informations[1],
                            new_player_informations[2],
                            new_player_informations[3])
        index_field = 0
        new_player_informations = []
        self.view.clear_player_informations()
        return new_player

    def handle_information_player_input(self):
        self.view.clear_view()
        self.view.render_new_player()

    def handle_player_selection_input(self):
        self.view.clear_view()
        self.view.render_selection_player()

    def is_player_id_valid(self, new_player_id):
        if not re.match(r"^[A-Z]{2}[1-9]{5}$", new_player_id):
            raise IDException("L'identifiant doit comporter 2 lettres suivies de 5 chiffres (AB12345)")
        if any(new_player_id == player.player_id for player in self.players_list):
            raise IDException("Cet identifiant existe déjà dans la base de données")
        return True

    def does_player_id_exist(self, player_id):
        if not re.match(r"^[A-Z]{2}[0-9]{5}$", player_id):
            raise IDException("L'identifiant doit comporter 2 lettres suivies de 5 chiffres (AB12345)")
        if not any(player_id == player.player_id for player in self.players_list):
            raise IDException("Cet identifiant n'existe pas dans la base de données")
        if any(player_id == player.player_id for player in self.wanted_players):
            raise IDException("Ce joueur est déjà inscrit à ce tournoi")
        return True

    def render_view(self):
        self.view.clear_view()
        if self.current_menu == 0:
            self.view.render(self.current_selection)
        elif self.current_menu == 1:
            self.view.render_players_to_add(self.current_selection)
        elif self.current_menu == 2:
            searched_player_name = f"{self.searched_player.first_name} {self.searched_player.name}"
            self.view.render_validate_player(searched_player_name, self.current_selection)

    # continue it if enough time
    def modify_tournament(self):
        tournaments = Deserializer.deserialize_tournament()
        self.view.display_all_tournaments(tournaments)
        choice = self.view.ask_tournament_to_modify(len(tournaments))
        # players = tournament.players
        # players_encounters = {}
        # if self.current_tournament.current_round == 1:
        #     for player in players:
        #         players_encounters[player] = []
        #     random.shuffle(players)
        #     matches = []
        #     for i in range(0, len(self.current_tournament.players), 2):
        #         match = Match(players[i], players[i + 1])
        #         players_encounters[players[i]].append(players[i + 1])
        #         players_encounters[players[i + 1]].append(players[i])
        #         matches.append(match)
        #
        #     current_round = Round("Round 1", matches)
        #     self.current_tournament.add_round(current_round)
        # matches[0].set_winner(MatchResult.PLAYER_ONE)
        # matches[0].update_player_one_score(1)
        # matches[1].set_winner(MatchResult.PLAYER_TWO)
        # matches[1].update_player_one_score(1)
