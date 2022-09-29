import requests


class Neighborhoods:
    """
    NEIGHBORHOODS
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints/NeighborhoodsController_getNeighborhoods
    """

    def __init__(self, base):
        self.__base = base
        self.__base_url = f"{base.base_url}/neighborhoods"

    def get_neighborhoods(
        self,
        cityId: int = 0,
        textSearch: str = "",
    ):
        """
        `List neighborhoods`

        :param cityId: City ID (Optional)
        :type cityId: int
        :param textSearch: Text search on neighborhood name (Optional)
        :type textSearch: str

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}"
        params = {}
        if cityId:
            params["cityId"] = cityId
        if textSearch:
            params["textSearch"] = textSearch

        r = requests.get(url, headers=self.__base.headers, params=params).json()
        return r
