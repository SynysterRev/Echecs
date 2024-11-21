from views.basic_view import BasicView
from textual.widgets import Button

class MenuView(BasicView):
    """Main menu of the application"""
    def __init__(self, console):
        super().__init__(console)
        self.view_name = "Menu principal"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if not self.handle_event:
            for callback in self.subscribers:
                callback(event.button.id)