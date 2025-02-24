import pygame
import random
import math

class Ball:
    def __init__(self, x, y, radius=10, speed_x=5, speed_y=5):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.radius = radius
        self.speed_x = speed_x * random.choice((1, -1))  # Randomize initial direction
        self.speed_y = speed_y * random.choice((1, -1))
        self.max_speed = 8

    def move(self, screen_width, screen_height):
        """Moves the ball and ensures accurate bouncing off walls."""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off the top and bottom walls
        if self.rect.top < 0:  # Hits top wall
            self.rect.top = 0  # Correct position
            self.speed_y *= -1  # Reverse direction

        elif self.rect.bottom > screen_height:  # Hits bottom wall
            self.rect.bottom = screen_height  # Correct position
            self.speed_y *= -1  # Reverse direction

    def bounce_off_paddle(self, paddle):
        """Adjusts ball angle and speed based on paddle collision."""
        paddle_center = paddle.rect.centery
        ball_center = self.rect.centery
        distance_from_center = ball_center - paddle_center
        max_bounce_angle = 45  # Max bounce angle in degrees

        # Normalize distance (-1 to 1) relative to paddle height
        normalized_dist = distance_from_center / (paddle.rect.height / 2)

        # Calculate bounce angle
        bounce_angle = normalized_dist * max_bounce_angle
        angle_radians = math.radians(bounce_angle)

        # Adjust speed based on impact position
        if abs(normalized_dist) < 0.2:  # Near center
            self.speed_x *= 0.9  # Slow down slightly
        elif abs(normalized_dist) > 0.7:  # Near edge
            self.speed_x *= 1.2  # Speed up more

        # Ensure speed is within limits
        self.speed_x = min(max(self.speed_x, -self.max_speed), self.max_speed)
        self.speed_y = min(max(self.speed_y, -self.max_speed), self.max_speed)

        # Change direction
        self.speed_x = abs(self.speed_x) * (-1 if self.speed_x > 0 else 1)
        self.speed_y = self.speed_x * math.tan(angle_radians)

    def reset(self, x, y):
        """Resets the ball to the center."""
        self.rect.x = x - self.radius
        self.rect.y = y - self.radius
        self.speed_x *= random.choice((1, -1))  # Randomize new direction
        self.speed_y *= random.choice((1, -1))

    def draw(self, screen, color=(255, 255, 255)):
        """Draws the ball on the screen."""
        pygame.draw.ellipse(screen, color, self.rect)
