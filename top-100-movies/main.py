import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, 'html.parser')
movie_data = [name.getText() for name in soup.find_all(name="h3", class_="title")]
movie_names = [name.split(' ', 1)[1] for name in movie_data ]
movie_rankings = [name.split(' ', 1)[0].rstrip(')') for name in movie_data]
movie_names.reverse()
movie_rankings.reverse()

movies = [f"{rank}. {name}" for rank, name in zip(movie_rankings, movie_names)]
try:
    with open("movies.txt", "x") as file:
        for item in movies:
            file.write(str(item) + "\n")
except FileExistsError:
    print("File already exists.")