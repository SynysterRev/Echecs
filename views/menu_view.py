from views.basic_view import BasicView

class MenuView(BasicView):
    """Main menu of the application"""
    def __init__(self):
        super().__init__()
        self.name = "Menu principal"