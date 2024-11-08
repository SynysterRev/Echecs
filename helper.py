class Helper:
    club_id =""

    text_menu = {"new_tournament" : "Créer un nouveau tournoi", "launch_tournament": "Démarrer un tournoi",
                 "add_players": "Ajouter des joueurs", "generate_reports": "Générer les rapports",
                 "identification_menu": "Identification menu", "quit": "Quitter", "main_menu": "Menu principal"}

    @classmethod
    def get_player_path(cls):
        return "data/" + cls.club_id + "/players/players.json"