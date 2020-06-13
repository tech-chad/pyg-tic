# tic tac toe game using pygame
import pygame

from typing import Tuple

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
GRID_COLOR = (128, 128, 180)
X_COLOR = (190, 0, 255)
O_COLOR = (0, 255, 128)
POS_1 = (67, 67)
POS_2 = (202, 67)
POS_3 = (337, 67)
POS_4 = (67, 202)
POS_5 = (202, 202)
POS_6 = (337, 202)
POS_7 = (67, 337)
POS_8 = (202, 337)
POS_9 = (337, 337)


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


def get_grid_location(x: int, y: int) -> Tuple[int, int]:
    if 10 <= x <= 132 and 10 <= y <= 135:
        return POS_1
    elif 135 <= x <= 263 and 10 <= y <= 135:
        return POS_2
    elif 266 <= x <= 390 and 10 <= y <= 135:
        return POS_3
    elif 10 <= x <= 132 and 135 <= y <= 263:
        return POS_4
    elif 135 <= x <= 263 and 135 <= y <= 263:
        return POS_5
    elif 266 <= x <= 390 and 135 <= y <= 263:
        return POS_6
    elif 10 <= x <= 132 and 266 <= y <= 390:
        return POS_7
    elif 135 <= x <= 263 and 266 <= y <= 390:
        return POS_8
    elif 266 <= x <= 390 and 266 <= y <= 390:
        return POS_9


def game_loop(win: pygame.Surface) -> None:
    run = True

    while run:
        draw_grid(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_pos = get_grid_location(mouse_x, mouse_y)
                if grid_pos:
                    draw_x(win, *grid_pos)


def main() -> None:
    pygame.init()
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    # font = pygame.font.SysFont('comicsans', 26, True)
    game_loop(win)


if __name__ == "__main__":
    main()
