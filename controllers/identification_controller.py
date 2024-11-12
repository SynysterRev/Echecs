from helper import Helper
from views.base import FormatIDException
from views.identification_view import IdentificationView

class IdentificationController:
    def __init__(self):
        self.view = IdentificationView()

    def run(self):
        while True:
            try:
                club_id = self.view.show_menu()
            except ValueError:
                self.view.show_type_int_error()
            except FormatIDException as id_exception:
                self.view.show_custom_error(id_exception)
            else:
                Helper.club_id = club_id
                return "main_menu"