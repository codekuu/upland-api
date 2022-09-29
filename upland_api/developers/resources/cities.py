import requests


class Cities:
    """
    CITIES
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints/CitiesController_getCities
    """

    def __init__(self, base):
        self.__base = base
        self.__base_url = f"{base.base_url}/cities"

    def get_cities(self):
        """
        `List availables cities`

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}"

        r = requests.post(url, headers=self.__base.headers).json()
        return r
