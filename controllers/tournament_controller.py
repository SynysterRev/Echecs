from pynput import keyboard

from controllers.base_controller import BaseController
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from helpers.serializer import Serializer
from models.tournament import Tournament


class TournamentController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.accessible_menus = (Helper.get_new_tournament_menu(),
                                 # Helper.get_modify_tournament_menu(),
                                 Helper.get_main_menu())
        self.tournaments_list = []
        self.players_list = []

    def run(self):
        self.tournaments_list = Deserializer.deserialize_tournament()
        self.players_list = Deserializer.deserialize_players()
        self.view.tournaments = self.tournaments_list
        self.view.accessible_menus = self.accessible_menus
        while True:
            self.view.clear_view()
            self.view.render(self.current_selection)
            with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
                listener.join()

            if self.accessible_menus[self.current_selection] == Helper.get_main_menu():
                return Helper.get_main_menu()

            self.create_tournament()


    def handle_information_tournament_input(self, user_input):
        self.view.clear_view()
        self.view.render_new_tournament(user_input)

    def create_tournament(self):
        index_field = 0
        self.view.clear_view()
        self.view.render_new_tournament("")
        method_per_index = {0: self.is_input_not_empty,
                            1: self.is_input_not_empty,
                            2: self.validate_date,
                            3: self.is_input_not_empty,
                            4: self.is_input_int}
        new_tournament_informations = []
        while True:
            final_input = self.get_user_input(self.handle_information_tournament_input,
                                              method_per_index[index_field])
            new_tournament_informations.append(final_input)
            index_field += 1
            if index_field == len(method_per_index):
                break
            self.view.change_information_input_index(index_field)
            self.view.validate_information(final_input, index_field - 1)
            self.handle_information_tournament_input("")
        new_tournament = Tournament(new_tournament_informations[0],
                                    new_tournament_informations[1],
                                    new_tournament_informations[2],
                                    self.players_list,
                                    new_tournament_informations[3],
                                    new_tournament_informations[4])
        Serializer.serialize_tournament(new_tournament)
        self.tournaments_list.append(new_tournament)

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
