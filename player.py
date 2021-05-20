import pygame
import random
import math
from projectile import Projectile
from wind import Wind
pygame.init()


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.name = 'Dracaufeu'
        self.health = 150
        self.maxhealth = self.health
        self.attack = 6
        self.velocity = 5
        self.armor = 3
        self.image = pygame.image.load('assets/Fire_Dragon.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 500
        self.originx = 100
        self.originy = 500
        self.movejump = 200
        self.all_projectiles = pygame.sprite.Group()
        self.all_wind = pygame.sprite.Group()
        self.pourcent = 100
        self.maxpourcent = 100
        self.pourcent_speed = 1
        self.coolown_is_load = True
        self.attack_w_2 = True

    def move_right(self):
        # si le joueur n'est pas en collision
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def attack_p(self):
        self.all_projectiles.add(Projectile(self, self.velocity, 'assets/projectile.png'))

    def attack_w(self):
        if self.coolown_is_load:
            self.all_wind.add(Wind(self.game))
            self.attack_w_2 = False
            self.pourcent = 0
        else:
            print("Impossible")

    def wind_cooldown(self):
        if not self.attack_w_2:
            self.pourcent += math.ceil(self.pourcent_speed) / 2
            print(self.pourcent)
            self.coolown_is_load = False
            if self.pourcent >= 100:
                self.pourcent = 100
                self.coolown_is_load = True

    def update_player_health(self, surface):
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x+50, self.rect.y-10, self.health, 10])

    def player_red_health(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), [self.rect.x+50, self.rect.y-10, self.maxhealth, 10])

    def uptade_player_fire(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), [10, 90, self.game.fireblast.maxdurability, 10])
        pygame.draw.rect(surface, (255, 0, 0), [10, 90, self.game.fireblast.durability, 10])

    def update_player_wind(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), [10, 60, self.maxpourcent * 1.5, 10])
        pygame.draw.rect(surface, (255, 255, 255), [10, 60, self.pourcent * 1.5, 10])

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def heal_myself(self, amount):
        if self.health + amount < self.maxhealth:
            self.health += amount
        else:
            self.health = self.maxhealth


    '''def move_jump(self):
        self.rect.y -= self.movejump

    def move_jump2(self):
        self.rect.y += self.movejump'''
