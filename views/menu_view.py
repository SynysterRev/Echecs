from views.basic_view import BasicView

class MenuView(BasicView):
    """Main menu of the application"""
    def __init__(self, console):
        super().__init__(console)
        self.name = "Menu principal"