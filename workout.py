import requests
from dotenv import load_dotenv
import os

load_dotenv()
def fetch_poster(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?external_source="
    headers = {
        "accept": "application/json",
        "Authorization": os.getenv("AUTHORIZATION")
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        url = f"https://api.themoviedb.org/3/tv/{id}?external_source="

        headers = {
            "accept": "application/json",
            "Authorization": os.getenv("AUTHORIZATION")
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            #print("404Error.png")
            return "404Error.png"
        data = response.json()
        if data["poster_path"] == None:
            return "404Error.png"
        #print("Series: ",data["poster_path"])
        return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    data = response.json()
    if data["poster_path"] == None:
        return "404Error.png"
    #print("Movie: ",data["poster_path"])
    return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

"""
movie_id:  18924 movie_title:  Pink Sin
movie_id:  296 movie_title:  Ant-Man
movie_id:  12264 movie_title:  Prophet Joseph
movie_id:  15332 movie_title:  Turbo FAST
movie_id:  8443 movie_title:  Sikander 2
"""
#print(fetch_poster(298618))
"""print(fetch_poster(296))
print(fetch_poster(12264))
print(fetch_poster(15332))
print(fetch_poster(8443))"""