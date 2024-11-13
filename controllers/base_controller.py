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

    def get_date_from_user(self, view_method, message_to_display):
        while True:
            try:
                date = view_method(message_to_display)
            except ValueError:
                self.view.show_custom_error("La date n'est pas au format jj/mm/aaaa")
            else:
                break
        return date.strftime("%d/%m/%Y")