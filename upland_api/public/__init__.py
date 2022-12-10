from requests import Session
from urllib.parse import urljoin
from upland_api.public import resources


class UplandPublicAPIRequests(Session):
    def __init__(self, base_url=None, headers={}, logging=False, *args, **kwargs):
        super(UplandPublicAPIRequests, self).__init__(*args, **kwargs)
        self.base_url = base_url
        self.headers = headers
        self.logging = logging

    def request(
        self,
        method,
        url,
        headers={},
        params={},
        data={},
        json={},
        allow_redirects=False,
    ):
        url = urljoin(self.base_url, url)
        if headers:
            self.headers = {**self.headers, **headers}
        if self.logging:
            print(f"{method} request made towards {url}")
        kwargs = {}
        if params:
            kwargs["params"] = params
        if data:
            kwargs["data"] = data
        if json:
            kwargs["json"] = json

        return super(UplandPublicAPIRequests, self).request(
            method, url, headers=self.headers, allow_redirects=allow_redirects, **kwargs
        )


class UplandPublicAPI:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.upland.me/",
        logging: bool = False,
    ):
        self.__api_key = api_key
        self.__base_url = base_url
        self.__logging = logging

        # Set up the base requests Session
        self.__base = UplandPublicAPIRequests(
            base_url=self.__base_url,
            headers=self.__get_headers(),
            logging=self.__logging,
        )

        # Init the endpoints with the base
        self.feature = resources.Feature(requests=self.__base, base_path="/feature")
        self.settings = resources.Settings(requests=self.__base, base_path="/settings")

    def __get_headers(self):
        """
        This function creates a dictionary of headers that will be used in the API call
        :return: A dictionary of headers.
        """
        headers = {
            "Accept-Charset": "application/json",
            "Authorization": f"Basic {self.__api_key}",
        }
        return headers
