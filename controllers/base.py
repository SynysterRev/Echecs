# from models.tournament import Tournament
# from models.round import Round
# from models.player import Player
# from models.match import Match
# from models.match import MatchResult
# import random
# from typing import List
#
# class Controller:
#     def sort_player_by_points(self, player):
#         return player[1]
#
#     def is_match_already_done(self, players_encounters, player_one, player_two):
#         return player_two in players_encounters[player_one]
#
#     def get_best_match(self, players_encounters, current_player, all_players):
#         for player in all_players[1:]:
#             if not self.is_match_already_done(players_encounters, current_player[0], player[0]):
#                 players_encounters[current_player[0]].append(player[0])
#                 players_encounters[player[0]].append(current_player[0])
#                 return Match(current_player, player)
#
#     def create_matches(self, players_points, players_encounters, tournament):
#         players_points.sort(key=self.sort_player_by_points, reverse=True)
#         all_matches = []
#         for round in tournament.rounds:
#             for match in round.matches:
#                 all_matches.append(match)
#
#         players_to_place = players_points
#         current_player = players_to_place[0]
#         new_matches = []
#         while len(players_to_place) > 0:
#             new_match = self.get_best_match(players_encounters, current_player, players_to_place)
#             players_to_place.remove(new_match.players_score[0])
#             players_to_place.remove(new_match.players_score[1])
#             new_matches.append(new_match)
#             if len(players_to_place) > 0:
#                 current_player = players_to_place[0]
#         return new_matches
#
#
#
#     def start_tournament(self, tournament: Tournament):
#         players = tournament.players
#         players_encounters = {}
#         for player in players:
#             players_encounters[player] = []
#         if tournament.current_round == 1:
#             random.shuffle(players)
#             matches = []
#             for i in range(0, len(tournament.players), 2):
#                 match = Match(players[i], players[i + 1])
#                 players_encounters[players[i]].append(players[i + 1])
#                 players_encounters[players[i + 1]].append(players[i])
#                 matches.append(match)
#
#             current_round = Round("Round 1", matches)
#             tournament.add_round(current_round)
#             matches[0].set_winner(MatchResult.PLAYER_ONE)
#             matches[0].update_player_one_score(1)
#             matches[1].set_winner(MatchResult.PLAYER_TWO)
#             matches[1].update_player_one_score(1)
#
#
#             new_matches = self.create_matches(players_points, players_encounters, tournament)
#             new_round = Round("Round two", new_matches)
#             new_matches[0].set_winner(MatchResult.PLAYER_ONE)
#             new_matches[0].update_player_one_score(1)
#             new_matches[1].set_winner(MatchResult.PLAYER_TWO)
#             new_matches[1].update_player_two_score(1)
#             tournament.add_round(new_round)
#
#     def start_round(self, tournament: Tournament):
#         current_round = tournament.rounds[tournament.current_round]
#         current_round.start_round()
#         round_matches = current_round.matches
#
#     def get_matches_current_round(self):
#
#
#
#     def run(self):
#         players = [Player("Marley", "Bob", "10/12/1099"),
#                    Player("Pascal", "Bob", "10/10/1099"),
#                    Player("Tristan", "Bob", "10/03/1099"),
#                    Player("Robert", "Bob", "10/10/1089"),
#                    Player("Jacques", "Bob", "10/03/1199"),
#                    Player("Lucien", "Bob", "10/05/1099")]
#         tournament = Tournament("test", "France", "today", players, "Ceci est un test")
#         self.start_tournament(tournament)
#
