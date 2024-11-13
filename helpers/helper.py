class Helper:
    club_id = ""

    text_menu = {"tournament_menu": "Gérer les tournois", "new_tournament": "Créer un nouveau tournoi",
                 "modify_tournament": "Modifier un tournoi", "launch_tournament": "Démarrer un tournoi",
                 "players_menu": "Gérer les joueurs", "add_player": "Ajouter un nouveau joueur",
                 "generate_reports": "Générer les rapports", "identification_menu": "Changer de club",
                 "quit": "Quitter", "main_menu": "Menu principal"}

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
    def get_players_menu():
        return "players_menu"

    @staticmethod
    def get_add_player():
        return "add_player"

    @staticmethod
    def get_generate_reports_menu():
        return "generate_reports"

    @staticmethod
    def get_quit():
        return "quit"

    @staticmethod
    def get_launch_tournament_menu():
        return "launch_tournament"

    @staticmethod
    def get_tournament_menu():
        return "tournament_menu"

    @staticmethod
    def get_modify_tournament_menu():
        return "modify_tournament"
