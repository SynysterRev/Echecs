from controllers.tournament_controller import TournamentController
from controllers.base import Controller
from views.menu_view import MenuView
from views.base import View
from views.identification_view import IdentificationView
from controllers.identification_controller import IdentificationController

def main():
    menu_view = IdentificationView()
    view = View(menu_view, None)
    controller = IdentificationController()
    controller.run()

if __name__ == "__main__":
    main()