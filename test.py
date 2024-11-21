from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll, VerticalScroll
from textual.screen import Screen
from textual.widgets import Placeholder


class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """


class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """


class Tweet(Placeholder):
    DEFAULT_CSS = """
    Tweet {
        height: 5;
        width: 1fr;
        border: tall $background;
    }
    """


class Column(VerticalScroll):
    DEFAULT_CSS = """
    Column {
        height: 1fr;
        width: 32;
        margin: 0 2;
    }
    """

    def compose(self) -> ComposeResult:
        for tweet_no in range(1, 20):
            yield Tweet(id=f"Tweet{tweet_no}")


class Label(Placeholder):
    DEFAULT_CSS = """
        Label {
            width: 1fr;
        }
        """


class Input(Placeholder):
    DEFAULT_CSS = """
           Input {
               width: 1fr;
           }
           """

class LabelWithInput(Placeholder):
    DEFAULT_CSS = """
    LabelWithInput {
        width: 1fr;
    }
    """
    def compose(self) -> ComposeResult:
        yield Label(id="Label")
        yield Input(id="Input")


class TweetScreen(Screen):
    def compose(self) -> ComposeResult:
        # yield LabelWithInput()
        yield Header(id="Header")
        yield Footer(id="Footer")
        with HorizontalScroll():
            yield Column()
            yield Column()
            yield Column()
            yield Column()

class LayoutApp(App):
    def on_ready(self) -> None:
        self.push_screen(TweetScreen())

if __name__ == "__main__":
    app = LayoutApp()
    app.run()