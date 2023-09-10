from pydantic import BaseModel
from typing import Optional
from datetime import datetime, time

class taskSchema(BaseModel):
    id: Optional[int]
    creationDate: datetime
    code: str
    status: str
    taskType: str
    isFinish: int
    checkTime: time
    finishDate: datetime
    userId: int