from requests import post

class Client:
    def __init__(self) -> None:
        self.__headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Android-Package': 'zxc.laitooo.onmanga',
            'x-firebase-client': 'fire-analytics/17.5.0 fire-installations/16.3.3 fire-fcm/20.2.4 kotlin/1.2.60 fire-android/ fire-rtdb/19.3.1 fire-iid/20.2.3 fire-cls/17.2.1 fire-core/19.3.1',
            'x-firebase-client-log-type': '3',
            'X-Android-Cert': '5D08264B44E0E53FBCCC70B4F016474CC6C5AB5C',
            'x-goog-api-key': 'AIzaSyAVFmo_CQ99SJ1OrvlQwxM_tP6uuCnECNg'}
        self.__data = '{"fid":"duL_3EQeQu6cThDqIS8Vm_","appId":"1:322049583859:android:aa76174b6eceead48fe586","authVersion":"FIS_v2","sdkVersion":"a:16.3.3"}'
        self.__data = self.__token()

    def __token(self) ->str:
        data = post('https://firebaseinstallations.googleapis.com/v1/projects/manga-online-8f4c1/installations', headers=self.__headers, data=self.__data)
        return data.json()

    @property
    def token(self):
        return self.__data.get('authToken').get('token')
    
    @property
    def full_data(self):
        return self.__data
