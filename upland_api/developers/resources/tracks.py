import requests as RealRequests
from upland_api.global_methods import verify_success
from upland_api.developers.models.tracks import (
    GetTracksOK,
    GetTrackOK,
    GetTrackBuildingsOK,
)


class Tracks:
    """
    TRACKS
    https://api.sandbox.upland.me/developers-api/docs/#/Generic%20Endpoints
    """

    def __init__(self, requests: RealRequests, base_path: str):
        self.__requests = requests
        self.__base_path = base_path

    def get_tracks(self, cityName, includePath) -> GetTracksOK:
        """
        `Locks the escrow container (Optional)`

        List all avaiblable tracks.

        :param cityName: Name of the city to get tracks from (Optional)
        :type cityName: str
        :param includePath: Include paths? (Optional)
        :type includePath: bool

        :return: Dict response from Upland Developers API
        """
        params = {}

        if cityName:
            params["cityName"] = cityName
        if includePath:
            params["includePath"] = includePath

        r = self.__requests.get(f"{self.__base_path}", params=params)
        verify_success(r, 200)

        return r.json()

    def get_track(self, trackId: int) -> GetTrackOK:
        """
        `Retrieve track's information`

        Retrieve track's information given an track ID.

        :param trackId: ID of the track
        :type trackId: int
        :return: Dict response from Upland Developers API
        """
        r = self.__requests.get(f"{self.__base_path}/{trackId}")
        verify_success(r, 200)

        return r.json()

    def get_track_buildings(self, trackId: int) -> GetTrackBuildingsOK:
        """
        `Retrieve buildings on a track`

        Will return all the constructions along the selected track

        :param trackId: ID of the track
        :type trackId: int
        :return: Dict response from Upland Developers API
        """
        r = self.__requests.get(f"{self.__base_path}/{trackId}/buildings")
        verify_success(r, 200)

        return r.json()
