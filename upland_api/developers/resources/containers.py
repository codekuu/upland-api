import requests


class Containers:
    """
    CONTAINERS
    https://api.sandbox.upland.me/developers-api/docs/#/Escrow%20Container%20Management
    """

    def __init__(self, base):
        self.__base = base
        self.__base_url = f"{base.base_url}/containers"

    def lock(self, containerId: int):
        """
        `Locks the escrow container (Optional)`
        This action will lock the container. After this action users can not join this container. This doesn't apply to all 3p apps. It's an optional call if a third party wants to make sure that no one else will enter the container.

        :param containerId: The ID of the container
        :type containerId: int
        :return: Status Code
        """
        url = f"{self.__base_url}/{containerId}/lock"
        r = requests.post(url, headers=self.__base.headers)
        return r.status_code

    def create_container(
        self,
    ):
        """
        `Create a new container`

        The third-party application will be able to create a new container in the escrow to receive user assets.
        The container times out after the lesser of the developer's desired container time to live.
        The webhook URL will be used by the escrow service to communicate with third-party apps about the transaction status in the container.

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}"
        r = requests.post(url, headers=self.__base.headers).json()
        return r

    def refresh_container(self, containerId: int):
        """
        `Refresh Expiration time of Escrow Container`

        Refresh the container expiration for the same amount of time previously informed.

        :param containerId: The ID of the container
        :type containerId: int
        :return: Status Code
        """
        url = f"{self.__base_url}/{containerId}/refresh-expiration-time"
        r = requests.post(url, headers=self.__base.headers)
        return r.status_code

    def get_container(self, containerId: int):
        """
        `Query Escrow Container`

        Retrieve container information by id, including expiration time. The possible values for the container status are created, locked, processing, resolved, and expired.

        :param containerId: The ID of the container
        :type containerId: int
        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}/{containerId}"
        r = requests.get(url, headers=self.__base.headers).json()
        return r

    def resolve_container(self, containerId: int, actions: list):
        """
        `Execute operations over the escrow assets and resolve container`

        Send some operations in batch to be executed over the escrow assets and UPXs.
        This call is the final resolution. At this moment Escrow Service will execute transactions and close the container. If there are assets remaining, they will return to the account source.

        :param containerId: The ID of the container you want to join
        :type containerId: int
        :param actions: list of assets
        :type actions: list

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}/{containerId}/resolve"
        data = {"actions": actions}
        r = requests.post(url, headers=self.__base.headers, data=data).json()
        return r

    def refund_container(self, containerId: int):
        """
        `Refund container assets`

        It sends back the assets inside the container to the original owners (no fees) and resolves the container.

        :param containerId: The ID of the container you want to join
        :type containerId: int

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}/{containerId}/refund"
        r = requests.post(url, headers=self.__base.headers).json()
        return r

    def delete_transaction(self, containerId: int, transactionId: str):
        """
        `Remove a transaction from container`

        Removes a transaction that has not been signed by the user from container.

        :param containerId: The ID of the container you want to join
        :type containerId: int

        :return: Status Code
        """
        url = f"{self.__base_url}/{containerId}/transactions/{transactionId}"
        r = requests.delete(url, headers=self.__base.headers)
        return r.status_code
