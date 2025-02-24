import pygame

def fade_in(screen, WIDTH, HEIGHT, color, duration=500):
    """Creates a fade-in effect when switching screens."""
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(color)
    
    for alpha in range(0, 255, 5):  # Gradually increase opacity
        fade_surface.set_alpha(alpha)
        screen.fill(color)  # Keep background color
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(duration // 50)  # Control speed of fade

def fade_out(screen, WIDTH, HEIGHT, color, duration=500):
    """Creates a fade-out effect when leaving the game."""
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(color)

    for alpha in range(255, 0, -5):  # Gradually decrease opacity
        fade_surface.set_alpha(alpha)
        screen.fill(color)  # Keep background color
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(duration // 50)  # Control speed of fade
