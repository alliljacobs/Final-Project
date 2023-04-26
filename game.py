import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Reverse')

# Set up the game clock
clock = pygame.time.Clock()

# Define colors
PINK = (251, 182, 209)
GREY = (182, 187, 199)
BLUE = (154, 206, 223)

# Set up the player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
player_x = WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = WINDOW_HEIGHT // 2 - PLAYER_HEIGHT // 2
player_speed = 5
player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)

# Set up the enemy
ENEMY_WIDTH = 30
ENEMY_HEIGHT = 30
enemy_x = random.randint(0, WINDOW_WIDTH - ENEMY_WIDTH)
enemy_y = random.randint(0, WINDOW_HEIGHT - ENEMY_HEIGHT)
enemy_speed = 3
enemy_rect = pygame.Rect(enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT)

# Set up the score
score = 0
font = pygame.font.SysFont('Arial', 30)

# Main game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x += player_speed
    elif keys[pygame.K_RIGHT]:
        player_rect.x -= player_speed
    elif keys[pygame.K_UP]:
        player_rect.y += player_speed
    elif keys[pygame.K_DOWN]:
        player_rect.y -= player_speed

    # Check for collisions
    if player_rect.colliderect(enemy_rect):
        score += 1
        enemy_x = random.randint(0, WINDOW_WIDTH - ENEMY_WIDTH)
        enemy_y = random.randint(0, WINDOW_HEIGHT - ENEMY_HEIGHT)
        enemy_rect.x = enemy_x
        enemy_rect.y = enemy_y

    # Draw the game window
    game_window.fill(GREY)
    pygame.draw.rect(game_window, BLUE, enemy_rect)
    pygame.draw.rect(game_window, PINK, player_rect)

    # Draw the score
    score_text = font.render(f'Score: {score}', True, PINK)
    game_window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the game's frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
