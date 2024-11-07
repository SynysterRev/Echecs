class BasicView:
    def __init__(self):
        self.name = ""

    def show_menu(self):
        """Allow some basic formatting for derived views"""
        print("\n")
        print(self.name)
        print("--------------------------")