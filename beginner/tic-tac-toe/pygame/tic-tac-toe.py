import pygame
import sys

class TicTacToe:
    WIDTH, HEIGHT = 600, 600
    LINE_WIDTH = 10
    BOARD_ROWS = 3
    BOARD_COLS = 3
    SQUARE_SIZE = WIDTH // BOARD_COLS
    CIRCLE_RADIUS = SQUARE_SIZE // 3
    CIRCLE_WIDTH = 10
    CROSS_WIDTH = 15
    SPACE = SQUARE_SIZE // 4
    
    BG_COLOR = (28, 170, 156)
    LINE_COLOR = (23, 145, 135)
    CIRCLE_COLOR = (239, 231, 200)
    CROSS_COLOR = (66, 66, 66)
    TEXT_COLOR = (255, 255, 255)
    
    pygame.font.init()
    FONT = pygame.font.Font(None, 50)
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")
        self.screen.fill(self.BG_COLOR)
        
        self.board = [[None] * self.BOARD_COLS for _ in range(self.BOARD_ROWS)]
        self.scores = {"X": 0, "O": 0}
        self.current_player = "X"
        self.game_over = False
        
        self.click_sound = pygame.mixer.Sound("sounds/click.wav")
        self.win_sound = pygame.mixer.Sound("sounds/win.wav")
        
        self.draw_lines()
    
    def draw_lines(self):
        for i in range(1, self.BOARD_ROWS):
            pygame.draw.line(self.screen, self.LINE_COLOR, (0, i * self.SQUARE_SIZE), (self.WIDTH, i * self.SQUARE_SIZE), self.LINE_WIDTH)
            pygame.draw.line(self.screen, self.LINE_COLOR, (i * self.SQUARE_SIZE, 0), (i * self.SQUARE_SIZE, self.HEIGHT), self.LINE_WIDTH)
    
    def draw_figures(self):
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLS):
                if self.board[row][col] == "O":
                    pygame.draw.circle(self.screen, self.CIRCLE_COLOR, (int(col * self.SQUARE_SIZE + self.SQUARE_SIZE / 2), int(row * self.SQUARE_SIZE + self.SQUARE_SIZE / 2)), self.CIRCLE_RADIUS, self.CIRCLE_WIDTH)
                elif self.board[row][col] == "X":
                    pygame.draw.line(self.screen, self.CROSS_COLOR, (col * self.SQUARE_SIZE + self.SPACE, row * self.SQUARE_SIZE + self.SPACE), (col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE, row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE), self.CROSS_WIDTH)
                    pygame.draw.line(self.screen, self.CROSS_COLOR, (col * self.SQUARE_SIZE + self.SPACE, row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE), (col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE, row * self.SQUARE_SIZE + self.SPACE), self.CROSS_WIDTH)
    
    def draw_winner_message(self, screen, font, winner):
        if winner == "X" or winner == "O":
            message = f"Player {winner} Wins!"
        else:
            message = "It's a Draw!"
        
        text = font.render(message, True, (255, 255, 0))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        
        # Draw a semi-transparent rectangle as a background for the text
        overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))  # Black with transparency
        screen.blit(overlay, (0, 0))

        # Draw the message text
        screen.blit(text, text_rect)
        pygame.display.flip()

        # Pause for a short duration before restarting
        pygame.time.delay(2000)

    def mark_square(self, row, col):
        self.board[row][col] = self.current_player
    
    def available_square(self, row, col):
        return self.board[row][col] is None
    
    def is_board_full(self):
        return all(self.board[row][col] is not None for row in range(self.BOARD_ROWS) for col in range(self.BOARD_COLS))
    
    def check_winner(self):
        pos = None
        for row in range(self.BOARD_ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] is not None:
                self.win_sound.play()
                pos = ((20, row*self.SQUARE_SIZE+self.SQUARE_SIZE//2), (self.WIDTH-20, row*self.SQUARE_SIZE+self.SQUARE_SIZE//2))
                return self.board[row][0], pos
        
        for col in range(self.BOARD_COLS):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                self.win_sound.play()
                pos = ((col*self.SQUARE_SIZE+self.SQUARE_SIZE//2, 20), (col*self.SQUARE_SIZE+self.SQUARE_SIZE//2, self.HEIGHT-20))
                return self.board[0][col], pos
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            self.win_sound.play()
            pos = ((20, 20), (self.WIDTH-20, self.HEIGHT-20))
            return self.board[0][0], pos
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            self.win_sound.play()
            pos = ((self.WIDTH-20, 20), (20, self.HEIGHT-20))
            return self.board[0][2], pos
        
        return None
    
    def restart_game(self):
        self.board = [[None] * self.BOARD_COLS for _ in range(self.BOARD_ROWS)]
        self.screen.fill(self.BG_COLOR)
        self.draw_lines()
        self.game_over = False
        self.current_player = "X"
    
    def draw_score(self):
        score_text = self.FONT.render(f"X: {self.scores['X']}  O: {self.scores['O']}", True, self.TEXT_COLOR)
        self.screen.blit(score_text, (20, 20))

    def draw_winning_line(self, screen, start_pos, end_pos):
        pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 10)
        pygame.display.flip()

    def draw_screen(self, player_win, pos):
        self.screen.fill(self.BG_COLOR)
        self.draw_lines()
        self.draw_figures()
        if player_win:
            self.draw_winning_line(self.screen, pos[0], pos[1])
            self.draw_winner_message(self.screen, self.FONT, player_win)
        self.draw_score()
        pygame.display.update()
            
    # mainloop
    def main(self):
        run = True
        while run:
            player_win = None
            pos = None
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    run = False
                
                # check to restart if R is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart_game()

                # mark square of mouse button clicked on square
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    self.click_sound.play()
                    col = event.pos[0] // self.SQUARE_SIZE
                    row = event.pos[1] // self.SQUARE_SIZE
                    if self.available_square(row, col):
                        self.mark_square(row, col)
                        winner = self.check_winner()
                        if winner:
                            self.scores[winner[0]] += 1
                            player_win = winner[0]
                            pos = winner[1]
                            self.game_over = True
                        elif self.is_board_full():
                            player_win = "Z"
                            self.restart_game()
                        else:
                            self.current_player = "O" if self.current_player == "X" else "X"
            
            self.draw_screen(player_win, pos)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = TicTacToe()
    game.main()
