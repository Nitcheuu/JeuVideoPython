from player import Player
from monster import Monster
from heal import Heal
from fire_blast import FireBlast
import pygame
import math
pygame.init()


class Game:

    def __init__(self, screen):
        # bool pour jeu
        self.is_playing = 1
        # charger le joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        # charger les monstres
        self.all_monsters = pygame.sprite.Group()
        # charger les heal
        self.all_heal = pygame.sprite.Group()
        self.heal = Heal(self)
        # charger le lance flamme
        self.all_fireblast = pygame.sprite.Group()
        self.fireblast = FireBlast(self)
        # charger le boss
        self.all_boss = pygame.sprite.Group()
        # charger le dico vide
        self.pressed = {}
        # mettre le boss sur False
        self.percent = 0
        self.maxpercent = 200
        self.percent_speed = 1
        self.boss_is_coming = False
        # récupérer l'écran
        self.screen = screen

    def game_exit(self):
        # on retire les groupes de l'écran
        self.all_monsters = pygame.sprite.Group()
        self.all_heal = pygame.sprite.Group()
        self.all_fireblast = pygame.sprite.Group()
        self.player.health = self.player.maxhealth
        self.percent = 0
        self.is_playing = 1

    def game_start(self):
        self.is_playing = 0
        self.spawn_monster()
        self.spawn_monster()
        self.all_heal.add(self.heal)
        self.all_fireblast.add(self.fireblast)

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.all_heal = pygame.sprite.Group()
        self.all_fireblast = pygame.sprite.Group()
        self.player.health = self.player.maxhealth
        self.is_playing = 1

    def update(self, screen):
        # afficher le score

        font = pygame.font.Font("assets/Coda.ttf", 18)
        div = pygame.font.Font("assets/Coda.ttf", 8)
        score_text = font.render("Score : " + str(self.percent) + " / " + str(self.maxpercent), 1, (0, 0, 0))
        hp_text = div.render(str(math.ceil(self.player.health)) + "/" + str(self.player.maxhealth), 1, (255, 255, 255))
        fire_text = div.render(str(math.ceil(self.fireblast.durability * 0.665)) + "%", 1, (255, 255, 255))
        wind_text = div.render(str(math.ceil(self.player.pourcent)) + "%", 1, (255, 255, 255))

        # appliquer l'image du joueur (class player self.sprite, position self.rect)

        screen.blit(self.player.image, self.player.rect)

        # appliquer la barre de vie du joueur

        self.player.player_red_health(screen)
        self.player.update_player_health(screen)
        screen.blit(hp_text, (self.player.rect.x+ 110, self.player.rect.y-12))

        # apliquer la barre de fireblast

        self.player.uptade_player_fire(screen)
        screen.blit(fire_text, (75, 100))

        # appliquer la barre de vent

        self.player.update_player_wind(screen)
        screen.blit(wind_text, (75, 70))

        # appliquer la barre de fin

        self.update_end_bar(screen)
        screen.blit(score_text, (10, 25))

        #

        self.end()

        # apliquer le déplacement des projectiles

        for projectile in self.player.all_projectiles:
            projectile.move_p()

        # appliquer le déplacement des monstres et la barre de vie

        for monster in self.all_monsters:
            monster.avancer()
            monster.monster_red_health(screen)
            monster.update_health_bar(screen)

        # appliquer les propriétés du boss

        for boss in self.all_boss:
            boss.boss_moove()

        # appliquer le déplacement du soin

        for heal in self.all_heal:
            heal.drop_life()
            heal.heal_player()

        # appliquer le lance-flamme

        for fireblast in self.all_fireblast:
            fireblast.fire_reload()

        # appliquer les propriétès du vent

        for wind in self.player.all_wind:
            wind.wind_moove()

        self.player.wind_cooldown()

        # afficher tous les projectiles

        self.player.all_projectiles.draw(screen)

        # afficher tous les monstres

        self.all_monsters.draw(screen)

        # afficher tous les boss

        self.all_boss.draw(screen)

        # afficher les soins

        self.all_heal.draw(screen)

        # afficher le vent

        self.player.all_wind.draw(screen)


        # mettre à jour l'écran

        pygame.display.flip()

        # Afficher des informations en console

        # print(game.player.rect.x)
        # print(game.player.name)

        # différentes touches

        '''while game.player.rect.y != 500:
            game.player.rect.y += game.player.downjump'''

        self.touches()

    def touches(self):
        if self.pressed.get(pygame.K_d) and self.player.rect.x < 890:
            self.player.move_right()
        elif self.pressed.get(pygame.K_a) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_q):
            # appliquer les props du lance flamme

            for fireblast in self.all_fireblast:
                if fireblast.fire_is_ok():
                    fireblast.fire_moove()
                    fireblast.fire_damage()
                    self.all_fireblast.draw(self.screen)

        '''elif game.pressed.get(pygame.K_SPACE) and game.player.rect.y > 399:
            game.player.move_jump()'''

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def end(self):
        if not self.boss_is_coming:
            print(self.percent)
        if self.percent >= self.maxpercent:
            self.percent = 100
            self.boss_is_coming = True
            self.is_playing = 1
        if self.is_playing == 1:
            self.all_monsters = pygame.sprite.Group()
            self.player.rect.x = self.player.originx
            self.player.pourcent = self.player.maxpourcent
            self.player.health = self.player.maxhealth
            self.fireblast.durability = self.fireblast.maxdurability
            self.heal.rect.y = self.heal.originy
            self.percent = 0

    def update_end_bar(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), [0, 10, self.maxpercent * 5.4, 5])
        pygame.draw.rect(surface, (255, 0, 0), [0, 10, self.percent * 5.4, 5])










