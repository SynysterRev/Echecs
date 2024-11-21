from textual import events, on
from textual.message import Message
from textual.widgets import Input, Label
from textual.widgets import Static


class LabelledInput(Static):
    class Changed(Message):
        def __init__(self, value: str) -> None:
            super().__init__()
            self.value = value


    def __init__(self, label: str, input_placeholder: str, validators: [], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_text = label
        self.input_placeholder = input_placeholder
        self.validators = validators
        self.input = None

    def compose(self):
        yield Label(self.label_text)
        yield Input(placeholder=self.input_placeholder, validators=self.validators)

    def _on_mount(self, event: events.Mount) -> None:
        self.input = self.query_one(Input)

    def get_input(self):
        return self.input

    @on(Input.Changed)
    def on_input_changed(self, message: Input.Changed):
        self.post_message(self.Changed(message.value))
