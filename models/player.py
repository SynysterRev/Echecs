class Player:
    def __init__(self, name, first_name, birth_date):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date

    @staticmethod
    def deserialize(json_text) -> "Player":
        name = json_text["name"]
        first_name = json_text["first_name"]
        birth_date = json_text["birth_date"]
        return Player(name, first_name, birth_date)

    def serialize(self):
        return {"name": self.name, "first_name": self.first_name, "birth_date": self.birth_date}

    def __str__(self):
        return self.first_name + " " + self.name + " né le " + self.birth_date

