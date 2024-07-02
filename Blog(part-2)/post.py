import requests


class Post:
    def __init__(self):
        response = requests.get(url="https://api.npoint.io/0cd445126623dfdd48ba")
        self.blogs = response.json()
