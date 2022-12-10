import requests as RealRequests
from upland_api.global_methods import verify_success
from upland_api.developers.models.neighborhoods import GetNeighborhoodsOK


class Neighborhoods:
    """
    NEIGHBORHOODS
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints/NeighborhoodsController_getNeighborhoods
    """

    def __init__(self, requests: RealRequests, base_path: str):
        self.__requests = requests
        self.__base_path = base_path

    def get_neighborhoods(
        self,
        cityId: int = 0,
        textSearch: str = "",
    ) -> GetNeighborhoodsOK:
        """
        `List neighborhoods`

        :param cityId: City ID (Optional)
        :type cityId: int
        :param textSearch: Text search on neighborhood name (Optional)
        :type textSearch: str

        :return: Dict response from Upland Developers API
        """
        params = {}
        if cityId:
            params["cityId"] = cityId
        if textSearch:
            params["textSearch"] = textSearch
        print(params)
        r = self.__requests.get(f"{self.__base_path}", params=params)
        verify_success(r, 200)

        return r.json()
