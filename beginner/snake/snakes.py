import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 10
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Font setup
font = pygame.font.Font(None, 36)

# Snake setup
snake = [(100, 100), (90, 100), (80, 100)]
direction = (GRID_SIZE, 0)

# Food setup
food = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
        random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

# Game variables
score = 0
speed = 10  # Initial speed
running = True
paused = False
wall_wrap = True  # Change to True if you want the snake to wrap around the screen

clock = pygame.time.Clock()

# Function to display text
def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Game loop
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)
            elif event.key == pygame.K_p:  # Pause the game
                paused = not paused

    if not paused:
        # Move snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Wall wrap feature
        if wall_wrap:
            new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)

        snake.insert(0, new_head)

        # Check collision with food
        if new_head == food:
            food = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                    random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
            score += 10  # Increase score
            speed += 0.5  # Increase speed gradually
        else:
            snake.pop()  # Remove last segment

        # Check collision with walls or itself
        if not wall_wrap and (new_head[0] < 0 or new_head[0] >= WIDTH or
                              new_head[1] < 0 or new_head[1] >= HEIGHT or
                              new_head in snake[1:]):
            running = False  # Game over

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Display score
    draw_text(f"Score: {score}", 10, 10)
    if paused:
        draw_text("Paused - Press 'P' to Resume", WIDTH // 4, HEIGHT // 2)

    pygame.display.flip()
    clock.tick(speed)  # Snake speed increases as score goes up

# Game over message
screen.fill(WHITE)
draw_text(f"Game Over! Final Score: {score}", WIDTH // 4, HEIGHT // 2)
pygame.display.flip()
pygame.time.delay(3000)  # Display message for 3 seconds before quitting

pygame.quit()
