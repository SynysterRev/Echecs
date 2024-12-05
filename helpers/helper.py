class Helper:
    text_menu = {"tournament_menu": "Gérer les tournois", "new_tournament": "Créer un nouveau tournoi",
                 "modify_tournament": "Modifier un tournoi", "start_tournament": "Démarrer un tournoi",
                 "start_round": "Démarrer un tour", "start_match": "Démarrer un match",
                 "players_menu": "Gérer les joueurs", "add_player": "Ajouter un nouveau joueur",
                 "generate_reports": "Générer les rapports", "quit": "Quitter", "main_menu": "Menu principal",
                 "match_result": "Résultat du match", "players_report": "Liste des joueurs",
                 "tournaments_report": "Liste des tournois",
                 "tournament_players_report": "Liste des joueurs pour un tournoi",
                 "tournament_rounds_report": "Tours d'un tournoi"}

    @classmethod
    def get_player_path(cls):
        return "data/players/players.json"

    @classmethod
    def get_tournament_path(cls):
        return "data/tournaments/"

    @staticmethod
    def get_main_menu():
        return "main_menu"

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
    def get_start_tournament_menu():
        return "start_tournament"

    @staticmethod
    def get_tournament_menu():
        return "tournament_menu"

    @staticmethod
    def get_modify_tournament_menu():
        return "modify_tournament"

    @staticmethod
    def get_start_round_menu():
        return "start_round"

    @staticmethod
    def get_start_match_menu():
        return "start_match"

    @staticmethod
    def get_match_result_menu():
        return "match_result"

    @staticmethod
    def get_players_report_menu():
        return "players_report"

    @staticmethod
    def get_tournaments_report_menu():
        return "tournaments_report"

    @staticmethod
    def get_tournament_players_report_menu():
        return "tournament_players_report"

    @staticmethod
    def get_tournament_rounds_report_menu():
        return "tournament_rounds_report"
