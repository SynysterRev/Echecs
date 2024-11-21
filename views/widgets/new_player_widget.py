from textual import events, on
from textual.validation import Function, Length, Regex
from textual.widgets import Button
from textual.widgets import Static
from textual.message import Message

from helpers.validator import Validator
from views.widgets.label_input import LabelledInput


class NewPlayerWidget(Static):
    """Custom widget for adding new players"""

    class Pressed(Message):
        def __init__(self, button: Button) -> None:
            super().__init__()
            self.button: Button = button

        @property
        def control(self) -> Button:
            """An alias for [Pressed.button][textual.widgets.Button.Pressed.button].

            This will be the same value as [Pressed.button][textual.widgets.Button.Pressed.button].
            """
            return self.button

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inputs = {}
        self.submit_button = None

    def compose(self):
        yield LabelledInput("ID", "AB12345", [Regex(r"^[A-Z]{2}[1-9]{5}$")], id="id")
        yield LabelledInput("Nom", "Bastide", [Length(minimum=1)], id="name")
        yield LabelledInput("Prénom", "Jean", [Length(minimum=1)], id="firstName")
        yield LabelledInput("Date de naissance", "10/10/2000", [Function(Validator.is_date)], id="birthDate")
        yield Button("+", disabled=True, id="add_player")

    def _on_mount(self, event: events.Mount) -> None:
        self.inputs["id"] = (self.query_one("#id"))
        self.inputs["name"] = (self.query_one("#name"))
        self.inputs["firstName"] = (self.query_one("#firstName"))
        self.inputs["birthDate"] = (self.query_one("#birthDate"))
        self.submit_button = self.query_one(Button)

    @on(LabelledInput.Changed)
    def on_labelled_input_change(self, message: LabelledInput.Changed):
        self.submit_button.disabled = self.are_all_inputs_valid()

    def are_all_inputs_valid(self) -> bool:
        return not (all(text_input.get_input().is_valid for text_input in self.inputs.values())
                    and all(text_input.get_input().value for text_input in self.inputs.values()))

    @on(Button.Pressed)
    def on_add_player_pressed(self, message: Button.Pressed):
        self.post_message(self.Pressed(message.button))

    def get_player_data(self):
        return {
            "player_id": self.inputs['id'].get_input().value,
            "name": self.inputs['name'].get_input().value,
            "first_name": self.inputs['firstName'].get_input().value,
            "birth_date": self.inputs['birthDate'].get_input().value
        }
