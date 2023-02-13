import pygame
pygame.init()

from Loup import Loup
from game import Game
from Pretre import Pretre
from Pnj import Pnj

# générer la fenêtre de jeu
pygame.display.set_caption("Word of Minecraft")
screen = pygame.display.set_mode((1619, 903))

# charger le jeu
game = Game()



#arrière-plan du jeu
background = pygame.image.load('Assets/Cartes/map1.png')


villageois = Pnj(nom="Villageois", image=pygame.image.load('Assets\pnj\$villageois.png'))
garde = Pnj(nom="Garde", image=pygame.image.load('Assets\pnj\$garde.png'))

loup = Loup()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arrière-plan du jeu
    screen.blit(background, (0,0))

    # appliquer l'image du perso
    screen.blit(game.joueur.image, game.joueur.rect)

    # appliquer l'image des pnj
    screen.blit(villageois.image, (475, 500))
    screen.blit(garde.image, (950, 240))

    # appliquer l'image du loup
    screen.blit(loup.image, (750, 240))

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur appuie sur une touche
    if game.pressed.get(pygame.K_RIGHT):
        game.joueur.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.joueur.move_left()
    elif game.pressed.get(pygame.K_UP):
        game.joueur.move_up()
    elif game.pressed.get(pygame.K_DOWN):
        game.joueur.move_down()

    print(game.joueur.rect.x)

    # si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # évenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # détecte si relache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


# appliquer les images des monstres
#screen.blit(game.all_monstres.image, game.all_monstres.rect)

