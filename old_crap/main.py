import math


def team_shift(path, shift=1):
    teams = len(path)
    shifted_path = []
    start = 0
    while len(shifted_path) < teams:
        for i in range(start, teams, shift):
            shifted_path.append(path[i])
        start += 1
    return shifted_path


def tour_generator(path, players):
    tour_sequence = []
    number_of_shifts = math.ceil(float(players)/len(path))
    for i in range(0, number_of_shifts):
        tour_sequence.extend(team_shift(path, i+1))
    return tour_sequence


players = int(input("Количество игроков: "))
teams = math.ceil(float(players)/6)
print("Команд:", teams)

paths = []
players_with_players = {}
teams_for_players = {}

for i in range(0, teams):
    paths.append(chr(65+i))

print(paths)
tour_sequence = tour_generator(paths, players)
print(tour_sequence)

for i in range(0, players):
    players_with_players[str(i+1)] = []
    teams_for_players[str(i+1)] = []

# print(players_with_players)

tours = int(input("Количество туров: "))

# Расширение массива, чтобы не выходить за пределы
tour_sequence.extend(tour_sequence[0:tours])

for tour in range(0, tours):
    for player in range(0, players):
        teams_for_players[str(player+1)].append(tour_sequence[player+tour-round(tours/2)])

# Итоговая таблица
for player in teams_for_players:
    print(player, teams_for_players[player])

# Проверка корректности распределения
for player in teams_for_players:
    for other_player in teams_for_players:
        if player != other_player:
            for tour in range(0, tours):
                if teams_for_players[player][tour] == teams_for_players[other_player][tour]:
                    if other_player in players_with_players[player]:
                        print("Игрок", player, "уже играл с игроком", other_player)
                    players_with_players[player].append(other_player)

for player in players_with_players:
    print(player, players_with_players[player])



