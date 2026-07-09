from steam_api import get_owned_games


def main():
    data = get_owned_games()

    print(data)


if __name__ == "__main__":
    main()