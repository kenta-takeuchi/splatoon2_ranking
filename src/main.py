from service import SplatoonService
from db.migrate import Migration

if __name__ == '__main__':
    Migration().exec()

    splatoon_service = SplatoonService()
    splatoon_service.fetch_x_ranking(month='2021-07-01', rule='tower_control')
    splatoon_service.save()
