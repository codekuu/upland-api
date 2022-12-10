from typing import List, Optional
from pydantic import BaseModel


class City(BaseModel):
    city_id: int
    city_name: str
    state_name: str
    country_name: str


class Features(BaseModel):
    treasures: List[int]
    standard_treasure: List[int]
    collections: List[int]
    riot_mode: List[int]
    construction: List[int]
    nft_swap: List[str]


class ProfilePic(BaseModel):
    city_id: int
    image: Optional[str]


class GetCityOK(BaseModel):
    cities: List[City]
    features: Features
    profile_pics: List[ProfilePic]
