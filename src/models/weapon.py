from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Weapon(Base):
    __tablename__ = 'weapon'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    sub_weapon_id = Column(Integer, ForeignKey('sub_weapon.id'))
    special_id = Column(Integer, ForeignKey('special.id'))

    scores = relationship("Score", back_populates="weapon")
    sub_weapon = relationship("SubWeapon", back_populates="weapons")
    special = relationship("Special", back_populates="weapons")
