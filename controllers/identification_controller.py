from helper import Helper
from views.identification_view import IdentificationView

class IdentificationController:
    def __init__(self):
        self.view = IdentificationView()

    def run(self):
        club_id = self.view.show_menu()
        Helper.club_id = club_id
        return "main_menu"