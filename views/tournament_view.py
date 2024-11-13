from views.basic_view import BasicView


class TournamentView(BasicView):
    def __init__(self):
        super().__init__()
        self.name = "Nouveau tournoi"
        self.accessible_menus = ()


    def show_menu(self):
        super().show_menu()