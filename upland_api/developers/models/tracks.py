from typing import List
from pydantic import BaseModel


class Track(BaseModel):
    id: int
    name: str
    path: List[List[float]]


class Meshes(BaseModel):
    Wall: str
    Roof: str
    Detail: str


class Building(BaseModel):
    id: int
    model_id: int
    name: str
    model: str
    lat: str
    lng: str
    rotate: List[float]
    scale: float
    altitude: int
    meshes: Meshes


class GetTracksOK(BaseModel):
    tracks: List[Track]


class GetTrackOK(BaseModel):
    id: int
    name: str
    path: List[List[float]]
    center: List[str]
    boundaries: List[List[List[float]]]


class GetTrackBuildingsOK(BaseModel):
    buildings: List[Building]
