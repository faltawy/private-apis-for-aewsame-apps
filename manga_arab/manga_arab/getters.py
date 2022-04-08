from aiohttp import ClientResponse, ClientSession
from manga_arab.utils import MangaArabApi
from typing import List
from manga_arab.models import AnimeManga
from manga_arab.exceptions import (ConnectionError,NoResults)
import asyncio


mangapi = MangaArabApi
class Getter:
    def __init__(self) -> None:
        self.session = ClientSession()
    
    async def get(self,*args, **kwargs)->ClientResponse:
        async with self.session.get(*args, **kwargs) as resp:
            assert resp.ok
            return resp
    
    async def search(self,search_term:str) ->List[AnimeManga]:
        querystring = {"name":str(search_term).lower(),"API_key":mangapi.API_key}
        async with self.session as session:
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
    
    async def get_details(self,anime_slug:str)->AnimeManga:
        url = mangapi.get_endpoint('manga-info')%(anime_slug)
        querystring = {"API_key":mangapi.API_key}
        response = await self.get(url,params=querystring)
        _details = await response.json()
        try:
            __details  = await _details.get('data')
            details = await __details.get('infoManga')[0]
            return AnimeManga(**details)
        except Exception as e:
            print(e)
            raise NoResults(anime_slug)




    async def read_chapter(self,anime_slug:str,chapter:int):
        querystring = {"API_key":mangapi.API_key}
        url = mangapi.get_endpoint('read-chapter')%(anime_slug,str(chapter))
        try:
            response = await self.get(url,params=querystring)
            chapter_data =await response.json()
            return chapter_data.get('pages_url')
        except:
            NoResults(anime_slug + str(chapter))




# async def search(search_term:str) -> List[AnimeManga]:
#     querystring = {"name":str(search_term).lower(),"API_key":mangapi.API_key}
#     async with ClientSession() as session:
#         response = await session.get(mangapi.get_endpoint('search'),params=querystring)
#         if not response.ok:
#             raise ConnectionError
#         else:
#             resp_data = await response.json()
#             if len(resp_data['data']) == 0:
#                 raise NoResults(search_term)
#             else:
#                 results = [AnimeManga(**d) for d in resp_data['data']]
                
#                 return results


# async def get_details(anime_slug)-> AnimeManga:
#     url = mangapi.get_endpoint('manga-info')%(anime_slug)
#     querystring = {"API_key":mangapi.API_key}
#     response = await get(url,params=querystring)
#     _details = await response.json()
#     try:
#         __details  = await _details.get('data')
#         details = await __details.get('infoManga')[0]
#         return AnimeManga(**details)
#     except:
#         raise NoResults(anime_slug)


# async def read_chapter(anime_slug:str,chapter:int):
#     querystring = {"API_key":mangapi.API_key}
#     url = mangapi.get_endpoint('read-chapter')%(anime_slug,str(chapter))
#     try:
#         response = await get(url,params=querystring)
#     except:
#         NoResults(anime_slug + str(chapter))
#     chapter_data =await response.json()
#     return chapter_data.get('pages_url')
