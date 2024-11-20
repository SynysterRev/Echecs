from controllers.base_controller import BaseController
from custom_exception import FormatIDException
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from models.player import Player
from helpers.serializer import Serializer


class PlayerController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.accessible_menus = (Helper.get_add_player(),
                                 Helper.get_main_menu())

    def run(self):
        players_list = Deserializer.deserialize_players()
        self.view.players_list = players_list
        self.view.accessible_menus = self.accessible_menus
        self.view.subscribe(self.on_click)
        self.view.run()

        self.click_event.wait()

        if self.menu_selected == Helper.get_main_menu():
            return Helper.get_main_menu()

        # while True:
        #     choice = self.get_user_choice(self.view.show_main_menu)
        #     if choice == 0:
        #         while True:
        #             try:
        #                 player_id = self.view.ask_player_id()
        #             except FormatIDException as id_exception:
        #                 self.view.show_custom_error(id_exception)
        #             else:
        #                 break
        #
        #         name = self.view.ask_player_name()
        #         first_name = self.view.ask_player_first_name()
        #         birth_date = self.get_date_from_user(self.view.ask_for_date,
        #                                              "Date de naissance (ex : 01/01/1900) : ")
        #         Serializer.serialize_player(Player(player_id, name, first_name, birth_date))
        #         # update view
        #         self.view.players_list = Deserializer.deserialize_players()
        #     else:
        #         return Helper.get_main_menu()
