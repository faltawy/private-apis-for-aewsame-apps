from requests import session

# dict_keys(['eId', 'AnimeID', 'Episode', 'ExtraEpisodes', 'MSLink', 'SVLink', 'OKLink', 'MALink', 'GDLink', 'FRLink', 'SFLink', 'MSLowQ', 'SVLowQ', 'FRLowQ', 'GDFhdQ', 'FRFhdQ', 'GULink', 'GULowQ', 'FDLink', 'LULink', 'LULowQ', 'IsOva', 'IsSpecial', 'IsFlr', 'IsLast', 'ViewStatus'])



class Episode(object):
    def __init__(self,epi_id:str,anime_id:str,index:int) -> None:
        pass
        
class Anime:
    def __init__(self) -> None:
        
        pass

    # def download



class SearchResult(Anime):
    # def __init__(self,MainId, Title, SubTitle, Tags, Season, RuntimeHours, RuntimeMinutes, AringDate, Thumbnail, Trailer, YTTrailer, Creator, Status, EpisodesCount, IsONA, IsOva, IsSpecial, IsCartoon, Score, Rank, Popularity, AgeRate,RelationId, JicanKey, Genres, Plot, IsFavourite, InLibrary) -> None:
    #     pass

    def __init__(self,data:dict) -> None:
        self.__data_json = data
        self._session = session()
        for key in data.keys():
            setattr(self, f'_{key.lower()}', data[key])

    @property
    def season(self):
        return int(self._season)
    
    @property
    def epis_count(self):
        return int(self._episodescount)
    # IsONA, IsOva, IsSpecial, IsCartoon
    @property
    def is_ova(self):
        return bool(int(self._isova))

    @property
    def is_cartoon(self):
        return bool(int(self._iscartoon))

    @property
    def is_special(self):
        return bool(int(self._is_special))

    @property
    def is_ona(self):
        return bool(int(self._is_ona))


    def __str__(self):
        return self._title

    def __repr__(self) -> str:
        return self._title
    
    @property
    def data_json(self):
        return self.__data_json   


    def fetch_details(self):
        'fetch anime details from jikan api'
        jikan_id = self._jicankey
        jikan_api = f'https://api.jikan.moe/v3/anime/{jikan_id}'
        return self._session.get(jikan_api).json()

    
    def fetch_episodes(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded',}
        data = {'AnimeID': self._mainid}
        response = self._session.post('https://animeify.net/animeify/apis_v2/episodes/episodes_loader.php', headers=headers, data=data)
        # response for each episode
        # {'eId': '6688', 'AnimeID': 'xDeathNote', 'Episode': '1', 'ExtraEpisodes': '', 'MSLink': 'zy8xqglcdccy', 'SVLink': '', 'OKLink': '1620561955463', 'MALink': 'jS4XUCxB!Dz3U_Ak9RzPTyNMuaKREUAp24QHl_u_Oq-xsO63DQgI', 'GDLink': '1eQbqQvBknpF6rMcJLAf2fagz-UOfiH48', 'FRLink': 'azgygkm5vpz5j3t', 'SFLink': '', 'MSLowQ': 'rc7itibz03so', 'SVLowQ': '', 'FRLowQ': '', 'GDFhdQ': '', 'FRFhdQ': '', 'GULink': '', 'GULowQ': '', 'FDLink': '', 'LULink': '', 'LULowQ': '', 'IsOva': '', 'IsSpecial': '', 'IsFlr': '', 'IsLast': '', 'ViewStatus': 'N/A'}

        # keys
        # dict_keys(['eId', 'AnimeID', 'Episode', 'ExtraEpisodes', 'MSLink', 'SVLink', 'OKLink', 'MALink', 'GDLink', 'FRLink', 'SFLink', 'MSLowQ', 'SVLowQ', 'FRLowQ', 'GDFhdQ', 'FRFhdQ', 'GULink', 'GULowQ', 'FDLink', 'LULink', 'LULowQ', 'IsOva', 'IsSpecial', 'IsFlr', 'IsLast', 'ViewStatus'])
        return response

# https://www.ok.ru/videoembed/{OKLink}
# https://drive.google.com/file/d/{GDLINK}
# https://www.mediafire.com/file/{FRLink}
# https://www.solidfiles.com/e/{SFLink}
# OKLink seems to be blocked in EGypt
# https://ok.ru/videoembed/{OKLink}


class AnimeFy():
    # base Class For the app 
    def __init__(self) -> None:
        self.__session = session()
        self.__search_headers= {'Content-Type': 'application/x-www-form-urlencoded',}


    def search(self,query:str):
        data = {
        'UserID': '0',
        'Language': 'AR',
        'Text': query}
        url = 'https://animeify.net/animeify/apis_v2/anime/filtersort/search.php'
        response = self.__session.post(url, headers=self.__search_headers, data=data)
        
        if response.ok:
            results = []
            for result in response.json():
                search_res = SearchResult(result)
                results.append(search_res)
            return results
        
        return 'error'

    

    

animeify = AnimeFy()
death = animeify.search('death note')


