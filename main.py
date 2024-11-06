from controllers.tournament_controller import TournamentController

def main():
    controller = TournamentController()
    controller.start_new_round()
    # controller.run()

if __name__ == "__main__":
    main()