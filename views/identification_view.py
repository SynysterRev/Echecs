from views.abstract_view import AbstractView
import re

from views.base import IncorrectValueException


class IdentificationView(AbstractView):
    def __init__(self):
        super().__init__()
        self.name = "Menu identification"

    def show_menu(self):
        """First menu to get the club using the application"""
        super(IdentificationView, self).show_menu()
        while True:
            try:
                id = str(input("Veuillez entrer l'identifiant du club : "))
                if not re.match(r"^[A-Z]{2}[1-9]{5}$", id):
                    raise IncorrectValueException("L'identifiant doit comporter 2 lettres suivies de 5 chiffres ("
                                                  "AB12345)")
            except ValueError:
                print("Veuillez entrer une chaîne de caractères")
            except IncorrectValueException as incorrect_value:
                print(incorrect_value)
            else:
                return id