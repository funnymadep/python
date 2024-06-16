# coding=utf-8
import pygame
import time
import random

pygame.init()

# 定义屏幕大小
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('snake')

# 设置颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# 设置蛇的初始位置和大小
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

# 定义字体
font_style = pygame.font.SysFont(None, 25)

def message(msg, color, y_displace=0):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3 + y_displace])

def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red, -50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for block in snake_List:
            pygame.draw.rect(screen, white, [block[0], block[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def show_help():
    help_open = True
    while help_open:
        screen.fill(black)
        message("help:", white, -100)
        message("press ↑↓←→ to choose direction", white, -50)
        message("press q to quit game", white, 0)
        message("press c restart game", white, 50)
        message("press b return menu", white, 100)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    help_open = False

def main_menu():
    menu_open = True
    while menu_open:
        screen.fill(black)
        message("snake", white, -100)
        message("press s start", white, -50)
        message("press h help", white, 0)
        message("press q quit", white, 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    gameLoop()
                if event.key == pygame.K_h:
                    show_help()
                if event.key == pygame.K_q:
                    menu_open = False

    pygame.quit()
    quit()

main_menu()
