from helpers.helper import Helper
from views.basic_view import BasicView

class MenuView(BasicView):

    def __init__(self):
        super().__init__()
        self.name = "Menu principal"
        self.accessible_menus = ()

    def show_menu(self):
        """Main menu of the application"""
        super(MenuView, self).show_menu()
        for i in range(len(self.accessible_menus)):
            # ex : "1. Créer un tournoi"
            print(f"{i + 1}. {Helper.text_menu[self.accessible_menus[i]]}")
        return self.ask_for_user_choice(len(self.accessible_menus))