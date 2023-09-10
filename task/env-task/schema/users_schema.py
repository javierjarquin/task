from pydantic import BaseModel
from typing import Optional


class usersSchema(BaseModel):
    id: Optional[int]
    name: str
    surname: str
    weight: float
    