from datetime import datetime
import re

from blessed import Terminal

from custom_exception import EmptyStringException, IDException
from models.player import Player


class BaseController:
    def __init__(self, view):
        """Base controller

        accessible_menus: id of all the menus that we can access from here
        view: view managed by the controller
        """
        self.view = view
        self.accessible_menus = ()
        self.current_selection = 0
        self.max_selection = 0
        self.players_list = []

    def run(self):
        self.view.accessible_menus = self.accessible_menus
        self.view.clear_view()
        self.view.render(self.current_selection)
        self.max_selection = len(self.accessible_menus)
        self.handle_input()
        return self.accessible_menus[self.current_selection]

    def handle_input(self):
        """Handle user input
           return False if the user select a menu -> we don't need to wait for the user input anymore"""

        term = Terminal()
        with term.cbreak():
            while True:
                key = term.inkey(timeout=0.1)
                if key:
                    if key.name == "KEY_ENTER":
                        return False
                    elif key.name == "KEY_UP":
                        self.move_up()
                    elif key.name == "KEY_DOWN":
                        self.move_down()

    def move_up(self):
        self.current_selection = (self.current_selection - 1) % self.max_selection
        self.render_view()

    def move_down(self):
        self.current_selection = (self.current_selection + 1) % self.max_selection
        self.render_view()

    def render_view(self):
        self.view.clear_view()
        self.view.render(self.current_selection)

    def is_input_not_empty(self, user_input):
        if len(user_input) > 0 and user_input[0] != " ":
            return True
        else:
            raise EmptyStringException()

    def is_input_int(self, user_input):
        try:
            int_input = int(user_input)
            if int_input > 0:
                return True
            else:
                raise ValueError()
        except ValueError:
            raise ValueError("Veuillez entrer un nombre positif et supérieur à 0")

    def validate_date(self, date):
        try:
            is_date = bool(datetime.strptime(date, "%d/%m/%Y"))
            return is_date
        except ValueError:
            raise ValueError("La date doit être au format JJ/MM/AAAA")

    def get_user_input(self, view_func, validate_func, default_input=""):
        term = Terminal()
        user_input = default_input
        with term.cbreak():
            while True:
                key = term.inkey(timeout=0.1)
                if key:
                    if key.name == "KEY_ENTER":
                        if validate_func(user_input):
                            return user_input
                    elif key.name == "KEY_BACKSPACE":
                        user_input = user_input[:-1]
                        self.view.current_input = user_input
                        view_func()
                    # avoid special key like arrow or F1 to be counted
                    elif key.name is None:
                        user_input += key
                        self.view.current_input = user_input
                        view_func()

    def ask_for_new_player(self):
        index_field = 0
        self.view.index_field = 0
        self.view.clear_view()
        self.view.render_new_player()
        method_per_index = {0: (self.is_player_id_valid, IDException),
                            1: (self.is_input_not_empty, EmptyStringException),
                            2: (self.is_input_not_empty, EmptyStringException),
                            3: (self.validate_date, ValueError)}
        new_player_informations = []
        while True:
            last_input = ""
            while True:
                try:
                    final_input = self.get_user_input(self.handle_information_player_input,
                                                      method_per_index[index_field][0], last_input)
                except method_per_index[index_field][1] as exception:
                    last_input = self.view.current_input
                    self.view.clear_view()
                    self.view.render_new_player(exception)
                else:
                    break
            self.view.current_input = ""
            new_player_informations.append(final_input)
            index_field += 1
            if index_field == 4:
                break
            self.view.change_information_input_index(index_field)
            self.view.validate_player_information(final_input, index_field - 1)
            self.handle_information_player_input()
        new_player = Player(new_player_informations[0],
                            new_player_informations[1],
                            new_player_informations[2],
                            new_player_informations[3])
        self.view.clear_player_informations()
        return new_player

    def is_player_id_valid(self, new_player_id):
        if not re.match(r"^[A-Z]{2}[1-9]{5}$", new_player_id):
            raise IDException("L'identifiant doit comporter 2 lettres suivies de 5 chiffres (AB12345)")
        if any(new_player_id == player.player_id for player in self.players_list):
            raise IDException("Cet identifiant existe déjà dans la base de données")
        return True

    def handle_information_player_input(self):
        self.view.clear_view()
        self.view.render_new_player()
