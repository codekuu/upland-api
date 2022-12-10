import requests as RealRequests
from ...global_methods import verify_success
from ..models.user import (
    GetProfileOK,
    GetAssetNftsOK,
    GetAssetsPropertiesOK,
    GetBalacesOK,
    PostJoinOK,
)


class User:
    """
    USER
    https://api.sandbox.upland.me/developers-api/docs/#/Upland%20User%20Information
    """

    def __init__(self, requests: RealRequests, base_path: str):
        self.__requests = requests
        self.__base_path = base_path

    def profile(self) -> GetProfileOK:
        """
        `Retrieve user profile information`

        :return: Dict response from Upland Developers API
        """
        r = self.__requests.get(f"{self.__base_path}/profile")
        verify_success(r, 200)

        return r.json()

    def assets_nfts(
        self,
        currentPage: int = 0,
        pageSize: int = 10,
        categories: list = [
            "blkexplorer",
            "essential",
            "landvehicle",
            "memento",
            "outdoordecor",
            "spirithlwn",
            "structure",
            "structornmt",
        ],
    ) -> GetAssetNftsOK:
        """
        `Get List of User's NFTs given a category`
        Available Categories (blkexplorer, essential, landvehicle, memento, outdoordecor, spirithlwn, structure, structornmt)

        :param currentPage: int = 0, defaults to 0
        :type currentPage: int (optional)
        :param pageSize: The number of results to return per call, defaults to 10
        :type pageSize: int (optional)
        :param categories: list = ["string"], defaults to ALL
        :type categories: list

        :return: Dict response from Upland Developers API
        """
        params = {
            "currentPage": currentPage,
            "pageSize": pageSize,
            "categories": categories,
        }
        r = self.__requests.get(f"{self.__base_path}/assets/nfts", params=params)
        verify_success(r, 200)

        return r.json()

    def assets_properties(
        self,
        currentPage: int = 0,
        pageSize: int = 10,
    ) -> GetAssetsPropertiesOK:
        """
        `Get List of User's properties`

        :param currentPage: int = 0, defaults to 0
        :type currentPage: int (optional)
        :param pageSize: The number of results to return per call, defaults to 10
        :type pageSize: int (optional)

        :return: Dict response from Upland Developers API
        """
        params = {
            "currentPage": currentPage,
            "pageSize": pageSize,
        }
        r = self.__requests.get(f"{self.__base_path}/assets/properties", params=params)
        verify_success(r, 200)

        return r.json()

    def balances(self) -> GetBalacesOK:
        """
        `Retrieve user balances as UPX and SPARK`

        :return: Dict response from Upland Developers API
        """
        r = self.__requests.get(f"{self.__base_path}/balances")
        verify_success(r, 200)

        return r.json()

    def join(
        self, containerId: int, upxAmount: int, sparkAmount: int, assets: list
    ) -> PostJoinOK:
        """
        `Put assets in escrow container`

        Send a list of user assets that will be added to the escrow container. This action must be approved by Upland User inside the Upland Application to be performed.

        :param containerId: The ID of the container you want to join
        :type containerId: int
        :param upxAmount: The amount of UPX
        :type upxAmount: int
        :param sparkAmount: The amount of spark
        :type sparkAmount: int
        :param assets: list of assets to be used in the container
        :type assets: list

        :return: Dict response from Upland Developers API
        """
        data = {
            "containerId": containerId,
            "upxAmount": upxAmount,
            "sparkAmount": sparkAmount,
            "assets": assets,
        }
        r = self.__requests.get(f"{self.__base_path}/join", data=data)
        verify_success(r, 200)

        return r.json()
