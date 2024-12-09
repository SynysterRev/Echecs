import json
import os

from helpers.helper import Helper


class Serializer:
    @staticmethod
    def serialize_player(player):
        """Serialize a player and save it in a json file"""
        file_data = []
        file_path = Helper.get_player_path()
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                try:
                    file_data = json.load(file)
                except json.decoder.JSONDecodeError:
                    pass
        file_data.append(player.serialize())
        with open(file_path, "w+") as file:
            json.dump(file_data, file, indent=4, separators=(',', ': '))

    @staticmethod
    def serialize_tournament(tournament):
        """Serialize a tournament and save it in a json file"""
        file_path = Helper.get_tournament_path() + tournament.name + ".json"
        try:
            os.makedirs(Helper.get_tournament_path(), exist_ok=True)
        except PermissionError:
            print(f"Impossible de créer '{Helper.get_tournament_path()}', vous n'avez pas les droits.")
            return
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return
        with open(file_path, "w") as file:
            json.dump(tournament.serialize(), file, indent=4, separators=(',', ': '))
