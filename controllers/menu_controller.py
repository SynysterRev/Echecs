from controllers.base_controller import BaseController
from helpers.helper import Helper


class MenuController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.accessible_menus = (Helper.get_start_tournament_menu(),
                                 Helper.get_tournament_menu(),
                                 Helper.get_players_menu(),
                                 Helper.get_generate_reports_menu(),
                                 Helper.get_quit())

    # def run(self):
    #     self.view.accessible_menus = self.accessible_menus
    #     self.view.subscribe(self.on_click)
    #     self.view.run()
    #
    #     self.click_event.wait()
    #
    #     return self.menu_selected
    #
    # def on_click(self, value):
    #     self.menu_selected = value
    #     self.view.unsubscribe(self.on_click)
    #     self.view.exit()
    #     self.click_event.set()