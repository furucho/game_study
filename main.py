import pygame
import sys
import constants
from models import Border, Sprite

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((constants.SCREEN["width"], constants.SCREEN["height"]))
pygame.display.set_caption("Pygame Sample")

# Sprite list
all_sprites_list = pygame.sprite.Group()

# Square Sprite
square_size = 50
square = pygame.sprite.Sprite()
square.image = pygame.Surface((square_size, square_size))
square.image.fill(constants.RED)
square.rect = pygame.Rect(*screen.get_rect().center, square_size, square_size)
all_sprites_list.add(square)

horizontal_border_height = 10
horizontal_border_width = constants.SCREEN["width"]
vertical_border_height = constants.SCREEN["height"]
vertical_border_width = 10

border = Border()
upper_border = border.create(horizontal_border_height, horizontal_border_width, constants.BORDER, 0, 0)
bottom_border = border.create(horizontal_border_height, horizontal_border_width, constants.BORDER, 0, constants.SCREEN["height"] - horizontal_border_height)
left_border = border.create(vertical_border_height, vertical_border_width, constants.BORDER, 0, 0)
right_border = border.create(vertical_border_height, vertical_border_width, constants.BORDER, constants.SCREEN["width"] - vertical_border_width, 0)

all_sprites_list.add(upper_border)
all_sprites_list.add(bottom_border)
all_sprites_list.add(left_border)
all_sprites_list.add(right_border)

## Drawing the layout
# Inside rock
rock_size = 10
# rock = Sprite(constants.WHITE, rock_size, rock_size)
# rock.rect.x = 200
# rock.rect.y = 200
rock = pygame.sprite.Sprite()
rock.image = pygame.Surface((rock_size, rock_size))
rock.image.fill(constants.WHITE)
rock.rect = pygame.Rect(200, 200, rock_size, rock_size)
all_sprites_list.add(rock)

# Chest Sprite
chest_size = 50
chest = Sprite(constants.GREEN, chest_size, chest_size)
chest.rect.x = 50
chest.rect.y = 50
all_sprites_list.add(chest)

# Text font
font = pygame.font.Font('freesansbold.ttf', 32)

def ajust_collision(floor_objects, axis, increment_value):
    if pygame.sprite.spritecollide(square, floor_objects, False):
        collided = True
        while collided:
            setattr(square.rect, axis, getattr(square.rect, axis) + increment_value)
            if not pygame.sprite.spritecollide(square, floor_objects, False):
                collided = False

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
        if not (square.rect.x - vertical_border_width) <= 0:
            square.rect.x -= constants.SPEED
            ajust_collision(floor_objects=[chest, rock], axis="x", increment_value=1)

    if keys[pygame.K_RIGHT]:
        if not (square.rect.x + vertical_border_width) >= (constants.SCREEN["width"] - square_size):
            square.rect.x += constants.SPEED
            ajust_collision(floor_objects=[chest, rock], axis="x", increment_value=-1)

    if keys[pygame.K_UP]:
        if not (square.rect.y - horizontal_border_height) <= 0:
            square.rect.y -= constants.SPEED
            ajust_collision(floor_objects=[chest, rock], axis="y", increment_value=1)

    if keys[pygame.K_DOWN]:
        if not (square.rect.y + horizontal_border_height) >= (constants.SCREEN["height"] - square_size):
            square.rect.y += constants.SPEED
            ajust_collision(floor_objects=[chest, rock], axis="y", increment_value=-1)

    # Fill the screen with black color
    screen.fill(constants.BLACK)

    # Draw the red square
    # pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))
    all_sprites_list.draw(screen)

    # Write square position
    # text = font.render(f"X: {screen.get_rect().center}", True, constants.WHITE, constants.BLACK)
    # textRect = text.get_rect()
    # textRect.center = (constants.SCREEN["height"] // 2, constants.SCREEN["width"] // 2)
    # screen.blit(text, textRect)
    # Clicking event

    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        clicked_sprites = [s for s in all_sprites_list if s.rect.collidepoint(pos)]

        if len(clicked_sprites) > 0:
            click_text = font.render("CLICKED", True, constants.WHITE, constants.BLACK)
        else:
            click_text = font.render("NOT CLICKED", True, constants.WHITE, constants.BLACK)
        
        click_textRect = click_text.get_rect()
        click_textRect.center = (constants.SCREEN["height"] // 2, constants.SCREEN["width"] // 2)
        screen.blit(click_text, click_textRect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()