import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = URL + date
response = requests.get(url=url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

