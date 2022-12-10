from typing import List
from pydantic import BaseModel


class Result(BaseModel):
    id: int
    category: str
    name: str
    thumbnail: str


class Neighborhood(BaseModel):
    id: int
    name: str


class Result(BaseModel):
    id: int
    address: str
    city: str
    neighborhood: Neighborhood


class GetAssetsPropertiesOK(BaseModel):
    currentPage: int
    pageSize: int
    totalResults: int
    results: List[Result]


class GetAssetNftsOK(BaseModel):
    currentPage: int
    pageSize: int
    totalResults: int
    results: List[Result]


class PostJoinOK(BaseModel):
    transactionId: str


class GetBalacesOK(BaseModel):
    availableUpx: int
    availableSpark: float
    stakedSpark: float
    availableSends: int


class GetProfileOK(BaseModel):
    id: str
    eosId: str
    username: str
    networth: float
    level: str
    avatarUrl: str
    initialCity: str
    currentCity: str
    isInJail: bool
