# responsible for the requests
from aiohttp import ClientSession,ClientResponse
from manga_arab.main import MangaArabApi
from typing import List
from manga_arab.models import (
    AnimeManga,
    Category,
    Chapter,
    Status)
from manga_arab.exceptions import (ConnectionError,NoResults)


async def get(*args, **kwargs)->ClientResponse:
    async with ClientSession() as session:
        response = await session.get(*args, **kwargs)
    if not response.ok:
        raise ConnectionError
    else:
        return response



# methods [search,get-details,read-chapter]
mangapi = MangaArabApi

async def search(search_term:str) -> List[AnimeManga]:
    querystring = {"name":str(search_term.LOWER()),"API_key":mangapi.API_key}
    async with ClientSession() as session:
        response = await session.get(mangapi.get_endpoint('search'),params=querystring)
        if not response.ok:
            raise ConnectionError
        else:
            resp_data = await response.json()
            if len(resp_data['data']) == 0:
                raise NoResults(search_term)
            else:
                results = [AnimeManga(**d) for d in resp_data['data']]
                
                return results





async def get_details(anime_slug)->AnimeManga:
    url = mangapi.get_endpoint('manga-info')%(anime_slug)
    querystring = {"API_key":mangapi.API_key}
    response = await get(url,params=querystring)
    __details = await response.json()
    try:
        details  = __details['data']['infoManga'][0]
        return AnimeManga(**details)
    except:
        raise NoResults(anime_slug)


async def read_chapter(anime_slug:str,chapter:int):
    querystring = {"API_key":mangapi.API_key}
    url = mangapi.get_endpoint('read-chapter')%(anime_slug,str(chapter))
    try:
        response = await get(url,params=querystring)
    except:
        NoResults(anime_slug + str(chapter))
    chapter_data =await response.json()
    return chapter_data.get('pages_url')

