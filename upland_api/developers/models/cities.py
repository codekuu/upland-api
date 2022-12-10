from typing import List
from pydantic import BaseModel


class City(BaseModel):
    id: int
    name: str
    stateName: str
    countryName: str


class CitiesOK(BaseModel):
    cities: List[City]
