import requests as RealRequests
from upland_api.global_methods import verify_success
from upland_api.public.models.feature import GetCityOK


class Feature:
    """
    Feature Endpoint
    https://api.upland.me/feature
    """

    def __init__(self, requests: RealRequests, base_path: str):
        self.__requests = requests
        self.__base_path = base_path

    def city(
        self,
    ) -> GetCityOK:
        """
        `Get All Cities and features`

        Get All Cities and features enabled in those cities.

        :return: Dict response from Upland Developers API
        """
        r = self.__requests.get(f"{self.__base_path}/city")
        verify_success(r, 200)

        return r.json()
