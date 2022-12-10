import requests as RealRequests
from upland_api.global_methods import verify_success
from upland_api.developers.models.cities import CitiesOK


class Cities:
    """
    CITIES
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints/CitiesController_getCities
    """

    def __init__(self, requests: RealRequests, base_path: str):
        self.__requests = requests
        self.__base_path = base_path

    def get_cities(self) -> CitiesOK:
        """
        `List availables cities`

        :return: Dict response from Upland Developers API
        """
        r = self.__requests.get(f"{self.__base_path}/developers-api/cities")
        verify_success(r, 200)

        return r.json()
