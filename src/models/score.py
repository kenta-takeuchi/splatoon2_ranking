from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, func, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Score(Base):
    __tablename__ = 'score'

    id = Column(Integer, primary_key=True)
    user_unique_id = Column(Integer, ForeignKey('user.unique_id'))
    rule = Column(String(20))
    scored_at = Column(Date)
    power = Column(Float)
    rank = Column(Integer)
    weapon_id = Column(Integer, ForeignKey('weapon.id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="scores")
    weapon = relationship("Weapon", back_populates="scores")

    @staticmethod
    def create(session, user, rule, scored_at, power, rank, weapon_id):
        score = Score(user=user, rule=rule, scored_at=scored_at, power=power, rank=rank, weapon_id=weapon_id)
        session.add(score)
        return user
