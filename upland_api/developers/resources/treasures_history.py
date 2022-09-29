import requests


class TreasuresHistory:
    """
    TREASURES HISTORY
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints/TreasuresController_getTreasuresHistory
    """

    def __init__(self, base):
        self.__base = base
        self.__base_url = f"{base.base_url}/treasures-history"

    def get_properties(
        self,
        cityId: int,
        currentPage: int = 0,
        pageSize: int = 10,
    ):
        """
        `List available properties given a city id`

        :param currentPage: int = 0, defaults to 0
        :type currentPage: int (optional)
        :param pageSize: The number of results to return per call, defaults to 10
        :type pageSize: int (optional)
        :param cityId: City ID
        :type cityId: int

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}"
        params = {"currentPage": currentPage, "pageSize": pageSize, "cityId": cityId}
        r = requests.get(url, headers=self.__base.headers, params=params).json()
        return r
