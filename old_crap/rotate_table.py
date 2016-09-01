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
    recaps[team] = []
    for tour in range(0, tours):
        recaps[team].append([])


# Заполнение стартовой таблицы на первый тур
player_generator = itertools.cycle(all_players)
for team in range(0, teams):
    for player in range(0, players_in_team):
        recaps[team][0].append(next(player_generator))


# Генерируем таблицу по турам
def get_new_column(recaps, tour, col):
    row = list()
    row.extend(recaps[col][tour])
    for extra_row in range(0, teams-players_in_team):
        row.append(recaps[teams-extra_row-1][tour][-1-col])
    column = list()
    column.extend(row[col:])
    column.extend(row[0:col])
    return column


def get_new_row(recaps, tour, r):
    row = list()
    for team in sorted(recaps.keys()):
        row.append(recaps[team][tour][r])
    row = row[r:] + row[0:r]
    return row

# Поворот влево
for tour in range(1, tours):
    print(tour)
    new_tour = []
    for team in range(0, players_in_team):
        row = get_new_row(recaps, tour-1, team)
        new_tour.append(row)

    for extra_col in range(0, teams - players_in_team):
        new_tour.append([])
        for player in range(0, players_in_team):
            new_tour[players_in_team+extra_col].append(new_tour[players_in_team-player-1][players_in_team+extra_col])

    for team in range(0, teams):
            recaps[team][tour] = new_tour[team][0:players_in_team]

    # for player in range(0, players_in_team):
    #     column = get_new_column(recaps, tour, player)
    #     for team in range(0, teams):
    #         recaps[team][tour+1].append(column[team])

# Поворот вправо
# for tour in range(1, tours):
#     for player in range(0, players_in_team):
#         column = get_new_column(recaps, tour-1, player)
#         for team in range(0, teams):
#             recaps[team][tour].append(column[team])
#

for tour in range(0, tours):
    for team in range(0, teams):
        for player in recaps[team][tour]:
            if player is not None:
                # players_with_players[player].extend(recaps[team][tour])
                teams_for_players[player].append(team)

for team in range(0, teams):
    print(chr(team+65), ': ', recaps[team], sep='')

for player in range(0, players):
    print('Игрок %s:' % player, end=' ')
    for tour in range(0, tours):
        print(chr(teams_for_players[player][tour] + 65), end=' ')
    print()

# Проверка распределения
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
