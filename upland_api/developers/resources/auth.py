import requests


class Auth:
    """
    TREASURES HISTORY
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints/TreasuresController_getTreasuresHistory
    """

    def __init__(self, base):
        self.__base = base
        self.__base_url = f"{base.base_url}/auth"

    def create_connection_code(
        self,
    ):
        """
        `Create Connection Code`

        Create a connection code to authenticate Upland Users on Third Party App.

        Upland User must add this code to your Upland Account to grant access.

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}/otp/init"
        r = requests.post(url, headers=self.__base.headers).json()
        return r
