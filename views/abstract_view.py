from abc import ABC

class AbstractView(ABC):
    def __init__(self):
        self.name = ""

    def show_menu(self):
        print(self.name)
        print("--------------------------")