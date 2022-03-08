import requests

from client import Client

class Chapter:
    def __init__(self) -> None:
        pass

class Page:
    def __init__(self) -> None:
        pass

class SearchResult:
    pass


class Manga:
    def __init__(self,token:str) -> None:
        self.__token = token

    def search(self,query):
        params = (('name', 'a'),('API_key', self.__token),)
        response = requests.get('https://onma.me/api/v3/advanced-search',params=params)

        print(response.content)

client = Client()
m = Manga(client.token)
m.search('a')