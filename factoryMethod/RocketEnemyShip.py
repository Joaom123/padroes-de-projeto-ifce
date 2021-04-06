from EnemyShip import EnemyShip


class RocketEnemyShip(EnemyShip):
    def __init__(self):
        super().__init__()
        self.set_name("Rocket Enemy Ship")
        self.set_amount_damage(10.0)
