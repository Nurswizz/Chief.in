import requests

def fetch_recipes(query, app_id, app_key):
    base_url = "https://api.edamam.com/search"
    endpoint = ""
    params = {
        "q": query,
        "app_id": app_id,
        "app_key": app_key
    }

    response = requests.get(base_url + endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("hits", [])
    else:
        print(f"Failed to fetch recipes. Status code: {response.status_code}")
        return []

def parse(query):
    recipes = fetch_recipes(query, "91c5b683", "286540e192be31c8a248139bf56f734d")

    if recipes:
        return recipes[0]['recipe']
    else:
        return False


