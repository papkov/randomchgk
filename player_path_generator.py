#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import itertools


def player_path_generator(n_players, n_players_in_team=6, n_tours=7):

    n_teams = math.ceil(float(n_players) / n_players_in_team)
    if n_teams % 2 == 0:
        n_teams += 1

    print("I am going to generate %s teams" % n_teams)

    # Check if input values are incorrect
    if n_players < 31:
        print("Can't proceed less than 6 teams")
        print("Please enter bigger number of players (31 or more)")
        return
    elif n_players < 55 and n_tours > 7:
        print("Can't generate more than 7 tours for this number of players, sorry")
        n_tours = 7
    elif n_tours > 11:
        print("Can't generate more than 11 tours for this number of players, sorry")
        n_tours = 11

    all_players = []
    for player in range(0, n_teams * n_players_in_team):
        if player < n_players:
            all_players.append(player)
        else:
            all_players.append("None" + str(player))

    # Team labels - letters
    team_letters = []
    for i in range(0, n_teams):
        team_letters.append(chr(65+i))

    # Templates
    players_with_players = {}
    teams_for_players = {}
    for i in range(0, len(all_players)):
        players_with_players[all_players[i]] = []
        teams_for_players[all_players[i]] = []

    # Recaps dict contains team members for every tour
    recaps = {}
    for team in range(0, n_teams):
        recaps[team_letters[team]] = []
        for tour in range(0, n_tours):
            recaps[team_letters[team]].append([])

    # Templates for generator by columns
    players_by_index = []
    p = 0
    for player in range(0, n_players_in_team):
        players_by_index.append([])
        for team in range(0, n_teams):
            players_by_index[player].append(all_players[p])
            p += 1

    # Check
    def in_team(player, team):
        for other_player in team:
            if player in players_with_players[other_player]:
                return True
        return False

    #
    for tour in range(0, n_tours):
        player_shift = 0
        for player in range(0, n_players_in_team):  # Количество игроков в команде
            generator = (p for p in itertools.cycle(players_by_index[player]))
            shift = tour * player + player_shift
            # Miss shifted elements
            for i in range(shift):
                next(generator)
            for team in team_letters:
                next_player = next(generator)

                # Miss players that have already been in the same team with existing players
                while in_team(next_player, recaps[team][tour]):
                    next_player = next(generator)
                    player_shift += 1

                recaps[team][tour].append(next_player)

        # Players played with each other
        for team in recaps.keys():
            for player in recaps[team][tour]:
                if player is not None:
                    players_with_players[player].extend(recaps[team][tour])
                    teams_for_players[player].append(team)

        # print("\nTour", tour)
        # for team in recaps.keys():
        #     print(team, recaps[team])

    # Check if everything is correct
    players_with_players = {}
    for i in range(0, len(all_players)):
        players_with_players[all_players[i]] = []

    repeats = 0
    for player in teams_for_players:
        for other_player in teams_for_players:
            if player != other_player:
                for tour in range(0, n_tours):
                    if teams_for_players[player][tour] == teams_for_players[other_player][tour]:
                        if other_player in players_with_players[player]:
                            # print("Игрок", player, "уже играл с игроком", other_player)
                            repeats += 1
                        players_with_players[player].append(other_player)

    print('Repeats:', repeats)
    print('Average per player:', repeats/len(all_players))

    for player in range(0, n_players):
        print('Player %s:' % (player+1), end=' ')
        for tour in range(0, n_tours):
            print(teams_for_players[player][tour], end=' ')
        print()

    for tour in range(0, n_tours):
        print("\nTour:", tour+1)
        for team in sorted(recaps.keys()):
            print("Team:", team, end='\t')
            for player in recaps[team][tour]:
                if str(player).isdigit():
                    print(player, end=' ')
            print()

    return teams_for_players


def main():
    print("This program was not designed to run standalone")
    input("Press Enter to continue")

if __name__ == '__main__':
    main()
