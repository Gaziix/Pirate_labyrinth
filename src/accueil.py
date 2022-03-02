import pygame

# Images pour notre page d'accueil
class Accueil(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.banner = pygame.image.load('../assets/img/banner.png')
        self.rect_banner = self.banner.get_rect()
        self.rect_banner.x = 250
        self.rect_banner.y = 200
        self.all_accueil = pygame.sprite.Group()
        