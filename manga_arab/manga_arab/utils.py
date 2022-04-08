from pydantic import BaseConfig

class MangaArabApi(BaseConfig):
    API_VERSION:str = 'v4/'
    __BASE_URL:str = 'https://onma.me/api/'
    BASE_URL:str = __BASE_URL + API_VERSION
    ENDPOINTS:dict = {
        'search':__BASE_URL + 'v3/advanced-search',
        'manga-info':__BASE_URL + "v3/manga-info/%s",
        'read-chapter':__BASE_URL +"v3/read-chapter/%s/%s",
    }
    GOOGLE_API_KEY:str = "AIzaSyAVFmo_CQ99SJ1OrvlQwxM_tP6uuCnECNg"
    API_key:str="23r1rdrYtOP0Ghgetyt6fc2"
    
    HEADERS:dict = {"x-goog-api-key":GOOGLE_API_KEY}
    @classmethod
    def get_endpoint(cls,endpoint:str)->str:
        return cls.ENDPOINTS.get(endpoint)