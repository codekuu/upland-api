import requests


class Tracks:
    """
    TRACKS
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints
    """

    def __init__(self, base):
        self.__base = base
        self.__base_url = f"{base.base_url}/tracks"

    def get_tracks(self, cityName, includePath):
        """
        `Locks the escrow container (Optional)`

        List all avaiblable tracks.

        :param cityName: Name of the city to get tracks from (Optional)
        :type cityName: str
        :param includePath: Include paths? (Optional)
        :type includePath: bool

        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}"
        params = {}

        if cityName:
            params["cityName"] = cityName
        if includePath:
            params["includePath"] = includePath

        r = requests.get(url, headers=self.__base.headers, params=params)
        return r.status_code

    def get_track(self, trackId: int):
        """
        `Retrieve track's information`

        Retrieve track's information given an track ID.

        :param trackId: ID of the track
        :type trackId: int
        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}/{trackId}"
        r = requests.get(url, headers=self.__base.headers).json()
        return r

    def get_track_buildings(self, trackId: int):
        """
        `Retrieve buildings on a track`

        Will return all the constructions along the selected track

        :param trackId: ID of the track
        :type trackId: int
        :return: Dict response from Upland Developers API
        """
        url = f"{self.__base_url}/{trackId}/buildings"
        r = requests.get(url, headers=self.__base.headers).json()
        return r
