import requests
import random

API_KEY = "your_api_key_here" 
BASE_URL = "https://api.themoviedb.org/3"

def get_genre_id(genre_name):
    """Fetch genre ID from TMDB based on user input."""
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json().get("genres", [])
        for genre in genres:
            if genre["name"].lower() == genre_name.lower():
                return genre["id"]
    return None

def get_movies_by_genre(genre_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []

def recommend_movie():
    genre_name = input("Enter a movie genre (e.g., Action, Comedy, Drama): ").strip()
    genre_id = get_genre_id(genre_name)

    if genre_id:
        movies = get_movies_by_genre(genre_id)
        if movies:
            movie = random.choice(movies)
            print("\n🎬 Movie Recommendation:")
            print(f"Title: {movie['title']}")
            print(f"Overview: {movie['overview']}")
            print(f"Rating: {movie['vote_average']} ⭐")
        else:
            print("No movies found for this genre.")
    else:
        print("Invalid genre name. Please try again.")

recommend_movie()
