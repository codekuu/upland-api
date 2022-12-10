import requests as RealRequests
from ...global_methods import verify_success
from ..models.collections import CollectionsOK


class Collections:
    """
    COLLECTIONS
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints/CollectionsController_getCollections
    """

    def __init__(self, requests: RealRequests, base_path: str):
        self.__requests = requests
        self.__base_path = base_path

    def get_collections(self) -> CollectionsOK:
        """
        `List collections`

        :return: Dict response from Upland Developers API
        """
        r = self.__requests.get(f"{self.__base_path}")
        verify_success(r, 200)

        return r.json()
