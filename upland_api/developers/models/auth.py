from pydantic import BaseModel
from datetime import datetime


class CreatedConnectionCodeCreated(BaseModel):
    code: str
    expireAt: datetime
