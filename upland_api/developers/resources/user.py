import requests


class User:
    """
    USER
    https://api.sandbox.upland.me/developers-api/docs/#/Upland%20User%20Information
    """

    def __init__(self, base):
        self.__base = base
        self.__base_url = f"{base.base_url}/user"

    def profile(self):
        """
        `Retrieve user profile information`

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}/profile"
        r = requests.get(url, headers=self.__base.headers).json()
        return r

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
    ):
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
        url = f"{self.__base_url}/assets/nfts"
        params = {
            "currentPage": currentPage,
            "pageSize": pageSize,
            "categories": categories,
        }
        r = requests.get(url, headers=self.__base.headers, params=params).json()
        return r

    def assets_properties(
        self,
        currentPage: int = 0,
        pageSize: int = 10,
    ):
        """
        `Get List of User's properties`

        :param currentPage: int = 0, defaults to 0
        :type currentPage: int (optional)
        :param pageSize: The number of results to return per call, defaults to 10
        :type pageSize: int (optional)

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}/assets/properties"
        params = {
            "currentPage": currentPage,
            "pageSize": pageSize,
        }
        r = requests.get(url, headers=self.__base.headers, params=params).json()
        return r

    def balances(self):
        """
        `Retrieve user balances as UPX and SPARK`

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}/user/balances"
        r = requests.get(url, headers=self.__base.headers).json()
        return r

    def join(self, containerId: int, upxAmount: int, sparkAmount: int, assets: list):
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
        url = f"{self.__base_url}/XXXXXXXXXXXXXX"
        data = {
            "containerId": containerId,
            "upxAmount": upxAmount,
            "sparkAmount": sparkAmount,
            "assets": assets,
        }
        r = requests.post(url, headers=self.__base.headers, data=data).json()
        return r

    def travels(
        self,
        currentPage: int = 0,
        pageSize: int = 10,
    ):
        """
        `Get List of User travels`

        :param currentPage: int = 0, defaults to 0
        :type currentPage: int (optional)
        :param pageSize: The number of results to return per call, defaults to 10
        :type pageSize: int (optional)

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}/XXXXXXXXXXXXXX"
        params = {
            "currentPage": currentPage,
            "pageSize": pageSize,
        }
        r = requests.get(url, headers=self.__base.headers, params=params).json()
        return r
