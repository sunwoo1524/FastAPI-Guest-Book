from pydantic import BaseModel
from datetime import datetime


# 방명록 스키마
class Note(BaseModel):
    name: str
    date: datetime = datetime.now()
    note: str