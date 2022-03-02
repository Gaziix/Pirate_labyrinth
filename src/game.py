import pygame
from player import Player
from accueil import Accueil
import pytmx
import pyscroll

class Game:

    def __init__(self):

        self.screen = pygame.display.set_mode((1280, 800))
        pygame.display.set_caption("Pirate labyrinthe")
        self.pressed = {}

        # Tiled data
        tmx_data = pytmx.util_pygame.load_pygame('../assets/img/map/map_samourai_labyrinthe.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(Game, player_position.x, player_position.y)
        self.group.add(self.player)

        self.walls = []
        self.winnable = []

        # on stocke toutes les collisions défini sur Tiled
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "winnable":
                self.winnable.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        
        
        self.accueil = Accueil(Game)
        

    def update(self):
        self.group.update()
        for sprite in self.group.sprites():
            if sprite.perso.collidelist(self.walls) >= 0:
                sprite.move_back()
            elif sprite.perso.collidelist(self.winnable) > -1:
                print("Bravo tu as réussi à trouver le trésor caché dans le labyrinthe !")
                return False
        return True
    
    def able_to_move(self):
        for sprite in self.group.sprites():
            if sprite.perso.collidelist(self.walls) >= 0:
                return -1
        return 0
    
    def remove_accueil(self):
        self.accueil.all_accueil.remove(self)