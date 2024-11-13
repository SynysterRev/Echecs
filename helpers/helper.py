class Helper:
    club_id = ""

    text_menu = {"new_tournament": "Créer un nouveau tournoi", "launch_tournament": "Démarrer un tournoi",
                 "add_players": "Ajouter des joueurs", "generate_reports": "Générer les rapports",
                 "identification_menu": "Changer de club", "quit": "Quitter", "main_menu": "Menu principal"}

    @classmethod
    def get_player_path(cls):
        return "data/" + cls.club_id + "/players/players.json"

    @staticmethod
    def get_main_menu():
        return "main_menu"

    @staticmethod
    def get_identification_menu():
        return "identification_menu"

    @staticmethod
    def get_new_tournament_menu():
        return "new_tournament"

    @staticmethod
    def get_add_players_menu():
        return "add_players"

    @staticmethod
    def get_generate_reports_menu():
        return "generate_reports"

    @staticmethod
    def get_quit():
        return "quit"

    @staticmethod
    def get_launch_tournament_menu():
        return "launch_tournament"
