import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

# Clock to control frame rate
clock = pygame.time.Clock()

# Rectangle properties
rect_width = 50
rect_height = 50
rect_x = 100
rect_y = 100
rect_speed_x = 5
rect_speed_y = 5

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update rectangle position
    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Bounce the rectangle off the edges
    if rect_x <= 0 or rect_x + rect_width >= SCREEN_WIDTH:
        rect_speed_x = -rect_speed_x
    if rect_y <= 0 or rect_y + rect_height >= SCREEN_HEIGHT:
        rect_speed_y = -rect_speed_y

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
