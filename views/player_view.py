from textual import on, events
from textual.app import ComposeResult
from textual.widgets import Button, Input, Pretty
from textual.widgets import DataTable

from helpers.helper import Helper
from views.basic_view import BasicView
from views.widgets.new_player_widget import NewPlayerWidget


class PlayerView(BasicView):
    CSS = """
    # Screen {
    #     align: center middle;
    # }
        DataTable {            
            border: solid white; /* Ajoute une bordure blanche */
            width: auto;
        }
        """
    CSS_PATH = "widgets/player.tcss"
    """Menu where user can add new players to the database"""

    def __init__(self, console):
        super().__init__(console)
        self.view_name = "Joueurs enregistrés"
        self.players_list = []
        self.new_player_event = None
        self.main_menu_event = None
        self.new_player_widget= None

    def compose(self) -> ComposeResult:
        table = DataTable(zebra_stripes=True)
        table.cursor_type = "none"
        table.add_columns("ID", "Prenom", "Nom", "Date de naissance")
        for player in self.players_list:
            table.add_row(player.player_id, player.first_name, player.name, player.birth_date)
        yield table

        yield NewPlayerWidget(id="add_player")

        yield Button(Helper.text_menu[self.accessible_menus[1]], id=self.accessible_menus[1])

        yield Pretty("")

    def _on_mount(self, event: events.Mount) -> None:
        self.new_player_widget = self.query_one("#add_player")

    def get_player_data(self):
        return self.new_player_widget.get_player_data()
        # return {
        #     "player_id": self.inputs['id'].value,
        #     "name": self.inputs['name'].value,
        #     "first_name": self.inputs['first_name'].value,
        #     "birth_date": self.inputs['birth_date'].value
        # }

    def update_player_list(self, new_player):
        self.players_list.append(new_player)
        self.query_one(DataTable).add_row(new_player.player_id, new_player.first_name, new_player.name,
                                          new_player.birth_date)

    @on(NewPlayerWidget.Pressed, "#add_player")
    def add_new_player(self):
        self.new_player_event(self.get_player_data())

    @on(Button.Pressed, "#main_menu")
    def main_menu(self):
        self.main_menu_event()

    def show_new_player_error(self):
        self.query_one(Pretty).update("L'ID du joueur existe déjà")

    def show_new_player_success(self):
        self.query_one(Pretty).update("Joueur ajouté avec succès")
