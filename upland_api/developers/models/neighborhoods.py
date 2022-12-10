from typing import List, Optional
from pydantic import BaseModel


class Result(BaseModel):
    id: int
    name: str
    cityId: Optional[int] = None
    area: float
    boundaries: List[List[List[float]]]
    center: List[float]
    city_id: Optional[int] = None


class GetNeighborhoodsOK(BaseModel):
    results: List[Result]
