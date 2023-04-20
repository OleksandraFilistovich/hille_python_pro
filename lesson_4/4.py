from copy import deepcopy
from typing import Any


def players_repr(players: list[dict], verbose: bool) -> None:
    if verbose:
        print(">> TEAM:")
        players = sorted(players, key=lambda x: x["name"])
        for player in players:
            print(
                f"   > name: {player['name']}, age: {player['age']}, "
                f"number: {player['number']}"
            )
    else:
        for player in players:
            print(f"{player['name']}, {player['age']}, {player['number']}")


def players_add(players: list[dict], player: dict) -> list[dict]:
    players = deepcopy(players)  # won't change given list and return new one
    players.append(player)

    return players


def players_del(players: list[dict], name: str) -> list[dict]:
    players = deepcopy(players)  # won't change given list and return new one
    for player in players:
        if player["name"] == name:
            players.remove(player)
            break
    return players


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    result = []
    for player in players:
        if str(player[field]) == value:
            result.append(player)
    return result


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    """If multiple players with same name - return the first one."""
    result = None
    for player in players:
        if player["name"] == name:
            result = player
            break
    return result


def main():
    test_team = [
        {"name": "Robin", "age": 30, "number": 1},
        {"name": "Demetrius", "age": 33, "number": 2},
        {"name": "Sebastian", "age": 23, "number": 3},
        {"name": "Maru", "age": 21, "number": 4},
        {"name": "Linus", "age": 31, "number": 5},
        {"name": "Caroline", "age": 28, "number": 6},
        {"name": "Robin", "age": 21, "number": 7},
        {"name": "Alex", "age": 20, "number": 8},
        {"name": "Sam", "age": 33, "number": 9},
        {"name": "Harvey", "age": 25, "number": 10},
    ]

    options = ["repr", "add", "del", "find", "get"]

    while True:
        print("\nPress 'Enter' to stop program.")
        if not (user_input := input(f"Enter your choice {options}:")):
            break

        if user_input == "repr":
            verbose_input = input("Do you want verbose print (y/n): ")
            if verbose_input == "y":
                players_repr(test_team, verbose=True)
            else:
                players_repr(test_team, verbose=False)

        elif user_input == "add":
            print({"Enter new player information"})
            add_name = input("name: ")
            add_age = input("age: ")
            add_num = input("number: ")
            add_player = {"name": add_name, "age": add_age, "number": add_num}

            new_team = players_add(test_team, add_player)
            print("-- team with added player --")
            players_repr(new_team, verbose=False)

        elif user_input == "del":
            del_name = input("Enter name of player you want to delete: ")

            new_team = players_del(test_team, del_name)
            print("-- team with deleted player --")
            players_repr(new_team, verbose=False)

        elif user_input == "find":
            print("Fields you can search by: 'name', 'age', 'number'")
            find_field = input("Enter name of field you want to search by: ")
            find_value = input("Enter field value: ")

            found_players = players_find(test_team, find_field, find_value)
            print(f"Players found for {find_field} = {find_value}:")
            players_repr(found_players, verbose=False)

        elif user_input == "get":
            find_name = input("Enter name of player you want to find: ")

            player = players_get_by_name(test_team, find_name)
            print(f"Player found: {player}")


if __name__ == "__main__":
    main()
