from typing import List
from pydantic import BaseModel


class Result(BaseModel):
    userName: str
    reward: int
    lockedAt: str
    spawnAt: str
    fullAddress: str
    treasureType: str


class Results(BaseModel):
    results: List[Result]


class GetTreasuresHistoryOK(BaseModel):
    results: Results
