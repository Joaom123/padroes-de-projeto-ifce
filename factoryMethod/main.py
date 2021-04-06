from EnemyShipFactory import EnemyShipFactory

enemy_ship_factory = EnemyShipFactory()

rocket_enemy_ship = enemy_ship_factory.make_enemy_ship('Rocket')
rocket_enemy_ship.display_enemy_ship()
rocket_enemy_ship.follow_hero_ship()
rocket_enemy_ship.enemy_ship_shoots()

ufo_enemy_ship = enemy_ship_factory.make_enemy_ship('UFO')
ufo_enemy_ship.display_enemy_ship()
ufo_enemy_ship.follow_hero_ship()
ufo_enemy_ship.enemy_ship_shoots()
