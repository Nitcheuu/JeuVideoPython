import pygame


class FireBlast(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("assets/fire_blast.png")
        self.image = pygame.transform.scale(self.image, (300, 100))
        self.damage = 1
        self.rect = self.image.get_rect()
        self.rect.x = self.game.player.rect.x + 170
        self.rect.y = self.game.player.rect.y + 30
        self.velocity = self.game.player.velocity
        self.maxdurability = 150
        self.durability = 150
        self.degats = 1

    def fire_is_ok(self):
        if self.durability > 0:
            return True
        else:
            print("Il n'y pas assez de feu")
            return False

    def fire_reload(self):
        if self.durability < 150:
            self.durability += 0.2

    def regain_durability(self, amount):
        if self.maxdurability <= self.durability + amount:
            self.durability = self.maxdurability
        else:
            self.durability += amount

    def fire_moove(self):
        self.rect.x = self.rect.x = self.game.player.rect.x + 170

    def fire_damage(self):
        if self.durability > 50:
            self.degats = 2
            self.image = pygame.transform.scale(self.image, (300, 100))
            self.rect.y = self.game.player.rect.y + 30
        '''if self.durability <= 50:
            self.degats = 0.5
            self.image = pygame.transform.scale(self.image, (150, 50))
            self.rect.y = self.game.player.rect.y + 55
        if self.durability <= 3:
            self.degats = 0.1
            self.image = pygame.transform.scale(self.image, (100, 30))
            self.rect.y = self.game.player.rect.y + 65'''
        if self.game.check_collision(self, self.game.all_monsters):
            for monster in self.game.check_collision(self, self.game.all_monsters):
                monster.degats(self.degats)
        self.durability -= 1