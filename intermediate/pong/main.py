import pygame
import sys
from menu import PongMenu
from game import PongGame, PongGameAI
from utility import fade_in

# Global constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
LIGHT_GRAY = (150, 150, 150)  # Hover color
BLUE = (0, 0, 255)
FPS = 60

def main():
    pygame.init()

    # Initialize screen and font
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong Game")
    font = pygame.font.Font(None, 50)

    run = True  # Controls the whole program

    while run:
        # Show the menu and get the selected game mode
        menu = PongMenu(screen, font, WIDTH, HEIGHT, BLACK, WHITE, GRAY, LIGHT_GRAY, BLUE)
        game_mode = menu.run()

        if game_mode in ["2p", "ai"]:
            fade_in(screen, WIDTH, HEIGHT, BLACK)  # Fade-in before starting the game

            if game_mode == "2p":
                game = PongGame(screen, WIDTH, HEIGHT, BLACK, WHITE, FPS)
            else:
                game = PongGameAI(screen, WIDTH, HEIGHT, BLACK, WHITE, FPS)

        # Run the selected game mode
        result = game.run()

        if result == "quit":  # If the user chooses to quit
            run = False  # Exit the main loop
        elif result == "menu":  # If the user presses ESC or clicks "Back"
            continue  # Restart the loop and return to the menu

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()