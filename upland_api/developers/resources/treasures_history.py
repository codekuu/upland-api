import requests as RealRequests
from upland_api.global_methods import verify_success
from upland_api.developers.models.treasures_history import GetTreasuresHistoryOK


class TreasuresHistory:
    """
    TREASURES HISTORY
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints/TreasuresController_getTreasuresHistory
    """

    def __init__(self, requests: RealRequests, base_path: str):
        self.__requests = requests
        self.__base_path = base_path

    def get_properties(
        self,
        cityId: int,
        currentPage: int = 0,
        pageSize: int = 10,
    ) -> GetTreasuresHistoryOK:
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
        params = {"currentPage": currentPage, "pageSize": pageSize, "cityId": cityId}
        r = self.__requests.get(f"{self.__base_path}", params=params)
        verify_success(r, 200)

        return r.json()
