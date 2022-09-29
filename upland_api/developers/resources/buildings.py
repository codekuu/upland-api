import requests


class Buildings:
    """
    BUILDINGS
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints
    """

    def __init__(self, base):
        self.__base = base
        self.__base_url = f"{base.base_url}/buildings"

    def get_buildings(self, boundaries: list):
        """
        `Retrieve buildings given some boundaries`

        Each boundary contains a list of coordinates as the example below.

        :param boundaries: List of boundaries
        :type boundaries: list

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}"
        data = {"boundaries": boundaries}

        r = requests.post(url, headers=self.__base.headers, data=data).json()
        return r
