from abc import ABC


class EnemyShip(ABC):

    def __init__(self):
        self.name = None
        self.amount_damage = None

    def set_name(self, name: str):
        self.name = name

    def set_amount_damage(self, amount_damage: float):
        self.amount_damage = amount_damage

    def follow_hero_ship(self):
        print(self.name + ' is following the hero')

    def display_enemy_ship(self):
        print(self.name + ' is on the screen')

    def enemy_ship_shoots(self):
        print(self.name + ' attacks and does {} damage to hero'.format(self.amount_damage))
