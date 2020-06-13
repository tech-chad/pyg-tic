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

    while run:
        draw_grid(win)
        if turn == 0:
            pygame.draw.rect(win, (0, 0, 0), (40, 400, 300, 80))
            win.blit(player_x, (60, 420))
        elif turn == 1:
            pygame.draw.rect(win, (0, 0, 0), (40, 400, 300, 80))
            win.blit(player_o, (60, 420))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
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
        state = check_for_winner(game_board)
        if state == "No":
            pass
        else:
            pygame.draw.rect(win, (0, 0, 0), (40, 400, 300, 90))
            win.blit(game_over, (85, 400))
            if state == "X":
                win.blit(x_winner, (43, 450))
            elif state == "O":
                win.blit(o_winner, (43, 450))
            elif state == "Stalemate":
                win.blit(stalemate, (98, 450))

        pygame.display.update()


def main() -> None:
    pygame.init()
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    game_loop(win)


if __name__ == "__main__":
    main()
