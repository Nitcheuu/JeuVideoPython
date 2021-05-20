import pygame
from boss import Boss


class BossEvent:

    def __init__(self):
        self.percent = 0
        self.percent_speed = 30
        self.all_boss = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def boss_comming(self):
        self.all_boss.add(Boss())

    def attempt_boss(self):
        if self.is_full_loaded():
            print("Arrivé du boss")

    def update_bar(self, surface):
        self.add_percent()
        pygame.draw.rect(surface, (0, 0, 0), [0, 20, surface.get_width(), 10])
        pygame.draw.rect(surface, (187, 11, 11), [0, 20, (surface.get_width() / 100) * self.percent, 10])
        self.attempt_boss()