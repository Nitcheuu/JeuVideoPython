import pygame
import time
import math
pygame.init()
from game import Game

# window

pygame.display.set_caption("Premier Jeu")
screen = pygame.display.set_mode((1080, 720))

# importe et charge le fond d'écran

bg = pygame.image.load('assets/bg.jpg')

# importer la bannière

'''banner_x = 500
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (banner_x, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 2 - banner_x / 2)'''

# importer le bouton

button_x = 400
button = pygame.image.load("assets/button.png")
button = pygame.transform.scale(button, (button_x, 150))
button_rect = button.get_rect()
button_rect.x = math.ceil(screen.get_width() / 2 - button_x / 2)
button_rect.y = 100

# importer le bouton quit

quit_button = pygame.image.load("assets/quit_button.jpg")
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = 800
quit_button_rect.y = 540

# importer le bouton de commande

command_button = pygame.image.load("assets/command_button.jpg")
command_button_rect = command_button.get_rect()
command_button_rect.x = 80
command_button_rect.y = 540

# charger le jeu

game = Game(screen)

# boucle de la partie

running = True

while running:

    # appliquer le fond d'écran (variable bg, (position))

    screen.blit(bg, (0, -200))

    # verifier si le jeu a commencé

    if game.is_playing == 0:
        # déclencher les instructions de la game
        game.update(screen)

    elif game.is_playing == 1:
        # importer le bouton
        pygame.draw.rect(screen, (255, 255, 255), [button_rect.x - 5, button_rect.y, 410, 160])
        screen.blit(button, (button_rect.x, 105))
        '''# importer la bannière
        screen.blit(banner, (banner_rect.x, 0)'''
        # importer le bouton
        pygame.draw.rect(screen, (255, 255, 255), [quit_button_rect.x - 5, quit_button_rect.y - 5, 210, 110])
        screen.blit(quit_button, (quit_button_rect.x, 540))
        # importer le bouton commande
        pygame.draw.rect(screen, (255, 255, 255), [command_button_rect.x - 5, command_button_rect.y - 5, 210, 110])
        screen.blit(command_button, (command_button_rect.x, 540))
        #
        screen.blit(game.player.image, (button_rect.x + 90, 300))

    # si on ferme la fenêtre

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # si une touche est relachée

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # lancer le projectile

            if event.key == pygame.K_SPACE:
                game.player.attack_p()

            if event.key == pygame.K_ESCAPE:
                game.game_exit()
                game.is_playing = 1

            if event.key == pygame.K_e:
                game.player.attack_w()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                game.game_start()
            if quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                print("Fermeture du jeu")
            if command_button_rect.collidepoint(event.pos):
                print("Ouverture des commandes")




