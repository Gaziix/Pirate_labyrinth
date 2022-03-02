import pygame
from game import Game

pygame.init()

game = Game()

# Notre jeu principal
def launch_game():
    running = True
    while running:
        running = game.update()
        game.group.draw(game.screen)

        pygame.display.flip() # Actualise la page

        # On prend les actions les gadgets récupérent
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Pour quitter l'application
                running = False
            elif event.type == pygame.KEYDOWN:  # Une touche enclenchée
                game.pressed[event.key] = True
                if event.key == pygame.K_ESCAPE:
                    running = False 
                elif event.key == pygame.K_UP and game.player.rect.y > 0:
                    game.player.move_top()
                elif event.key == pygame.K_RIGHT and game.player.rect.x + game.player.rect.width + 25 < game.screen.get_width():
                    game.player.move_right()
                elif event.key == pygame.K_LEFT and game.player.rect.x > 0:
                    game.player.move_left()
                elif event.key == pygame.K_DOWN and game.player.rect.y + game.player.rect.height + 25 < game.screen.get_height():
                    game.player.move_down()
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

# Notre page d'accueil
def launch_all():
    running_accueil = True
    click_sounds = pygame.mixer.Sound("../assets/sound/click.ogg")
    background = pygame.image.load('../assets/img/bg_accueil.jpg')
    while running_accueil:
        game.screen.blit(background, (0, 0))  # mettre un fond d'écran et viser quelle partie on veut
        game.screen.blit(game.accueil.banner, game.accueil.rect_banner)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pour quitter l'application
                running_accueil = False
                game.remove_accueil()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if game.accueil.rect_banner.collidepoint(pos):
                    game.remove_accueil()
                    click_sounds.play()
                    launch_game()
                    running_accueil = False
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    game.remove_accueil()
                    launch_game()
                    running_accueil = False
                    
    pygame.quit() # On quitte la fenêtre pygame

launch_all()