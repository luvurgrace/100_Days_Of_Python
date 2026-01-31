import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movies_webpage = response.text
soup = BeautifulSoup(movies_webpage, "html.parser")

with open("movies.txt", "w", encoding="utf-8") as f:
    movie_names = soup.find_all("h3")
    for movie in movie_names[::-1]:
        n_movie = movie.getText()
        f.write(f"{n_movie}\n")

