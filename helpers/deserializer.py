import json
import os
from typing import List

from helpers.helper import Helper
from models.player import Player
from models.tournament import Tournament


class Deserializer:
    @staticmethod
    def deserialize_players() -> List[Player]:
        players_list = []
        file_path = Helper.get_player_path()
        if os.path.exists(file_path):
            with open(Helper.get_player_path(), "r") as file:
                try:
                    json_data = json.load(file)
                    for player in json_data:
                        players_list.append(Player.deserialize(player))
                    return players_list
                except json.decoder.JSONDecodeError:
                    pass
        return []

    @staticmethod
    def deserialize_tournament() -> List[Tournament]:
        tournament_list = []
        file_path = Helper.get_tournament_path()
        if os.path.exists(file_path):
            files = os.listdir(file_path)
            for file in files:
                with open(file_path + file, "r") as json_file:
                    json_data = json.load(json_file)
                    tournament_list.append(Tournament.deserialize(json_data))
                return tournament_list
        return []
