import math
import itertools

players = int(input("Количество игроков: "))
players_in_team = int(input("Количество игроков в команде: "))
teams = math.ceil(float(players) / players_in_team)
print("Будет сгенерировано команд:", teams)
tours = int(input("Количество туров: "))

all_players = []
for player in range(0, teams * players_in_team):
    if player < players:
        all_players.append(player)
    else:
        all_players.append("None" + str(player))

# played = []
players_with_players = {}
teams_for_players = {}

# Шаблон списка встреч игроков
for i in range(0, len(all_players)):
    players_with_players[all_players[i]] = []
    teams_for_players[all_players[i]] = []

# Названия команд - буквы
team_letters = []
for i in range(0, teams):
    team_letters.append(chr(65+i))

# Генерация шаблонов списка составов команд
recaps = {}
for team in range(0, teams):
    recaps[team_letters[team]] = []
    for tour in range(0, tours):
        recaps[team_letters[team]].append([])

# Генерация шаблона столбцов по номерам игроков
players_by_index = []
p = 0
for player in range(0, players_in_team):
    players_by_index.append([])
    for team in range(0, teams):
        players_by_index[player].append(all_players[p])
        p += 1

print(players_by_index)

for tour in range(0, tours):
    for player in range(0, players_in_team):  # Количество игроков в команде
        generator = (p for p in itertools.cycle(players_by_index[player]))
        # shift = tour * player
        # # Пропустить элементы со сдвигом
        # for i in range(shift):
        #     next(generator)

        # Для первого игрока сразу заполняем столбец без сдвига
        if player == 0:
            recaps["A"][tour].append(next(generator))
        else:
            # Поиск оптимального сдвига
            played_together = True
            while played_together:
                next_player = next(generator)
                played_together = False
                for player_already_in_team in recaps["A"][tour]:  # Для всех игроков, которые уже есть в первой команде
                    if next_player in players_with_players[player_already_in_team]:
                        played_together = True
                        # print("Игрок", next_player, "уже играл с игроком", player_already_in_team)
                if not played_together:
                    recaps["A"][tour].append(next_player)

        for team in sorted(recaps.keys())[1:]:
            next_player = next(generator)
            recaps[team][tour].append(next_player)
    # Для всех игроков объявляем, что они сыграли друг с другом
    for team in recaps.keys():
        for player in recaps[team][tour]:
            if player is not None:
                players_with_players[player].extend(recaps[team][tour])
                teams_for_players[player].append(team)
    # print(players_with_players[0])
    print("\nTour", tour)
    for team in sorted(recaps.keys()):
        print(team, recaps[team])
# for team in sorted(recaps.keys()):
#     print(team, recaps[team])
# Проверка корректности распределения
players_with_players = {}
for i in range(0, len(all_players)):
    players_with_players[all_players[i]] = []

repeats = 0
for player in teams_for_players:
    for other_player in teams_for_players:
        if player != other_player:
            for tour in range(0, tours):
                if teams_for_players[player][tour] == teams_for_players[other_player][tour]:
                    if other_player in players_with_players[player]:
                        pass
                        # print("Игрок", player, "уже играл с игроком", other_player)
                        repeats += 1
                    players_with_players[player].append(other_player)

print('Повторных пересечений:', repeats)
print('В среднем на игрока:', repeats/len(all_players))


# combinations = itertools.combinations(all_players, 6)
# i = 0
# print(sum(1 for _ in combinations))
for player in sorted(teams_for_players.keys()):
    print(player, teams_for_players[player])
