from typing import List
from pydantic import BaseModel


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


class BuildingsOK(BaseModel):
    buildings: List[Building]
