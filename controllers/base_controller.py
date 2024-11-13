from custom_exception import OutOfRangeValueException

class BaseController:
    def __init__(self, view):
        self.view = view
        self.accessible_menus = ()

    def run(self):
        pass

    def get_user_choice(self) -> int:
        while True:
            try:
                choice = self.view.show_menu()
            except ValueError:
                self.view.show_type_int_error()
            except OutOfRangeValueException as exception:
                self.view.show_custom_error(exception)
            else:
                return choice