import requests

url = "https://api.jikan.moe/v4/anime"

def get_anime_details():
    
    params = {
        "page":1,
        "limit":25
        }
    
    response = requests.get(url,params=params)
    
    data = response.json()
    anime_list = []
    for anime in data["data"]:
        anime_list.append(anime)
        print(anime["title"])
    # print(anime_list)