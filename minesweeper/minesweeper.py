import pygame
import random
import sys

pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('扫雷游戏')

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
gray = (192, 192, 192)
red = (255, 0, 0)

# 设置字体
font = pygame.font.SysFont(None, 25)
large_font = pygame.font.SysFont(None, 50)

# 默认网格大小和雷的数量
grid_size = 20
num_mines = 40

def create_grid(grid_size, num_mines, first_click):
    grid = [[0] * grid_size for _ in range(grid_size)]
    mines = []

    while len(mines) < num_mines:
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        if grid[x][y] == 0 and not in_safe_zone(first_click, (x, y)):
            grid[x][y] = -1
            mines.append((x, y))

    for mine in mines:
        for i in range(mine[0] - 1, mine[0] + 2):
            for j in range(mine[1] - 1, mine[1] + 2):
                if 0 <= i < grid_size and 0 <= j < grid_size and grid[i][j] != -1:
                    grid[i][j] += 1

    return grid

def in_safe_zone(first_click, pos):
    x, y = first_click
    px, py = pos
    return abs(x - px) <= 2 and abs(y - py) <= 2

def message(msg, color, y_displace=0, font=font):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3 + y_displace])

def game_loop(grid_size, num_mines):
    game_over = False
    first_click = True
    grid = [[0] * grid_size for _ in range(grid_size)]
    revealed = [[False] * grid_size for _ in range(grid_size)]
    flagged = [[False] * grid_size for _ in range(grid_size)]
    cell_size = min(screen_width // grid_size, screen_height // grid_size)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = x // cell_size
                col = y // cell_size
                if event.button == 1:  # 左键点击
                    if first_click:
                        grid = create_grid(grid_size, num_mines, (row, col))
                        first_click = False
                    if grid[row][col] == -1:
                        game_over = True
                    else:
                        reveal_cells(revealed, grid, row, col)
                if event.button == 3:  # 右键点击
                    flagged[row][col] = not flagged[row][col]

        screen.fill(black)
        for row in range(grid_size):
            for col in range(grid_size):
                rect = pygame.Rect(row * cell_size, col * cell_size, cell_size, cell_size)
                if revealed[row][col]:
                    pygame.draw.rect(screen, white, rect)
                    if grid[row][col] > 0:
                        text = font.render(str(grid[row][col]), True, black)
                        screen.blit(text, rect)
                else:
                    pygame.draw.rect(screen, gray, rect)
                    if flagged[row][col]:
                        pygame.draw.rect(screen, red, rect)
                pygame.draw.rect(screen, black, rect, 1)

        pygame.display.flip()

def reveal_cells(revealed, grid, row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True
    if grid[row][col] == 0:
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                    reveal_cells(revealed, grid, i, j)

def show_help():
    help_open = True
    while help_open:
        screen.fill(black)
        message("help:", white, -100, large_font)
        message("use mouse left clicked", white, -50)
        message("use mouse right flag", white, 0)
        message("press b return menu", white, 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    help_open = False

def choose_difficulty():
    choose_open = True
    while choose_open:
        screen.fill(black)
        message("choose diffcultly:", white, -100, large_font)
        message("1. simple (20x20)", white, -50)
        message("2. medium (50x50)", white, 0)
        message("3. hard (100x100)", white, 50)
        message("press1,2 or 3", white, 100)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 20, 40
                if event.key == pygame.K_2:
                    return 50, 250
                if event.key == pygame.K_3:
                    return 100, 1000

def main_menu():
    menu_open = True
    global grid_size, num_mines
    while menu_open:
        screen.fill(black)
        message("minesweeper", white, -100, large_font)
        message("press s start", white, -50)
        message("press h help", white, 0)
        message("press d choose diffcultly", white, 50)
        message("press q quit", white, 100)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_loop(grid_size, num_mines)
                if event.key == pygame.K_h:
                    show_help()
                if event.key == pygame.K_d:
                    grid_size, num_mines = choose_difficulty()
                if event.key == pygame.K_q:
                    menu_open = False

    pygame.quit()
    sys.exit()

main_menu()
