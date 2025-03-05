import requests
import random

API_KEY = "0dc885cbd7f5091d59e943be90a59a43" 
BASE_URL = "https://api.themoviedb.org/3"

def get_genre_id(genre_name):
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    genres = response.json()["genres"]
    for genre in genres:
        if genre["name"]==genre_name:
            return genre['id']
    return None

def get_movies_in_genre(genre_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&language=en_US&with_genres={genre_id}&page=1"
    try:
        response = requests.get(url)
        return response.json().get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies: {e}")
    return []

def recommend_movie():
    genre = input("Choose genre: ")
    genre_id = get_genre_id(genre)
    movies = get_movies_in_genre(genre_id)
    if movies:
        movie = random.choice(movies)        
        print(f"Movie title: {movie['title']}")
        print(f"Overview: {movie['overview']}")

recommend_movie()