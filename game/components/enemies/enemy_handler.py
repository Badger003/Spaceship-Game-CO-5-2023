from game.components.enemies.ship import Ship
from game.components.enemies.ship2 import Ship2

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies.append(Ship())
        self.enemies.append(Ship2())
    

    def update(self):
        for enemy in self.enemies:
            enemy.update()

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)  
