import pygame
import sys

class PongMenu:
    def __init__(self, screen, font, width, height, bg_color, text_color, button_color, hover_color, title_color):
        """Initialize Pygame and set up the main menu screen."""
        self.screen = screen
        self.font = font
        self.WIDTH = width
        self.HEIGHT = height
        self.BG_COLOR = bg_color
        self.TEXT_COLOR = text_color
        self.BUTTON_COLOR = button_color
        self.HOVER_COLOR = hover_color
        self.TITLE_COLOR = title_color

        # Buttons
        self.button_1p = pygame.Rect(self.WIDTH // 2 - 130, self.HEIGHT // 2 - 40, 260, 60)
        self.button_2p = pygame.Rect(self.WIDTH // 2 - 100, self.HEIGHT // 2 + 40, 200, 60)
        self.button_3p = pygame.Rect(self.WIDTH // 2 - 70, self.HEIGHT // 2 + 120, 140, 60)

    def draw_text(self, text, x, y, color):
        """Render text on the screen."""
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def run(self):
        """Display the menu with clickable buttons and hover effects."""
        while True:
            self.screen.fill(self.BG_COLOR)
            self.draw_text("Pong Game", self.WIDTH // 2, self.HEIGHT // 4, self.TITLE_COLOR)

            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Change button color on hover
            color_1p = self.HOVER_COLOR if self.button_1p.collidepoint(mouse_x, mouse_y) else self.BUTTON_COLOR
            color_2p = self.HOVER_COLOR if self.button_2p.collidepoint(mouse_x, mouse_y) else self.BUTTON_COLOR
            color_3p = self.HOVER_COLOR if self.button_3p.collidepoint(mouse_x, mouse_y) else self.BUTTON_COLOR

            # Draw buttons
            pygame.draw.rect(self.screen, color_1p, self.button_1p)
            pygame.draw.rect(self.screen, color_2p, self.button_2p)
            pygame.draw.rect(self.screen, color_3p, self.button_3p)

            # Draw button text
            self.draw_text("1 Player (vs AI)", self.WIDTH // 2, self.HEIGHT // 2 - 10, self.TEXT_COLOR)
            self.draw_text("2 Players", self.WIDTH // 2, self.HEIGHT // 2 + 70, self.TEXT_COLOR)
            self.draw_text("QUIT", self.WIDTH // 2, self.HEIGHT // 2 + 150, self.TEXT_COLOR)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_1p.collidepoint(mouse_x, mouse_y):
                        return "ai"
                    if self.button_2p.collidepoint(mouse_x, mouse_y):
                        return "2p"
                    if self.button_3p.collidepoint(mouse_x, mouse_y):
                        pygame.quit()
                        sys.exit()