from models import Base, BaseEngine
from models import Score, Special, SubWeapon, User, Weapon


class Migration(object):
    def __init__(self):
        self.engine = BaseEngine().engine

    def exec(self):
        Base.metadata.create_all(self.engine)
