class MangaArabApi():
    API_VERSION = 'v4/'
    __BASE_URL = 'https://onma.me/api/'
    BASE_URL = __BASE_URL + API_VERSION
    ENDPOINTS = {
        'search':__BASE_URL + 'v3/advanced-search',
        'manga-info':__BASE_URL + "v3/manga-info/%s",
        'read-chapter':__BASE_URL +"v3/read-chapter/%s/%s",
    }
    GOOGLE_API_KEY = "AIzaSyAVFmo_CQ99SJ1OrvlQwxM_tP6uuCnECNg"
    API_key="23r1rdrYtOP0Ghgetyt6fc2"
    
    HEADERS = {"x-goog-api-key":GOOGLE_API_KEY}
    API_key = '23r1rdrYtOP0Ghgetyt6fc2'
    
    @classmethod
    def get_endpoint(cls,endpoint:str):
        return cls.ENDPOINTS.get(endpoint)

    

