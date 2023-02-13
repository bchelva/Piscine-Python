import pygame

from Monstre import Monstre
from Personnage import Personnage
from Pretre import Pretre
from Loup import Loup
from Pnj import Pnj
from camera import *

# créer une seconde classe qui va représenter le jeu
class Game:
    def __init__(self):
        #definir si notre jeu a commencé ou non
        self.is_playing = False
        # générer le joueur
        self.joueur = Pretre()
        self.personnage = Personnage()

        self.loup = Loup()
        self.loup.image = pygame.image.load('Assets/Mechants/Loup/Loup2.png')
        # groupe de monstre
        self.all_monstres = pygame.sprite.Group()
        self.pressed = {}
        #self.spawn_monstre()
        display_w, display_h = 550, 350
        self.canvas = pygame.Surface((display_w, display_h))
        self.window = pygame.display.set_mode(((display_w, display_h)))
        # gérer le son
        self.sounds_manager = SoundManager()
        self.camera = Camera(self.joueur)
        self.follow = Follow(self.camera, self.joueur)
        self.border = Border(self.camera, self.joueur)
        self.auto = Auto(self.camera, self.joueur)
        self.camera.setmethod(self.follow)

    def update(self, screen):
        # appliquer l'image du perso
        screen.blit(self.joueur.image, self.joueur.rect)

        villageois = Pnj(nom="Villageois", image=pygame.image.load('Assets\pnj\$villageois.png'))
        garde = Pnj(nom="Garde", image=pygame.image.load('Assets\pnj\$garde.png'))

        # appliquer l'image des pnj
        screen.blit(villageois.image, (475, 500))
        screen.blit(garde.image, (950, 240))

        def spawn_mechant(self):
            monstre = Monstre()

        # appliquer l'image du loup
        #screen.blit(self.Loup.image, (750, 240))

        # si le joueur appuie sur une touche
        #if self.pressed.get(pygame.K_RIGHT):
        #    self.joueur.move_right()
        #elif self.pressed.get(pygame.K_LEFT):
        #    self.joueur.move_left()
        #elif self.pressed.get(pygame.K_UP):
        #    self.joueur.move_up()
        #elif self.pressed.get(pygame.K_DOWN):
        #    self.joueur.move_down()
