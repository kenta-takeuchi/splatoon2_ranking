import configparser
import json
import urllib.parse

import requests

settings = configparser.SafeConfigParser()
settings.read('settings.ini')


class SplatoonService:
    def __init__(self):
        self.headers = {
            'Accept-language': 'ja',
            'Cookie': f'iksm_session={settings.get("SPLANET", "iksm_session")}',
            'User-Agent': settings.get('SPLANET', 'user_agent')}
        self.base_url = settings.get('SPLANET', 'base_url')

    def get_x_ranking(self, month: str, rule: str):
        url = urllib.parse.urljoin(self.base_url, f'x_power_ranking/{month}/{rule}')
        results = []
        for i in range(1, 6):
            params = {'page': i}
            response = requests.get(url, headers=self.headers, params=params)
            results.extend(json.loads(response.text)['top_rankings'])
        print(results[0])
        print(len(results))
