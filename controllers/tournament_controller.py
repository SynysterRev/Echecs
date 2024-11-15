from controllers.base_controller import BaseController
from helpers.deserializer import Deserializer
from helpers.helper import Helper
from helpers.serializer import Serializer
from models.tournament import Tournament


class TournamentController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.accessible_menus = (Helper.get_new_tournament_menu(),
                                 Helper.get_modify_tournament_menu(),
                                 Helper.get_start_tournament_menu(),
                                 Helper.get_main_menu())

    def run(self):
        self.view.accessible_menus = self.accessible_menus
        while True:
            choice = self.get_user_choice(self.view.show_main_menu)
            if self.accessible_menus[choice] == Helper.get_new_tournament_menu():
                self.create_tournament()
            elif self.accessible_menus[choice] == Helper.get_modify_tournament_menu():
                self.modify_tournament()
            else:
                return self.accessible_menus[choice]



    def create_tournament(self):
        tournament_name = self.get_string_from_user("Nom : ")
        tournament_place = self.get_string_from_user("Lieu : ")
        tournament_date = self.get_date_from_user(self.view.ask_for_date,
                                                  "Date de début (ex : 01/01/1900) : ")
        while True:
            try:
                tournament_rounds = self.view.ask_tournament_number_rounds()
            except ValueError:
                self.view.show_type_int_error()
            else:
                break
        tournament_description = self.view.ask_tournament_description()
        players = Deserializer.deserialize_players()
        new_tournament = Tournament(tournament_name, tournament_place, tournament_date, players,
                                    tournament_description, tournament_rounds)
        Serializer.serialize_tournament(new_tournament)

    # continue it if enough time
    def modify_tournament(self):
        tournaments = Deserializer.deserialize_tournament()
        self.view.display_all_tournaments(tournaments)
        choice = self.view.ask_tournament_to_modify(len(tournaments))
        # players = tournament.players
        # players_encounters = {}
        # if self.current_tournament.current_round == 1:
        #     for player in players:
        #         players_encounters[player] = []
        #     random.shuffle(players)
        #     matches = []
        #     for i in range(0, len(self.current_tournament.players), 2):
        #         match = Match(players[i], players[i + 1])
        #         players_encounters[players[i]].append(players[i + 1])
        #         players_encounters[players[i + 1]].append(players[i])
        #         matches.append(match)
        #
        #     current_round = Round("Round 1", matches)
        #     self.current_tournament.add_round(current_round)
            # matches[0].set_winner(MatchResult.PLAYER_ONE)
            # matches[0].update_player_one_score(1)
            # matches[1].set_winner(MatchResult.PLAYER_TWO)
            # matches[1].update_player_one_score(1)


