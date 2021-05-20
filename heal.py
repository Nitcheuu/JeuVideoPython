import pygame
import random


class Heal(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.heal = random.randint(50, 75)
        self.image = pygame.image.load("assets/heal.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 500)
        self.rect.y = -500
        self.originy = -500
        self.velocity = random.randint(1, 2)

    def drop_life(self):
        self.rect.y += self.velocity

    def heal_player(self):
        if self.game.check_collision(self, self.game.all_player):
            self.game.player.heal_myself(self.heal)
            # self.game.fireblast.regain_durability(self.heal)
            self.rect.x = random.randint(50, 500)
            self.rect.y = -500
        if self.rect.y > 700:
            self.rect.x = random.randint(50, 500)
            self.rect.y = -500