from typing import List
from fastapi import FastAPI
from manga_arab.exceptions import NoResults
from manga_arab.models import AnimeManga
from manga_arab.getters import Getter

DEBUG = True
APP_DESCRIPTION = 'this is api for my spider againest mangaarab app '
MAX_RESULTS = 10
api = FastAPI(debug=DEBUG,description=APP_DESCRIPTION)

getter = Getter()
@api.get('/search/{search_term}',response_model=List[AnimeManga],description='this route is used to retrieve search results')
async def search_view(search_term:str):
    getter = Getter()
    results = await getter.search(search_term)
    return results[:MAX_RESULTS]


@api.get('/manga_details/{manga_sulg}')
async def manga_detail_view(manga_slug):
    getter = Getter()
    try:
        anime_details = await getter.get_details(manga_slug)
        print(anime_details)
    except NoResults:
        return 'no results found'
    return anime_details

@api.get('/get-chapters/{anime_slug}/{chapter_id}')
async def get_chapters(anime_slug:str,chapter_id:int):
    getter = Getter()
    data = await getter.read_chapter(anime_slug,chapter_id)
    print(data)
    return data
