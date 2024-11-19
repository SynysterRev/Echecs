class Player:
    def __init__(self, player_id, name, first_name, birth_date):
        self.player_id = player_id
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date

    @staticmethod
    def deserialize(json_text) -> "Player":
        player_id = json_text["player_id"]
        name = json_text["name"]
        first_name = json_text["first_name"]
        birth_date = json_text["birth_date"]
        return Player(player_id, name, first_name, birth_date)

    def serialize(self):
        return {"player_id": self.player_id, "name": self.name, "first_name": self.first_name, "birth_date":
            self.birth_date}

    def __str__(self):
        return f"{self.first_name} {self.name} (ID : {self.player_id})"

