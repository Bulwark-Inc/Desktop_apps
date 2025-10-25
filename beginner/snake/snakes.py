import pygame
import random

class SnakeGame:
    WIDTH, HEIGHT = 600, 400
    GRID_SIZE = 10
    WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        self.wall_wrap = True
        self.reset_game()
    
    def reset_game(self):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = (self.GRID_SIZE, 0)
        self.food = self.generate_food()
        self.score = 0
        self.speed = 10
    
    def generate_food(self):
        return (random.randint(0, (self.WIDTH - self.GRID_SIZE) // self.GRID_SIZE) * self.GRID_SIZE,
                random.randint(0, (self.HEIGHT - self.GRID_SIZE) // self.GRID_SIZE) * self.GRID_SIZE)
    
    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.BLACK)
        self.screen.blit(text_surface, (x, y))
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != (0, self.GRID_SIZE):
                    self.direction = (0, -self.GRID_SIZE)
                elif event.key == pygame.K_DOWN and self.direction != (0, -self.GRID_SIZE):
                    self.direction = (0, self.GRID_SIZE)
                elif event.key == pygame.K_LEFT and self.direction != (self.GRID_SIZE, 0):
                    self.direction = (-self.GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-self.GRID_SIZE, 0):
                    self.direction = (self.GRID_SIZE, 0)
                elif event.key == pygame.K_p:
                    self.paused = not self.paused
    
    def update_snake(self):
        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        if self.wall_wrap:
            new_head = (new_head[0] % self.WIDTH, new_head[1] % self.HEIGHT)
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.food = self.generate_food()
            self.score += 10
            self.speed += 0.5
        else:
            self.snake.pop()
        if not self.wall_wrap and (new_head[0] < 0 or new_head[0] >= self.WIDTH or
                                   new_head[1] < 0 or new_head[1] >= self.HEIGHT or
                                   new_head in self.snake[1:]):
            self.running = False
    
    def draw_elements(self):
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen, self.RED, (self.food[0], self.food[1], self.GRID_SIZE, self.GRID_SIZE))
        for segment in self.snake:
            pygame.draw.rect(self.screen, self.GREEN, (segment[0], segment[1], self.GRID_SIZE, self.GRID_SIZE))
        self.draw_text(f"Score: {self.score}", 10, 10)
        if self.paused:
            self.draw_text("Paused - Press 'P' to Resume", self.WIDTH // 4, self.HEIGHT // 2)
    
    def run(self):
        while self.running:
            self.handle_events()
            if not self.paused:
                self.update_snake()
            self.draw_elements()
            pygame.display.flip()
            self.clock.tick(self.speed)
        
        self.game_over()
    
    def game_over(self):
        self.screen.fill(self.WHITE)
        self.draw_text(f"Game Over! Final Score: {self.score}", self.WIDTH // 4, self.HEIGHT // 2)
        pygame.display.flip()
        pygame.time.delay(3000)
        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
