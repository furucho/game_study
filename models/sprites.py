import pygame

class Sprite(pygame.sprite.Sprite):
     def __init__(self, color, height, width):
          super().__init__()

          self.image = pygame.Surface([width, height])

          pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

          self.rect = self.image.get_rect()