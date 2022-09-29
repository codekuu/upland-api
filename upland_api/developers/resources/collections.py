import requests


class Collections:
    """
    COLLECTIONS
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints/CollectionsController_getCollections
    """

    def __init__(self, base):
        self.__base = base
        self.__base_url = f"{base.base_url}/collections"

    def get_collections(self):
        """
        `List collections`

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}"

        r = requests.get(url, headers=self.__base.headers).json()
        return r
