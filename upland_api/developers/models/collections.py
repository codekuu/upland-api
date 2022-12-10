from typing import List, Optional
from pydantic import BaseModel


class Result(BaseModel):
    id: int
    name: str
    amount: int
    rarityLevel: int
    description: str
    requirements: str
    yieldBoost: float
    oneTimeReward: int
    image: str
    imageThumbnail: str
    cityId: Optional[int]


class CollectionsOK(BaseModel):
    results: List[Result]
