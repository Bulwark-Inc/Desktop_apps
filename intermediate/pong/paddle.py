import pygame

class Paddle:
    def __init__(self, x, y, width=10, height=100, speed=5):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self, keys, up_key, down_key, screen_height):
        """Moves the paddle up or down based on key presses."""
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < screen_height:
            self.rect.y += self.speed

    def draw(self, screen, color=(255, 255, 255)):
        """Draws the paddle on the screen."""
        pygame.draw.rect(screen, color, self.rect)
