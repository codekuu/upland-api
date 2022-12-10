import requests as RealRequests
from upland_api.global_methods import verify_success
from upland_api.developers.models.buildings import BuildingsOK


class Buildings:
    """
    BUILDINGS
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints
    """

    def __init__(self, requests: RealRequests, base_path: str):
        self.__requests = requests
        self.__base_path = base_path

    def get_buildings(self, boundaries: list) -> BuildingsOK:
        """
        `Retrieve buildings given some boundaries`

        Each boundary contains a list of coordinates as the example below.

        :param boundaries: List of boundaries
        :type boundaries: list

        :return: Dict response from Upland Developers API
        """
        r = self.__requests.post(
            f"{self.__base_path}",
            data={"boundaries": boundaries},
        )
        verify_success(r, 200)

        return r.json()
