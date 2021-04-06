from RocketEnemyShip import RocketEnemyShip
from UFOEnemyShip import UFOEnemyShip


class EnemyShipFactory:
    def make_enemy_ship(self, ship_id: str):
        if ship_id == 'UFO':
            return UFOEnemyShip()
        if ship_id == 'Rocket':
            return RocketEnemyShip()
        return None
