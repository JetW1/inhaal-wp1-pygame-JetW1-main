import sys
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 700
screen_height = 600

# Game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cybertruck Game")

# Images
bg_image = pygame.image.load('docs/images/space.png.jpg').convert_alpha()



# Game loop
while True:
    # Background
    screen.blit(bg_image, (0, 0))
    bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Update display
    pygame.display.update()

    # Control the frame rate
    pygame.time.Clock().tick(60)
