class Helper:
    text_menu = {"tournament_menu": "Gérer les tournois", "new_tournament": "Créer un nouveau tournoi",
                 "start_tournament": "Démarrer un tournoi", "start_round": "Démarrer un tour",
                 "start_match": "Démarrer un match", "players_menu": "Gérer les joueurs",
                 "add_player": "Ajouter un nouveau joueur",
                 "generate_reports": "Générer les rapports", "quit": "Quitter", "main_menu": "Menu principal",
                 "match_result": "Résultat du match", "players_report": "Liste des joueurs",
                 "tournaments_report": "Liste des tournois",
                 "tournament_players_report": "Liste des joueurs pour un tournoi",
                 "tournament_rounds_report": "Tours d'un tournoi",
                 "import_players": "Importer tous les joueurs", "back": "Retour",
                 "select_players": "Sélectionner des joueurs", "validate": "Valider"}

    @classmethod
    def get_player_path(cls):
        """Get the path where the json players is stored"""
        return "data/players/"

    @classmethod
    def get_tournament_path(cls):
        """Get the path where the jsons tournaments are stored"""
        return "data/tournaments/"

    @staticmethod
    def get_main_menu():
        """Get the text used to go to the main menu"""
        return "main_menu"

    @staticmethod
    def get_new_tournament_menu():
        """Get the text used to go to the menu to create a new tournament"""
        return "new_tournament"

    @staticmethod
    def get_players_menu():
        """Get the text used to go to the menu to create new players"""
        return "players_menu"

    @staticmethod
    def get_add_player():
        """Get the text used to go to the add player menu"""
        return "add_player"

    @staticmethod
    def get_generate_reports_menu():
        """Get the text used to go to the generate reports menu"""
        return "generate_reports"

    @staticmethod
    def get_quit():
        """Get the text used to quit the program"""
        return "quit"

    @staticmethod
    def get_start_tournament_menu():
        """Get the text used to go to the flow tournament menu"""
        return "start_tournament"

    @staticmethod
    def get_tournament_menu():
        """Get the text used to go to the tournament menu"""
        return "tournament_menu"

    @staticmethod
    def get_start_round_menu():
        """Get the text used to go to the flow round menu"""
        return "start_round"

    @staticmethod
    def get_start_match_menu():
        """Get the text used to go to the selection of a winner in match menu"""
        return "start_match"

    @staticmethod
    def get_match_result_menu():
        """Get the text used to go to the results of all matches menu"""
        return "match_result"

    @staticmethod
    def get_players_report_menu():
        """Get the text used to go to the players report menu"""
        return "players_report"

    @staticmethod
    def get_tournaments_report_menu():
        """Get the text used to go to the tournaments report menu"""
        return "tournaments_report"

    @staticmethod
    def get_tournament_players_report_menu():
        """Get the text used to go to the players participating in a tournament report menu"""
        return "tournament_players_report"

    @staticmethod
    def get_tournament_rounds_report_menu():
        """Get the text used to go to the rounds report menu"""
        return "tournament_rounds_report"

    @staticmethod
    def get_import_players_menu():
        """Get the text used to import all players in a tournament"""
        return "import_players"

    @staticmethod
    def get_select_players_menu():
        """Get the text used to select players who are going to play in a tournament"""
        return "select_players"

    @staticmethod
    def get_validate():
        """Get the text used to validate a choice"""
        return "validate"

    @staticmethod
    def get_back():
        """Get the text used to go back to the previous menu"""
        return "back"
