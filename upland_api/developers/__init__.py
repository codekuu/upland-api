from upland_api.developers import resources


class UplandDevelopersAPIBase:

    servers = {
        "production": "https://api.prod.upland.me/developers-api",
        "development": "https://api.sandbox.upland.me/developers-api",
    }

    def __init__(self, api_key: str, server: str = "development"):
        self.base_url = self.servers[server]
        self.api_key = f"Basic {api_key}"
        self.headers = self.get_headers()

    def get_headers(self):
        """
        This function creates a dictionary of headers that will be used in the API call
        :return: A dictionary of headers.
        """
        headers = {
            "Accept-Charset": "application/json",
            "content-type": "application/json",
            "Authorization": self.api_key,
        }
        return headers


# It's a wrapper for the UplandDevelopersAPIBase class that makes it easier to access the resources
class UplandDevelopersAPI:
    def __init__(self, api_key: str, server: str = "development"):
        """
        It creates a class called UplandDevelopersAPI.

        :param api_key: Your API key
        :type api_key: str
        :param server: The server you want to connect to, defaults to development
        :type server: str (optional)
        """
        self.__api_key = api_key
        self.__server = server
        self.__base = UplandDevelopersAPIBase(api_key, server)

        self.user = resources.User(self.__base)
        self.auth = resources.Auth(self.__base)
        self.containers = resources.Containers(self.__base)
        self.tracks = resources.Tracks(self.__base)
        self.buildings = resources.Buildings(self.__base)
        self.cities = resources.Cities(self.__base)
        self.properties = resources.Properties(self.__base)
        self.neighborhoods = resources.Neighborhoods(self.__base)
        self.collections = resources.Collections(self.__base)
        self.treasures_history = resources.TreasuresHistory(self.__base)
