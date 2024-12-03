from pynput import keyboard

from controllers.base_controller import BaseController
from helpers.deserializer import Deserializer
from helpers.helper import Helper


class ReportController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.players_list = []
        self.tournaments_list = []
        self.accessible_menus = ("players_report", "tournaments_report",
                                 "players_tournament_report", "tournament_flow_report",
                                 Helper.get_main_menu())
        self.view_to_display = {-1: self.view.render_menu, 0: self.view.render_all_players,
                                1: self.view.render_all_tournaments, 2: self.view.render_tournament_players,
                                3: self.view.render_tournament_info}
        self.index_menu = -1
        self.selected_tournament = None

    def run(self):
        self.players_list = Deserializer.deserialize_players()
        self.tournaments_list = Deserializer.deserialize_tournament()
        self.view.players_list = self.players_list
        self.view.tournaments = self.tournaments_list
        self.view.accessible_menus = self.accessible_menus
        self.max_selection = len(self.accessible_menus)
        while True:
            self.view.clear_view()
            self.view_to_display[self.index_menu](self.current_selection)
            with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
                listener.join()

            if self.accessible_menus[self.current_selection] == Helper.get_main_menu():
                return Helper.get_main_menu()

            if self.current_selection == 2 or self.current_selection == 3:
                self.max_selection = len(self.tournaments_list)
                self.index_menu = self.select_tournament()
            else:
                self.index_menu = self.current_selection
            self.max_selection = len(self.accessible_menus)
            self.current_selection = 0

    def render_view(self):
        self.view.clear_view()
        self.view_to_display[self.index_menu](self.current_selection)

    def select_tournament(self):
        index_menu = self.current_selection
        self.current_selection = 0
        self.view.clear_view()
        self.view.render_tournaments_names(self.current_selection)
        with keyboard.Listener(on_press=self.handle_input, suppress=True) as listener:
            listener.join()
        self.selected_tournament = self.tournaments_list[self.current_selection]
        self.view.selected_tournament = self.selected_tournament
        return index_menu
