import keyboard

from views.basic_view import BasicView
from rich.padding import Padding
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Group
from rich.layout import Layout

class PlayerView(BasicView):
    """Menu where user can add new players to the database"""
    def __init__(self, console):
        super().__init__(console)
        self.name = "Joueurs enregistrés"
        self.players_list = []

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

        padded_table = Padding(table, (1,0,0,0))

        menu_options = Align.center(self.get_table_menu(current_selection))
        panel_menu_options = Panel(menu_options, title="Menu options",
                                           border_style="blue", padding=(1, 0),
                                           expand=False)
        padded_menu_options = Padding(panel_menu_options, 1)

        panel_title = f"[bold magenta]{self.name}[/bold magenta]"
        layout= Group(Align.center(padded_table),
                            Align.center(padded_menu_options))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)

    def render_new_player(self, current_selection):
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        table.add_row("ID joueur : ")
        panel = Panel(Align.center(table), title="puet")
        self.console.print(panel)
        # self.console.print(Panel(Align.center()))
        # keyboard.unhook_all()
        # bl = input("noice ")
        # bl = Prompt.ask("hey ")
        # table.add_row()
        # for index, menu in enumerate(self.accessible_menus):
        #     if index == current_selection:
        #         option_style = "bold white on blue"
        #     else:
        #         option_style = "white"
        #
        #     option_text = Text(menu, style=option_style)
        #     table.add_row(option_text)
