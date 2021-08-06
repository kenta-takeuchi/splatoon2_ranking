from service import SplatoonService

if __name__ == '__main__':
    splatoon_service = SplatoonService()
    splatoon_service.get_x_ranking('210701T00_210801T00', 'tower_control')
