from typing import List, Optional
from pydantic import BaseModel


class Action(BaseModel):
    assetId: Optional[int]
    amount: Optional[int]
    category: str
    targetEosId: str
    isRefund: Optional[bool]


class Asset(BaseModel):
    id: int
    transactionId: int
    category: str
    ownerEosId: str
    status: str
    assetId: int


class ResolveContainerPayloadActions(BaseModel):
    actions: List[Action]


class CreateContainerOK(BaseModel):
    id: int
    appId: int
    expirationDate: str
    status: str


class GetContainerOK(BaseModel):
    id: int
    appId: int
    expirationDate: str
    status: str
    upx: int
    spark: int
    assets: List[Asset]


class ResolveRefundContainerOK(BaseModel):
    transactionId: str
