class Player:
    def __init__(self, name, first_name, birth_date):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date

    @staticmethod
    def deserialize(json_text: str) -> "Player":
        name = json_text["name"]
        first_name = json_text["first_name"]
        birth_date = json_text["birth_date"]
        return Player(name, first_name, birth_date)

