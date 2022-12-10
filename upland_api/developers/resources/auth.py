import requests as RealRequests
from dataclasses import dataclass
from upland_api.global_methods import verify_success
from upland_api.developers.models.auth import CreatedConnectionCodeCreated


@dataclass
class Auth:
    """
    TREASURES HISTORY
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints/TreasuresController_getTreasuresHistory
    """

    def __init__(self, requests: RealRequests, base_path: str):
        self.__requests = requests
        self.__base_path = base_path

    def create_connection_code(
        self,
    ) -> CreatedConnectionCodeCreated:
        """
        `Create Connection Code`

        Create a connection code to authenticate Upland Users on Third Party App.

        Upland User must add this code to your Upland Account to grant access.

        :return: Dict response from Upland Developers API
        """
        r = self.__requests.post(f"{self.__base_path}/otp/init")
        verify_success(r, 201)

        return r.json()
