from controllers.main_controller import MainController
from views.view_manager import ViewManager


def main():
    view_manager = ViewManager()
    main_controller = MainController(view_manager)
    main_controller.run()

if __name__ == "__main__":
    main()
