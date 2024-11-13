from controllers.base_controller import BaseController
from helpers.helper import Helper
from views.identification_view import FormatIDException


class IdentificationController(BaseController):
    def __init__(self, view):
        super().__init__(view)

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
                return Helper.get_main_menu()
