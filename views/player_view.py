from rich.align import Align
from rich.console import Group
from rich.padding import Padding
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

from views.basic_view import BasicView

class PlayerView(BasicView):
    """Menu where user can add new players to the database"""

    def __init__(self, console):
        super().__init__(console)
        self.name = "Joueurs enregistrés"
        self.players_list = []
        self.new_player_informations = ["ID joueur : ", "Nom : ", "Prénom : ", "Date de naissance : "]
        self.index_field = 0

    def show_main_menu(self):
        self.show_heading_menu()
        for player in self.players_list:
            print(player)
        print()
        self.display_accessible_menus()
        return self.ask_for_user_choice(2)

    def ask_player_id(self):
        return Prompt.ask("ID joueur")

    def ask_player_name(self):
        return Prompt.ask("Nom")

    def ask_player_first_name(self):
        return Prompt.ask("Prénom")

    def render(self, current_selection):
        table = Table()
        table.add_column("ID", justify="center")
        table.add_column("Prénom", justify="center")
        table.add_column("Nom", justify="center")
        table.add_column("Date de naissance", justify="center")

        for player in self.players_list:
            test = [player.player_id, player.first_name, player.name, player.birth_date]
            table.add_row(*test)

        padded_table = Padding(table, (1, 0, 0, 0))

        menu_options = Align.center(self.get_table_menu(current_selection))
        panel_menu_options = Panel(menu_options, title="Menu options",
                                   border_style="blue", padding=(1, 0),
                                   expand=False)
        padded_menu_options = Padding(panel_menu_options, 1)

        panel_title = f"[bold magenta]{self.name}[/bold magenta]"
        layout = Group(Align.center(padded_table),
                       Align.center(padded_menu_options))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)

    def render_new_player(self, current_input):
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        for index, information in enumerate(self.new_player_informations):
            table.add_row(self.get_input_display(information, current_input, index == self.index_field))

        panel_title = f"[bold magenta]{"Nouveau joueur"}[/bold magenta]"
        panel = Panel(Align.center(table), title=panel_title)
        self.console.print(panel)

    def get_input_display(self, player_information, current_input, is_current_field):
        if is_current_field:
            player_information += current_input
            return Text(f">{player_information}")
        else:
            return Text(player_information)

    def validate_information(self, final_input, field_index):
        if field_index < len(self.new_player_informations):
            self.new_player_informations[field_index] += final_input

    def change_information_input_index(self, new_field_index):
        self.index_field = new_field_index