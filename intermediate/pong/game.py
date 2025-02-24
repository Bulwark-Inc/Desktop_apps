import pygame
import random
from paddle import Paddle
from ball import Ball
from utility import fade_out

class PongGame:
    def __init__(self, screen, width, height, bg_color, text_color, fps):
        """Initialize the Pong game with dependencies passed from main."""
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.BG_COLOR = bg_color
        self.TEXT_COLOR = text_color
        self.FPS = fps
        self.paused = False

        # Load sound effects
        self.hit_sound = pygame.mixer.Sound("sounds/hit.wav")
        self.score_sound = pygame.mixer.Sound("sounds/score.wav")

        # Game objects
        paddle_width, paddle_height = 10, 100
        ball_radius = 10

        self.player1 = Paddle(20, self.HEIGHT // 2 - paddle_height // 2)
        self.player2 = Paddle(self.WIDTH - 30, self.HEIGHT // 2 - paddle_height // 2)
        self.ball = Ball(self.WIDTH // 2, self.HEIGHT // 2, radius=ball_radius)

        # Game variables
        self.running = True
        self.clock = pygame.time.Clock()
        self.player1_score = 0
        self.player2_score = 0
        self.font = pygame.font.Font(None, 36)

        # Ball speed control
        self.default_speed_x = self.ball.speed_x
        self.default_speed_y = self.ball.speed_y

    def handle_events(self):
        """Handles user input, quitting, pause, and menu navigation."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return "quit"
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Back to Main Menu
                    self.running = False
                    return "menu"    # Signal to return to menu
                elif event.key == pygame.K_p:  # Pause game
                    self.paused = not self.paused

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.back_button.collidepoint(x, y):  # Back Button Clicked
                    self.running = False
                    return "menu"  
                elif self.pause_button.collidepoint(x, y):  # Pause Button Clicked
                    self.paused = not self.paused
            
        return None # Default return

    def update(self):
        """Updates the game state, including paddle and ball movements."""
        keys = pygame.key.get_pressed()
        self.player1.move(keys, pygame.K_w, pygame.K_s, self.HEIGHT)
        self.player2.move(keys, pygame.K_UP, pygame.K_DOWN, self.HEIGHT)
        self.ball.move(self.WIDTH, self.HEIGHT)

        # Ball collision with paddles
        if self.ball.rect.colliderect(self.player1.rect):
            self.ball.bounce_off_paddle(self.player1)
            self.hit_sound.play()

        elif self.ball.rect.colliderect(self.player2.rect):
            self.ball.bounce_off_paddle(self.player2)
            self.hit_sound.play()

        # Scoring system
        if self.ball.rect.left <= 0:  # Player 2 scores
            self.player2_score += 1
            self.ball.reset(self.WIDTH // 2, self.HEIGHT // 2)
            self.ball.speed_x = self.default_speed_x  # Reset speed
            self.ball.speed_y = self.default_speed_y
            self.score_sound.play()

        elif self.ball.rect.right >= self.WIDTH:  # Player 1 scores
            self.player1_score += 1
            self.ball.reset(self.WIDTH // 2, self.HEIGHT // 2)
            self.ball.speed_x = self.default_speed_x  # Reset speed
            self.ball.speed_y = self.default_speed_y
            self.score_sound.play()

    def draw(self):
        """Renders the game objects and UI elements."""
        self.screen.fill(self.BG_COLOR)

        # Draw paddles, ball, and score
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        self.ball.draw(self.screen)

        # Display score
        score_text = self.font.render(f"{self.player1_score} - {self.player2_score}", True, self.TEXT_COLOR)
        self.screen.blit(score_text, (self.WIDTH // 2 - 20, 20))

        # Draw Back Button
        self.back_button = pygame.Rect(10, 10, 100, 40)  # Position and size
        pygame.draw.rect(self.screen, (255, 0, 0), self.back_button)
        back_text = self.font.render("Back", True, (255, 255, 255))
        self.screen.blit(back_text, (20, 15))

        # Draw Pause Button
        self.pause_button = pygame.Rect(self.WIDTH - 110, 10, 100, 40)
        pygame.draw.rect(self.screen, (0, 255, 0), self.pause_button)
        pause_text = self.font.render("Pause" if not self.paused else "Resume", True, (255, 255, 255))
        self.screen.blit(pause_text, (self.WIDTH - 100, 15))

        pygame.display.flip()

    def run(self):
        """Main game loop."""
        while self.running:
            result = self.handle_events()
            if result:  # If ESC was pressed or quit requested
                if result == "menu":
                    fade_out(self.screen, self.WIDTH, self.HEIGHT, self.BG_COLOR)  # Fade-out before returning to menu
                return result
            
            if not self.paused:  # Only update when not paused
                self.update()

            self.draw()
            self.clock.tick(self.FPS)
        
        fade_out(self.screen, self.WIDTH, self.HEIGHT, self.BG_COLOR)  # Ensure fade-out on exit
        return "menu"  # Default return to menu if loop exits

class PongGameAI(PongGame):
    def __init__(self, screen, width, height, bg_color, text_color, fps):
        """Initialize Pong game with AI opponent."""
        super().__init__(screen, width, height, bg_color, text_color, fps)
        self.ai_speed = 5

    def update(self):
        """Updates the game state with AI movement and smooth collisions."""
        keys = pygame.key.get_pressed()
        self.player1.move(keys, pygame.K_w, pygame.K_s, self.HEIGHT)
        self.ai_move()  # Improved AI movement function
        self.ball.move(self.WIDTH, self.HEIGHT)

        # Ball collision with paddles
        if self.ball.rect.colliderect(self.player1.rect) or self.ball.rect.colliderect(self.player2.rect):
            self.ball.speed_x *= -1  # Reverse direction
            self.ball.speed_x *= min(1.1, 3)  # Limit speed increase
            self.ball.speed_y *= min(1.1, 3)
            self.ball.rect.x += self.ball.speed_x  # Prevent ball getting stuck
            self.hit_sound.play()

        # Scoring system
        if self.ball.rect.left <= 0:
            self.player2_score += 1
            self.reset_ball()
        elif self.ball.rect.right >= self.WIDTH:
            self.player1_score += 1
            self.reset_ball()

    def reset_ball(self):
        """Resets ball to center with controlled speed."""
        self.ball.reset(self.WIDTH // 2, self.HEIGHT // 2)
        self.ball.speed_x = self.default_speed_x * random.choice((1, -1))
        self.ball.speed_y = self.default_speed_y * random.choice((1, -1))
        self.score_sound.play()

    def ai_move(self):
        """Simple AI movement that follows the ball."""
        if self.ball.rect.centery > self.player2.rect.centery:
            self.player2.rect.y += self.ai_speed
        elif self.ball.rect.centery < self.player2.rect.centery:
            self.player2.rect.y -= self.ai_speed
