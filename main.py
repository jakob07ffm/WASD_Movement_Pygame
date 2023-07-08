import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 480
screen_height = 320
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("WASD Game")

# Set up the player
player_width = 50
player_height = 50
player_x = (screen_width - player_width) // 2
player_y = (screen_height - player_height) // 2
player_speed = 5

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill the screen with white

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Get the keys that are currently pressed
    keys = pygame.key.get_pressed()

    # Move the player based on the keys pressed
    if keys[K_w]:
        player_y -= player_speed
    if keys[K_s]:
        player_y += player_speed
    if keys[K_a]:
        player_x -= player_speed
    if keys[K_d]:
        player_x += player_speed

    # Ensure the player stays within the screen boundaries
    if player_x < 0:
        player_x = 0
    elif player_x + player_width > screen_width:
        player_x = screen_width - player_width
    if player_y < 0:
        player_y = 0
    elif player_y + player_height > screen_height:
        player_y = screen_height - player_height

    # Draw the player on the screen
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))

    pygame.display.flip()

# Quit the game
pygame.quit()