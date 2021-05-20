import pygame
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxhealth = 100
        self.attack = 0.2
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1080 + random.randint(0, 50)
        self.rect.y = 550
        self.velocity = random.randint(1, 4)
        self.random_monster()
        self.loot = 5

    def update_health_bar(self, surface):
        if self.velocity < 3:
            pygame.draw.rect(surface, (111, 210, 46), [self.rect.x+12, self.rect.y-10, self.health, 5])
        if self.velocity > 2:
            pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 60, self.rect.y - 10, self.health, 5])

    def monster_red_health(self, surface):
        if self.velocity < 3:
            pygame.draw.rect(surface, (255, 0, 0), [self.rect.x+12, self.rect.y-10, self.maxhealth, 5])
        if self.velocity > 2:
            pygame.draw.rect(surface, (255, 0, 0), [self.rect.x+60, self.rect.y-10, self.maxhealth, 5])

    def attaquer(self):
        self.game.player.damage(self.attack)

    def avancer(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        else:
            self.attaquer()

    def random_monster(self):
        if self.velocity > 2:
            self.image = pygame.image.load("assets/player.png")
            self.rect.y = 510
            self.maxhealth = 80
            self.health = 80
        if self.velocity < 3:
            self.image = pygame.image.load("assets/mummy.png")
            self.rect.y = 550
            self.maxhealth = 100
            self.health = 100
            self.attack = 0.5

    def degats(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1080 + random.randint(0, 50)
            self.health = self.maxhealth
            self.velocity = random.randint(1, 4)
            self.random_monster()
            self.game.percent += self.loot

    def recul(self, amount):
        if self.velocity > 2:
            self.rect.x += amount
        if self.velocity < 3:
            self.rect.x += amount * 0.5
