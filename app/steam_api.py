import requests
from config import STEAM_API_KEY, STEAM_ID


def get_owned_games():
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"

    params = {
        "key": STEAM_API_KEY,
        "steamid": STEAM_ID,
        "include_appinfo": True,
        "include_played_free_games": True
    }

    response = requests.get(url, params=params)

    return response.json()