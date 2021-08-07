import configparser
from datetime import datetime as dt
import json
import urllib.parse

import requests
from sqlalchemy import and_

from constracts import RULE
from models import BaseSession
from models import Score, Special, SubWeapon, User, Weapon

settings = configparser.SafeConfigParser()
settings.read('settings.ini')


class SplatoonService:
    def __init__(self):
        self.headers = {
            'Accept-language': 'ja',
            'Cookie': f'iksm_session={settings.get("SPLANET", "iksm_session")}',
            'User-Agent': settings.get('SPLANET', 'user_agent')}
        self.base_url = settings.get('SPLANET', 'base_url')
        self.rule = ''
        self.ranking_data = []
        self.month = ''

    def fetch_x_ranking(self, month: str, rule: str):
        if rule not in RULE:
            raise ValueError
        self.month = month
        self.rule = rule

        url = urllib.parse.urljoin(self.base_url, f'x_power_ranking/{self._filtering_month()}/{rule}')
        results = []
        for i in range(1, 6):
            params = {'page': i}
            response = requests.get(url, headers=self.headers, params=params)
            results.extend(json.loads(response.text)['top_rankings'])

        self.ranking_data = results

    def save(self):
        # TODO
        #  N+1以上のことしているのでやばい
        #  sqliteにfind_or_createないか調べる
        #  find_or_createの処理を各モデルクラスに移行する
        #  武器のマスタデータのAPI探す
        #   マスタデータを登録するメソッドを作る
        #   saveメソッドから武器のfind_or_create処理を削除して、userとscoreのfind_or_createのみにする
        session = BaseSession().get_session()
        for data in self.ranking_data:
            user = session.query(User).get(data['unique_id'])
            if user is None:
                user = User.create(session, data['unique_id'], data['name'])

            # weapon = session.query(Weapon).get(int(data['weapon']['id']))
            # if weapon is None:
                # sub_weapon = session.query(SubWeapon).get(int(data['weapon']['sub']['id']))
                # if sub_weapon is None:
                #     sub_weapon = SubWeapon.create(session, int(data['weapon']['sub']['id']),
                #                                   data['weapon']['sub']['name'])
                #
                # special = session.query(Special).get(int(data['weapon']['special']['id']))
                # if special is None:
                #     special = Special.create(session, int(data['weapon']['special']['id']),
                #                              data['weapon']['special']['name'])

                # weapon = Weapon.create(session, int(data['weapon']['id']), data['weapon']['name'], sub_weapon.id,
                #                        special.id)

            score = session.query(Score).filter(and_(Score.user_unique_id == user.unique_id,
                                                     Score.scored_at == self.month,
                                                     Score.rule == self.rule)).scalar()
            if score is None:
                Score.create(session, user, self.rule, dt.strptime(self.month, '%Y-%m-%d'), data['x_power'],
                             data['rank'], int(data['weapon']['id']))
            session.commit()

    def _filtering_month(self):
        this_month = f'{self.month[2:4]}{self.month[5:7]}'
        if self.month[5:7] == '12':
            next_month = f'{int(self.month[2:4]) + 1}01'
        else:
            next_month = f'{self.month[2:4]}{str(int(self.month[5:7]) + 1).zfill(2)}'
        return f'{this_month}01T00_{next_month}01T00'
