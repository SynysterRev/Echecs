import json
import os

from helpers.helper import Helper
from models.player import Player


class Serializer:
    @staticmethod
    def serialize_player(player):
        file_data = []
        file_path = Helper.get_player_path()
        if os.path.exists(file_path):
            with open(Helper.get_player_path(), "r") as file:
                file_data = json.load(file)
                file_data.append(Player.serialize(player))
        with open(file_path, "w+") as file:
            json.dump(file_data, file, indent=4, separators=(',',': '))