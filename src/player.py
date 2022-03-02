import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.player = Player
        self.image = pygame.image.load('../assets/img/pirate.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.vitesse = 32
        self.rect = self.image.get_rect()
        pygame.display.set_icon(self.image)
        self.position = [x, y]
        self.old_position = self.position.copy()

    def save_location(self):
        self.old_position = self.position.copy()
    
    def move_back(self):
        self.position = self.old_position.copy()
        self.perso = pygame.Rect(self.position[0], self.position[1], self.rect.width, self.rect.height)

    def update(self):
        self.rect.topleft = self.position
        self.perso = pygame.Rect(self.position[0], self.position[1], self.rect.width, self.rect.height)
    
    # défini les différentes façon de bouger du joueur
    def move_right(self):
        self.save_location()
        self.position[0] += self.vitesse
    
    def move_left(self):
        self.save_location()
        self.position[0] -= self.vitesse

    def move_top(self):
        self.save_location()
        self.position[1] -= self.vitesse

    def move_down(self):
        self.save_location()
        self.position[1] += self.vitesse
