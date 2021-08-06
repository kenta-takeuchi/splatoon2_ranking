from sqlalchemy import Column, DateTime, Float, ForeignKey, func, Integer
from sqlalchemy.orm import relationship

from .database import Base


class Score(Base):
    __tablename__ = 'score'

    unique_id = Column(Integer, primary_key=True)
    rank = Column(Integer)
    power = Column(Float)
    scored_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    user_id = Column(Integer, ForeignKey('user.unique_id'))
    weapon_id = Column(Integer, ForeignKey('weapon.id'))

    user = relationship("User", back_populates="scores")
    weapon = relationship("Weapon", back_populates="scores")
