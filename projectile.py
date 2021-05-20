import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, velocity, image):
        super().__init__()
        self.player = player
        self.velocity = velocity
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 180
        self.rect.y = player.rect.y + 60
        self.attack = 1
        self.angle = 0

    def remove_p(self):
        self.player.all_projectiles.remove(self)

    def move_p(self):
        self.rect.x += self.velocity + 1
        # self.rotate_p()
        if self.rect.x > 1080:
            self.remove_p()

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove_p()
            monster.degats(self.attack)
            print("Porjo supp")





