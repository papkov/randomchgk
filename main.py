#!/usr/bin/env python
# -*- coding: utf-8 -*-
import player_path_generator as generator

players = int(input("Players: "))
# players_in_team = int(input("Количество игроков в команде: "))
# tours = int(input("Количество туров: "))

paths = generator.player_path_generator(players)

with open("paths.csv", "w") as f:
    for player in range(0, players):
        f.write(";".join(paths[player]))
        f.write("\n")

ex = input("\nPress any key")
# print(paths.values())
