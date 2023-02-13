import pygame

from Monstre import Monstre
from Personnage import Personnage
from Pretre import Pretre

# créer une seconde classe qui va représenter le jeu
class Game:
    def __init__(self):
        # générer le joueur
        #self.joueur = (self)
        #self.pressed = {}
        # groupe de monstre
        self.all_monstres = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_mechant()
        self.joueur = Pretre()

    def spawn_mechant(self):
        monstre = Monstre()