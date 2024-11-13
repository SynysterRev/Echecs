import datetime
import re

from views.basic_view import BasicView


class PlayerView(BasicView):
    def __init__(self):
        super().__init__()
        self.name = "Joueurs"
        self.players_list = []

    def show_menu(self):
        super().show_menu()
        print("Joueurs enregistrés : ")
        for player in self.players_list:
            print(player)
        print("1. Ajouter un nouveau joueur")
        print("2. Revenir au menu principal")
        return self.ask_for_user_choice(2)

    def ask_player_name(self):
        return str(input("Nom : "))

    def ask_player_first_name(self):
        return str(input("Prenom : "))

    def ask_player_birth_date(self):
        date = str(input("Date de naissance (ex : 01/01/1900): "))
        return datetime.datetime.strptime(date, "%d/%m/%Y")
