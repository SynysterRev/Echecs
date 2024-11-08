from views.basic_view import BasicView
import re

from views.base import FormatIDException


class IdentificationView(BasicView):
    def __init__(self):
        super().__init__()
        self.name = "Menu identification"

    def show_menu(self):
        """First menu to get the club using the application"""
        super(IdentificationView, self).show_menu()
        club_id = str(input("Veuillez entrer l'identifiant du club : "))
        if not re.match(r"^[A-Z]{2}[1-9]{5}$", club_id):
            raise FormatIDException()
        return club_id