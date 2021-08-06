from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class SubWeapon(Base):
    __tablename__ = 'sub_weapon'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    weapons = relationship("Weapon", back_populates="sub_weapon")
