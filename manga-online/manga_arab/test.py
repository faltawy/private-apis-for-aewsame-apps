from typing import List
from fastapi import FastAPI,APIRouter
from manga_arab.exceptions import NoResults
from manga_arab.models import AnimeManga
from manga_arab.getters import search,get_details
DEBUG = True
APP_DESCRIPTION = 'this is api for my spider againest mangaarab app '
MAX_RESULTS = 10
api = FastAPI(debug=DEBUG,description=APP_DESCRIPTION)

@api.get('/search/{search_term}',response_model=List[AnimeManga],description='this route is used to retrieve search results')
async def search_view(search_term:str):
    results = await search(search_term)
    return results[:MAX_RESULTS]


@api.get('/manga_details/{manga_sulg}')
async def manga_detail_view(manga_slug):
    try:
        anime_details = await get_details(manga_slug)
    except NoResults:
        return 'no results found'
    return anime_details
