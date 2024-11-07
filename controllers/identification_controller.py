from views.identification_view import IdentificationView

class IdentificationController:
    def __init__(self):
        self.view = IdentificationView()

    def run(self):
        id = self.view.show_menu()
        # load correct json
        # go to main menu
        return