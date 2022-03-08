import requests

headers = {
    'Client-Id': 'android-app2',
    'Client-Secret': '7befba6263cc14c90d2f1d6da2c5cf9b251bfbbd',
    'Accept': 'application/*+json',
    'Connection': 'Keep-Alive',
    'User-Agent': 'okhttp/3.12.12',
}


anime_data = {'anime_id': '3322', 'anime_name': 'benriya saitou-san isekai ni iku', 'anime_type': 'TV', 'anime_status': 'Not Yet Aired', 'just_info': 'No', 'anime_season': '', 'anime_release_year': None, 'anime_rating': None, 'anime_genres': 'مغامرات, كوميديا, خيال', 'anime_cover_image_url': 'https://img.anslayer.com/anime/anime/cover-image/anime-cover-8d76eb2d29634729f01e2e0601dc6a64.png', 'anime_trailer_url': '', 'anime_release_day': ''}
class SearchResult:
    def __init__(self,metadata:dict,id,name,type,status,anime_release_day,anime_genres,anime_cover_image_url,anime_trailer_url):
        self.meta_data = metadata



def search(query:str,max_results=20,order_by='latest_first')->dict:
    params = (('json', '{"_offset":0,"_limit":%s,"_order_by":"%s","list_type":"filter","%s":"attack","just_info":"Yes"}'%(str(max_results),order_by,query)),)
    search_url = 'https://anslayer.com/anime/public/animes/get-published-animes'
    data = requests.get(search_url, headers=headers, params=params).json()
    return data

print(search('death note'))

