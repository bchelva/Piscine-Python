import pygame

# Initialize Pygame
pygame.init()

# Load map image
map_img = pygame.image.load("map.png")

# Set screen size to match map image size
screen = pygame.display.set_mode(map_img.get_rect().size)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw map on screen
    screen.blit(map_img, (0, 0))

    # Update display
    pygame.display.update()

# Initialize Pygame
pygame.init()

# Load map and warrior images
map_img = pygame.image.load("map.png")
warrior_img = pygame.image.load("warrior.png")

# Set screen size to match map image size
screen = pygame.display.set_mode(map_img.get_rect().size)

# Set warrior starting position
warrior_pos = [400, 500]

# Speed of warrior movement
speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Move warrior based on arrow key presses
            if event.key == pygame.K_UP:
                warrior_pos[1] -= speed
            elif event.key == pygame.K_DOWN:
                warrior_pos[1] += speed
            elif event.key == pygame.K_LEFT:
                warrior_pos[0] -= speed
            elif event.key == pygame.K_RIGHT:
                warrior_pos[0] += speed

    # Draw map on screen
    screen.blit(map_img, (0, 0))

    # Draw warrior on screen
    screen.blit(warrior_img, warrior_pos)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
