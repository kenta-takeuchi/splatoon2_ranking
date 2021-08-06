from sqlalchemy import Column, DateTime, func, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'user'

    unique_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    scores = relationship("Score", back_populates="users")
