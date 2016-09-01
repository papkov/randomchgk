import math
import random

# random.seed(2)

players = int(input("Количество игроков: "))
teams = math.ceil(float(players)/6)
print("Команд:", teams)
tours = int(input("Количество туров: "))

all_players = range(0, players)
played = []
players_with_players = {}
teams_for_players = {}

# Шаблон списка встреч игроков
for i in range(0, players):
    players_with_players[i] = []
    teams_for_players[i] = []

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


def get_next_player(team, players_with_players, all_players, played, shift):
    appropriate = []
    for player in all_players:
        played_together = False
        # Если игрок уже есть в этой команде - переходим к следующему
        if player in team:
            continue
        # Если игрок уже играл в этом туре - переходим к следующему
        if player in played:
            continue
        # Если игрок уже играл с другими игроками команды - переходим к следующему
        for player_in_team in team:
            if player_in_team is not None and player in players_with_players[player_in_team]:
                played_together = True
                break
        if played_together:
            continue


        # print("Add player", player)
        # print(player, end=", ")
        return player
        # appropriate.append(player)
        # if len(appropriate) == shift+1:
        #     return appropriate.pop()
    # Если что-то пошло не так
    # print("Something went wrong. Player wasn't found")
    # if len(appropriate) == 0:
    #     return None
    # random_player = random.choice(appropriate)
    # return random_player
    # return appropriate.pop()

print(recaps)
for tour in range(0, tours):
    played = []
    for player in range(0, 6):  # Количество игроков в команде
        for team in recaps.keys():
            next_player = get_next_player(recaps[team][tour], players_with_players, all_players, played, tour)
            recaps[team][tour].append(next_player)
            played.append(next_player)
    # Для всех игроков объявляем, что они сыграли друг с другом
    for team in recaps.keys():
        for player in recaps[team][tour]:
            if player is not None:
                players_with_players[player].extend(recaps[team][tour])
                teams_for_players[player].append(team)

    print("\nTour", tour)
    print(players_with_players[0])
    for team in recaps.keys():
        print(team, recaps[team])
    # print("Tour", tour, recaps)
    # print(players_with_players)

# print(recaps)
for player in teams_for_players.keys():
    print(player, teams_for_players[player])

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
