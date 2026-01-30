import requests

from configuration.ConfigProvider import ConfigProvider

class SearchApi:
    def __init__(self, base_url: str) -> None:
        base_url = ConfigProvider().get("api", "base_url")
        self.base_url = base_url

    def get(self, path: str, params=None) -> requests.Response:
        url = f"{self.base_url}{path}"
        resp = requests.get(url, params=params)
        return resp
    
    def delete(self, path, params=None) -> requests.Response:
        url = f"{self.base_url}{path}"
        return requests.delete(url, params=params)



        

       

        

        
       
        #put_into_cart
        #go_to_cart
        # возможно, проверить размер текста в каких-то карточках/блоках, или размер иконок

