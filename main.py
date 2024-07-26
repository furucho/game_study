import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Sample")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SURFACE_COLOR = (167, 255, 100)
COLOR = (255, 100, 98)
BORDER = (255, 100, 98)

# Classes
class Sprite(pygame.sprite.Sprite):
     def __init__(self, color, height, width):
          super().__init__()

          self.image = pygame.Surface([width, height])

          pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

          self.rect = self.image.get_rect()

# Sprite list
all_sprites_list = pygame.sprite.Group()

# Square Sprite
square_size = 50
square = Sprite(RED, square_size, square_size)
square.rect.x = (screen_width - square_size) // 2
square.rect.y = (screen_height - square_size) // 2

all_sprites_list.add(square)

# Chest Sprite
chest_size = 50
chest = Sprite(GREEN, chest_size, chest_size)
chest.rect.x = 50
chest.rect.y = 50

all_sprites_list.add(chest)

# Drawing border
horizontal_border_height = 10
horizontal_border_width = screen_width
vertical_border_height = screen_height
vertical_border_width = 10

upper_border = Sprite(BORDER, horizontal_border_height, horizontal_border_width)
bottom_border = Sprite(BORDER, horizontal_border_height, horizontal_border_width)
left_border = Sprite(BORDER, vertical_border_height, vertical_border_width)
right_border = Sprite(BORDER, vertical_border_height, vertical_border_width)
upper_border.rect.x = 0
upper_border.rect.y = 0
bottom_border.rect.x = 0
bottom_border.rect.y = screen_height - horizontal_border_height
left_border.rect.x = 0
left_border.rect.y = 0
right_border.rect.x = screen_width - vertical_border_width
right_border.rect.y = 0


all_sprites_list.add(upper_border)
all_sprites_list.add(bottom_border)
all_sprites_list.add(left_border)
all_sprites_list.add(right_border)

# Set up the initial position and speed of the square
# square_size = 50
# square_x = (screen_width - square_size) // 2
# square_y = (screen_height - square_size) // 2
speed = 5

# Text font
font = pygame.font.Font('freesansbold.ttf', 32)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False
    
    # Key presses handling
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False
         
    if keys[pygame.K_LEFT]:
        chest.rect.x += speed
        if not square.rect.x < 0:
            square.rect.x -= speed
    
    if keys[pygame.K_RIGHT]:
        chest.rect.x -= speed
        if not square.rect.x > (screen_width - square_size):
            square.rect.x += speed
    
    if keys[pygame.K_UP]:
        chest.rect.y += speed
        if not square.rect.y < 0:
            square.rect.y -= speed
    
    if keys[pygame.K_DOWN]:
        chest.rect.y -= speed
        if not square.rect.y > (screen_height - square_size):
            square.rect.y += speed

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw the red square
    # pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))
    all_sprites_list.draw(screen)

    # Write square position
    # text = font.render(f"X: {str(chest.rect.x)} - Y: {str(chest.rect.y)}", True, WHITE, BLACK)
    # textRect = text.get_rect()
    # textRect.center = (screen_height // 2, screen_width // 2)
    # screen.blit(text, textRect)
    # Clicking event

    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        clicked_sprites = [s for s in all_sprites_list if s.rect.collidepoint(pos)]

        if len(clicked_sprites) > 0:
            click_text = font.render("CLICKED", True, WHITE, BLACK)
        else:
            click_text = font.render("NOT CLICKED", True, WHITE, BLACK)
        
        click_textRect = click_text.get_rect()
        click_textRect.center = (screen_height // 2, screen_width // 2)
        screen.blit(click_text, click_textRect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()