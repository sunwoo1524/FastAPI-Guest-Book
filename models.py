from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

from database import Base


# 방명록 테이블
class GuestBook(Base):
    __tablename__ = "guestbook"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.now)
    note = Column(String, nullable=False)