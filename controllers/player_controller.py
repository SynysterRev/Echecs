from deserializer import Deserializer
from helper import Helper
from models.player import Player
from serializer import Serializer
from views.base import OutOfRangeValueException
from views.player_view import PlayerView


class PlayerController:
    def __init__(self):
        self.view = PlayerView()


    def run(self):
        players_list = Deserializer.deserialize_players()
        self.view.players_list = players_list
        while True:
            try:
                choice = self.view.show_menu()
            except ValueError as ve:
                self.view.show_type_int_error()
            except OutOfRangeValueException as exception:
                self.view.show_custom_error(exception)
            else:
                if choice == 0:
                    name = self.view.ask_player_name()
                    first_name = self.view.ask_player_first_name()
                    while True:
                        try:
                            birth_date = self.view.ask_player_birth_date()
                        except ValueError:
                            self.view.show_custom_error("La date de naissance n'est pas au format jj/mm/aaaa")
                        else:
                            break
                    string_date = birth_date.strftime("%d/%m/%Y")
                    Serializer.serialize_player(Player(name, first_name, string_date))
                    # update view
                    self.view.players_list = Deserializer.deserialize_players()
                else:
                    return Helper.get_main_menu()

    def handle_player_name(self):
        while True:
            try:
                name = self.view.ask_player_name()
            except ValueError as ve:
                self.view.show_type_int_error()
            except OutOfRangeValueException as exception:
                self.view.show_custom_error(exception)