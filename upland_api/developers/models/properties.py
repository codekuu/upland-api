from typing import List
from pydantic import BaseModel


class Neighborhood(BaseModel):
    id: int
    name: str


class Result(BaseModel):
    id: int
    address: str
    neighborhood: Neighborhood


class GetPropertiesOK(BaseModel):
    currentPage: int
    pageSize: int
    totalResults: int
    results: List[Result]
