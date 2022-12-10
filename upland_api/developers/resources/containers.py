import requests as RealRequests
from upland_api.global_methods import verify_success
from upland_api.developers.models.containers import (
    ResolveContainerPayloadActions,
    CreateContainerOK,
    GetContainerOK,
    ResolveRefundContainerOK,
)


class Containers:
    """
    CONTAINERS
    https://api.sandbox.upland.me/developers-api/docs/#/Escrow%20Container%20Management
    """

    def __init__(self, requests: RealRequests, base_path: str):
        self.__requests = requests
        self.__base_path = base_path

    def create_container(
        self,
    ) -> CreateContainerOK:
        """
        `Create a new container`

        The third-party application will be able to create a new container in the escrow to receive user assets.
        The container times out after the lesser of the developer's desired container time to live.
        The webhook URL will be used by the escrow service to communicate with third-party apps about the transaction status in the container.

        :return: Dict response from Upland Developers API
        """
        r = self.__requests.get(f"{self.__base_path}")
        verify_success(r, 201)

        return r.json()

    def get_container(self, containerId: int) -> GetContainerOK:
        """
        `Query Escrow Container`

        Retrieve container information by id, including expiration time. The possible values for the container status are created, locked, processing, resolved, and expired.

        :param containerId: The ID of the container
        :type containerId: int
        :return: Dict response from Upland Developers API
        """
        r = self.__requests.get(f"{self.__base_path}/{containerId}")
        verify_success(r, 201)

        return r.json()

    def refresh_container(self, containerId: int) -> int:
        """
        `Refresh Expiration time of Escrow Container`

        Refresh the container expiration for the same amount of time previously informed.

        :param containerId: The ID of the container
        :type containerId: int
        :return: Status Code
        """
        r = self.__requests.get(
            f"{self.__base_path}/{containerId}/refresh-expiration-time"
        )
        verify_success(r, 204)

        return r.status_code

    def lock(self, containerId: int) -> int:
        """
        `Locks the escrow container (Optional)`
        This action will lock the container. After this action users can not join this container. This doesn't apply to all 3p apps. It's an optional call if a third party wants to make sure that no one else will enter the container.

        :param containerId: The ID of the container
        :type containerId: int
        :return: Status Code
        """
        r = self.__requests.get(f"{self.__base_path}/{containerId}/lock")
        verify_success(r, 204)

        return r.status_code

    def resolve_container(
        self, containerId: int, actions: ResolveContainerPayloadActions
    ) -> ResolveRefundContainerOK:
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
        r = self.__requests.post(
            f"{self.__base_path}/{containerId}/resolve",
            data={"actions": actions},
        )
        verify_success(r, 200)

        return r.json()

    def refund_container(self, containerId: int) -> ResolveRefundContainerOK:
        """
        `Refund container assets`

        It sends back the assets inside the container to the original owners (no fees) and resolves the container.

        :param containerId: The ID of the container you want to join
        :type containerId: int

        :return: Dict response from Upland Developers API
        """
        r = self.__requests.post(
            f"{self.__base_path}/{containerId}/refund",
        )
        verify_success(r, 200)

        return r.json()

    def delete_transaction(self, containerId: int, transactionId: str) -> int:
        """
        `Remove a transaction from container`

        Removes a transaction that has not been signed by the user from container.

        :param containerId: The ID of the container you want to join
        :type containerId: int

        :return: Status Code
        """
        r = self.__requests.delete(
            f"{self.__base_path}/{containerId}/transactions/{transactionId}",
        )
        verify_success(r, 204)

        return r.status_code
