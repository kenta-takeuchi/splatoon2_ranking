import configparser
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import json

from service import SplatoonService
from db.migrate import Migration

settings = configparser.SafeConfigParser()
settings.read('settings.ini')

if __name__ == '__main__':
    Migration().exec()

    # TODO
    #  settings.iniで取得する期間とルールを選べるようにする
    #  その期間とルールでfor文でぶん回すようにする
    str_rules = settings.get("SPLANET", "rules")
    rules = json.loads(settings.get("SPLANET", "rules"))
    for rule in rules:
        splatoon_service = SplatoonService()
        splatoon_service.fetch_x_ranking(month='2019-07-01', rule=rule)
        splatoon_service.save()
