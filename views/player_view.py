import re

from textual import on
from textual.app import ComposeResult
from textual.widgets import DataTable

from custom_exception import FormatIDException
from helpers.helper import Helper
from views.basic_view import BasicView
from textual.widgets import Button, Input, Label, Pretty
from helpers.validator import Validator
from textual.validation import Function

class PlayerView(BasicView):
    CSS = """
        DataTable {            
            border: solid white; /* Ajoute une bordure blanche */
            width: auto;
        }
        Input {
            width: auto;
        }
        """

    """Menu where user can add new players to the database"""
    def __init__(self, console):
        super().__init__(console)
        self.submit_button = None
        self.view_name = "Joueurs enregistrés"
        self.players_list = []
        self.inputs = {}

    def show_main_menu(self):
        self.show_heading_menu()
        for player in self.players_list:
            print(player)
        print()
        self.display_accessible_menus()
        return self.ask_for_user_choice(2)

    def ask_player_id(self):
        player_id = input("ID joueur : ")
        if not re.match(r"^[A-Z]{2}[1-9]{5}$", player_id):
            raise FormatIDException()
        return player_id

    def ask_player_name(self):
        return str(input("Nom : "))

    def ask_player_first_name(self):
        return str(input("Prenom : "))

    def compose(self) -> ComposeResult:
        table = DataTable(zebra_stripes=True)
        table.cursor_type = "none"
        table.add_columns("ID", "Prenom", "Nom", "Date de naissance")
        for player in self.players_list:
            table.add_row(player.player_id, player.first_name, player.name, player.birth_date)
        yield table

        yield Label("Entrez l'identifiant du joueur")
        self.inputs['id'] = Input(placeholder="AB12345", validators=[Function(Validator.is_id)])
        # self.inputs['id'].on_change = self.on_input_change
        yield self.inputs['id']

        yield Label("Entrez le nom du joueur")
        self.inputs['name'] = Input(placeholder="Bastide",validators=[Function(Validator.is_name)])
        # self.inputs['name'].on_change = self.on_input_change
        yield self.inputs['name']

        yield Label("Entrez le prénom du joueur")
        self.inputs['first_name'] = Input(placeholder="Jean", validators=[Function(Validator.is_name)])
        # self.inputs['first_name'].on_change = self.on_input_change
        yield self.inputs['first_name']

        yield Label("Entrez la date de naissance du joueur")
        self.inputs['birth_date'] = Input(placeholder="10/10/2000", validators=[Function(Validator.is_date)])
        # self.inputs['birth_date'].on_change = self.on_input_change
        yield self.inputs['birth_date']

        self.submit_button = Button("Ajouter joueur", disabled=True)
        yield self.submit_button
        for i in range(len(self.accessible_menus)):
            yield Button(Helper.text_menu[self.accessible_menus[i]], id=self.accessible_menus[i])

    def validate_inputs(self):
        all_valid = all(text_input.validate() for text_input in self.inputs.values())
        self.submit_button.disabled = not all_valid

        yield Pretty([])

    @on(Input.Changed)
    def on_input_change(self, message: Input.Changed):
        self.query_one(Pretty).update(message)
        for text_input in self.inputs.values():
            self.query_one(Pretty).update(text_input.value)
            all_valid = text_input.validate(text_input.value)
        self.submit_button.disabled = not all_valid

    def on_click_new_player(self):
        pass