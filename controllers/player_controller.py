import re

from pynput import keyboard

from controllers.base_controller import BaseController
from custom_exception import EmptyStringException, IDException
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from helpers.serializer import Serializer
from models.player import Player


class PlayerController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.accessible_menus = (Helper.get_add_player(),
                                 Helper.get_main_menu())
        self.players_list = []

    def run(self):
        self.players_list = Deserializer.deserialize_players()
        self.view.players_list = self.players_list
        self.view.accessible_menus = self.accessible_menus
        self.max_selection = len(self.accessible_menus)
        while True:
            self.view.clear_view()
            self.view.render(self.current_selection)
            with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
                listener.join()

            if self.accessible_menus[self.current_selection] == Helper.get_main_menu():
                return Helper.get_main_menu()

            index_field = 0
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
                self.view.change_information_input_index(index_field)
                self.view.validate_information(final_input, index_field - 1)
                self.handle_information_player_input()
            new_player = Player(new_player_informations[0],
                                new_player_informations[1],
                                new_player_informations[2],
                                new_player_informations[3])
            Serializer.serialize_player(new_player)
            self.players_list.append(new_player)
            index_field = 0
            new_player_informations = []
            self.view.clear_player_informations()

    def handle_information_player_input(self):
        self.view.clear_view()
        self.view.render_new_player()

    def is_player_id_valid(self, new_player_id):
        if not re.match(r"^[A-Z]{2}[1-9]{5}$", new_player_id):
            raise IDException("L'identifiant doit comporter 2 lettres suivies de 5 chiffres (AB12345)")
        if any(new_player_id == player.player_id for player in self.players_list):
            raise IDException("Cet identifiant existe déjà dans la base de données")
        return True
