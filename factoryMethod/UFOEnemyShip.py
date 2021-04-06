from EnemyShip import EnemyShip


class UFOEnemyShip(EnemyShip):
    def __init__(self):
        super().__init__()
        self.set_name("UFO Enemy Ship")
        self.set_amount_damage(30.0)
