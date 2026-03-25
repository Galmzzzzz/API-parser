import requests
import json


def parser():

    limit = 2_000

    url = f"https://korter.kz/pyapi/building/cards?geo_object_ids=1&offset=80&limit={limit}&sort_geo_object_id=1&locale=ru-RU"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return data

