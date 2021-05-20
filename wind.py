import pygame


class Wind(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("assets/wind.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.game.player.rect.x + 170
        self.rect.y = self.game.player.rect.y + 60
        self.velocity = 5
        self.power = 100

    def wind_remoove(self):
        self.game.player.all_wind.remove(self)

    def wind_moove(self):
        self.rect.x += self.velocity
        if self.rect.x > 1080:
            self.wind_remoove()

        for monster in self.game.check_collision(self, self.game.all_monsters):
            self.wind_remoove()
            monster.recul(self.power)
            print("Vent supprimé")




