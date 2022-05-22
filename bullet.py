import pygame

class Bullet:
    def __init__(self, x, y, direction, type):
        self.speed = 15
        self.x = x
        self.y = y
        self.direction = direction
        self.type = type

    def update_positive(self):
        self.x += self.speed
    
    def update_negative(self):
        self.x -= self.speed
    
    def draw(self):
        bullet = pygame.image.load(self.image)
        self.win.blit(bullet, (self.x, self.y))
