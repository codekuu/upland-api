import requests as RealRequests
from upland_api.global_methods import verify_success
from upland_api.public.models.settings import GetConfigOK, GetMaintenanceOK


class Settings:
    """
    Settings Endpoint
    https://api.upland.me/settings
    """

    def __init__(self, requests: RealRequests, base_path: str):
        self.__requests = requests
        self.__base_path = base_path

    def maintenance(
        self,
    ) -> GetMaintenanceOK:
        """
        `Get Maintenance status of Upland`

        :return: Dict response from Upland Developers API
        """
        r = self.__requests.get(f"{self.__base_path}/maintenance")
        verify_success(r, 200)

        return r.json()

    def config(
        self,
    ) -> GetConfigOK:
        """
        `Get Config of Upland`

        :return: Dict response from Upland Developers API
        """
        r = self.__requests.get(f"{self.__base_path}/config")
        verify_success(r, 200)

        return r.json()
