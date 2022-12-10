from requests import Session
from urllib.parse import urljoin
from upland_api.developers import resources


class UplandDevelopersAPIRequests(Session):
    def __init__(self, base_url=None, headers={}, logging=False, *args, **kwargs):
        super(UplandDevelopersAPIRequests, self).__init__(*args, **kwargs)
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

        return super(UplandDevelopersAPIRequests, self).request(
            method, url, headers=self.headers, allow_redirects=allow_redirects, **kwargs
        )


class UplandDevelopersAPI:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.sandbox.upland.me",
        logging: bool = False,
    ):
        self.__api_key = api_key
        self.__base_url = base_url
        self.__logging = logging

        # Set up the base requests Session
        self.__base = UplandDevelopersAPIRequests(
            base_url=self.__base_url,
            headers=self.__get_headers(),
            logging=self.__logging,
        )

        # Init the endpoints with the base
        self.auth = resources.Auth(
            requests=self.__base, base_path="/developers-api/auth"
        )
        self.buildings = resources.Buildings(
            self.__base, base_path="/developers-api/buildings"
        )
        self.cities = resources.Cities(
            self.__base, base_path="/developers-api/buildings"
        )
        self.collections = resources.Collections(
            self.__base, base_path="/developers-api/collections"
        )
        self.containers = resources.Containers(
            self.__base, base_path="/developers-api/containers"
        )
        self.neighborhoods = resources.Neighborhoods(
            self.__base, base_path="/developers-api/neighborhoods"
        )
        self.properties = resources.Properties(
            self.__base, base_path="/developers-api/properties"
        )
        self.tracks = resources.Tracks(self.__base, base_path="/developers-api/tracks")
        self.treasures_history = resources.TreasuresHistory(
            self.__base, base_path="/developers-api/treasures-history"
        )
        self.user = resources.User(self.__base, base_path="/developers-api/user")

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
