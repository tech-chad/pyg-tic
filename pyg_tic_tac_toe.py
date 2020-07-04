# tic tac toe game using pygame
import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
GRID_COLOR = (128, 128, 180)
X_COLOR = (190, 0, 255)
O_COLOR = (0, 255, 128)
WINNER_COLOR = (255, 255, 255)
STALEMATE_COLOR = (255, 0, 0)
GAME_OVER_COLOR = (255, 0, 0)
POS_DICT = {1: (67, 67), 2: (202, 67), 3: (337, 67),
            4: (67, 202), 5: (202, 202), 6: (337, 202),
            7: (67, 337), 8: (202, 337), 9: (337, 337)}


def draw_grid(win: pygame.Surface) -> None:
    pygame.draw.line(win, GRID_COLOR, (135, 10), (135, 390))
    pygame.draw.line(win, GRID_COLOR, (265, 10), (265, 390))
    pygame.draw.line(win, GRID_COLOR, (10, 135), (390, 135))
    pygame.draw.line(win, GRID_COLOR, (10, 265), (390, 265))


def draw_x(win: pygame.Surface, x: int, y: int) -> None:
    pygame.draw.line(win, X_COLOR, (x - 40, y - 40), (x + 40, y + 40))
    pygame.draw.line(win, X_COLOR, (x - 40, y + 40), (x + 40, y - 40))


def draw_o(win: pygame.Surface, x: int, y: int) -> None:
    pygame.draw.circle(win, O_COLOR, (x, y), 48, 1)


def get_grid_location(x: int, y: int) -> int:
    if 10 <= x <= 132 and 10 <= y <= 135:
        return 1
    elif 135 <= x <= 263 and 10 <= y <= 135:
        return 2
    elif 266 <= x <= 390 and 10 <= y <= 135:
        return 3
    elif 10 <= x <= 132 and 135 <= y <= 263:
        return 4
    elif 135 <= x <= 263 and 135 <= y <= 263:
        return 5
    elif 266 <= x <= 390 and 135 <= y <= 263:
        return 6
    elif 10 <= x <= 132 and 266 <= y <= 390:
        return 7
    elif 135 <= x <= 263 and 266 <= y <= 390:
        return 8
    elif 266 <= x <= 390 and 266 <= y <= 390:
        return 9


def check_for_winner(game_board: list) -> str:
    for i in range(0, 9, 3):
        if game_board[i] == game_board[i + 1] == game_board[i + 2] == "X":
            return "X"
        elif game_board[i] == game_board[i + 1] == game_board[i + 2] == "O":
            return "O"
    for i in range(0, 3):
        if game_board[i] == game_board[i + 3] == game_board[i + 6] == "X":
            return "X"
        elif game_board[i] == game_board[i + 3] == game_board[i + 6] == "O":
            return "O"
    if game_board[0] == game_board[4] == game_board[8] == "X":
        return "X"
    elif game_board[0] == game_board[4] == game_board[8] == "O":
        return "O"
    if game_board[2] == game_board[4] == game_board[6] == "X":
        return "X"
    elif game_board[2] == game_board[4] == game_board[6] == "O":
        return "O"

    for cell in game_board:
        if cell == "":
            return "No"
    else:
        return "Stalemate"


def main_menu(win: pygame.Surface) -> str:
    font = pygame.font.SysFont('comicsans', 60, False)
    play_string = font.render("PLAY", 1, (0, 0, 0))
    quit_string = font.render("QUIT", 1, (0, 0, 0))
    state = "quit"
    run = True
    win.fill((0, 0, 0))
    while run:
        pygame.draw.rect(win, (255, 255, 255), (100, 50, 200, 75))
        pygame.draw.rect(win, (255, 255, 255), (100, 250, 200, 75))
        win.blit(play_string, (150, 70))
        win.blit(quit_string, (150, 270))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = "quit"
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 100 <= mouse_x <= 300 and 50 <= mouse_y <= 150:
                    state = "play"
                    run = False
                elif 100 <= mouse_x <= 300 and 250 <= mouse_y <= 350:
                    state = "quit"
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                state = "play"
                run = False
            elif keys[pygame.K_q]:
                state = "quit"
                run = False

        pygame.display.update()

    win.fill((0, 0, 0))
    pygame.display.update()
    return state


def game_loop(win: pygame.Surface) -> None:
    font = pygame.font.SysFont('comicsans', 60, False)
    player_x = font.render("Player X Turn", 1, X_COLOR)
    player_o = font.render("Player O Turn", 1, O_COLOR)
    x_winner = font.render("Player X WINS!!", 1, WINNER_COLOR)
    o_winner = font.render("Player O WINS!!", 1, WINNER_COLOR)
    stalemate = font.render("Stalemate", 1, STALEMATE_COLOR)
    game_over = font.render("Game Over", 1, GAME_OVER_COLOR)

    game_board = ["" for _ in range(9)]
    turn = 0
    run = True
    state = "playing"

    while run:
        draw_grid(win)
        if turn == 0:
            pygame.draw.rect(win, (0, 0, 0), (40, 400, 300, 80))
            win.blit(player_x, (60, 420))
        elif turn == 1:
            pygame.draw.rect(win, (0, 0, 0), (40, 400, 300, 80))
            win.blit(player_o, (60, 420))

        winner = check_for_winner(game_board)
        if winner == "No":
            pass
        else:
            pygame.draw.rect(win, (0, 0, 0), (40, 400, 300, 90))
            win.blit(game_over, (85, 400))
            state = "game over"
            if winner == "X":
                win.blit(x_winner, (43, 450))
            elif winner == "O":
                win.blit(o_winner, (43, 450))
            elif winner == "Stalemate":
                win.blit(stalemate, (98, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and state == "playing":
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_pos = get_grid_location(mouse_x, mouse_y)
                if grid_pos:
                    if turn == 0 and game_board[grid_pos - 1] == "":
                        draw_x(win, *POS_DICT[grid_pos])
                        game_board[grid_pos - 1] = "X"
                        turn = 1
                    elif turn == 1 and game_board[grid_pos - 1] == "":
                        draw_o(win, *POS_DICT[grid_pos])
                        game_board[grid_pos - 1] = "O"
                        turn = 0
            if event.type == pygame.MOUSEBUTTONDOWN and state == "game over":
                run = False

        pygame.display.update()


def main() -> None:
    pygame.init()
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")

    while True:
        value = main_menu(win)
        if value == "play":
            game_loop(win)
        elif value == "quit":
            break


if __name__ == "__main__":
    main()
