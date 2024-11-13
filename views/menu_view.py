from views.basic_view import BasicView

class MenuView(BasicView):

    def __init__(self):
        super().__init__()
        self.name = "Menu principal"

    def show_menu(self):
        """Main menu of the application"""
        return super().show_menu()