import json
from typing import List

from helper import Helper
from models.player import Player


class Deserializer:
    @staticmethod
    def deserialize_players() -> List[Player]:
        players_list = []
        with open(Helper.get_player_path(), "r") as file:
            json_data = json.load(file)
            for player in json_data["players"]:
                players_list.append(Player.deserialize(player))
        return players_list
