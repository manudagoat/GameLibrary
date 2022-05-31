#flappy bird: https://replit.com/join/wfwklubfsb-manilmehta
#checkers https://replit.com/join/mtidjaptoz-mokshverma
#Egg: https://replit.com/join/zsogcraqtn-mokshverma
#chess https://replit.com/join/lmjtzcjwnq-mokshverma
#sudoku you have
#Connect 4 is on this repl
#Coin Dash u have

import pygame
from pygame import mixer
import tkinter
import PIL
import random
from tkinter import *
from PIL import Image, ImageTk  
import numpy as np
import sys
import math
import time
from pygame import Rect
from pygame import Vector2
from math import radians, sqrt
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((0, 0))
root = Tk()
root.geometry('500x550')

image = Image.open("GUI.png")
resize_image = image.resize((500, 550))

img = ImageTk.PhotoImage(resize_image)

chess = PhotoImage(file='Chess.png')
img_label_chess = Label(image=chess)

checkers = PhotoImage(file='Checkers.png')
img_label_checkers = Label(image=checkers)

connect4 = PhotoImage(file='Connect4.png')
img_label_connect4 = Label(image=connect4)

sudoku = PhotoImage(file='Sudoku.png')
img_label_sudoku = Label(image=sudoku)

CDash = PhotoImage(file='Coin Dash.png')
img_label_makruk = Label(image=CDash)

snake = PhotoImage(file='Snake.png')
img_label_snake = Label(image=snake)

trafficfun = PhotoImage(file='TrafficFun.png')
img_label_trafficfun = Label(image=trafficfun)

spaceinvaders = PhotoImage(file='SpaceInvaders.png')
img_label_spaceinvaders = Label(image=spaceinvaders)

label1 = Label(image=img)
label1.image = img
label1.pack()

#music

music = pygame.mixer.music.load('rec room music.mp3')
pygame.mixer.music.play(-1)

#print Traffic Fun code here
def initTrafficFun():
    import pygame
    import time
    import random
    
    pygame.init()
    
    width, height = 800, 600
    backgroundColor = 225, 0, 0
    screen = pygame.display.set_mode((width, height))
    backgroundRaw = pygame.image.load("background.png")
    background = pygame.transform.scale(backgroundRaw, (800, 600))
    
    pygame.display.set_caption('Traffic Fun')
    
    score = 0
    
    speed1 = random.randrange(4, 8)
    speed2 = random.randrange(6, 10)
    speed3 = random.randrange(8, 14)
    speed4 = random.randrange(8, 12)
    
    pressed_left = False
    pressed_right = False
    
    playerX = 435
    playerY = 460
    playerRaw = pygame.image.load("PlayerCar.png")
    player = pygame.transform.scale(playerRaw, (60, 125))
    
    car1X = 435
    car1Y = -20
    car1Raw = pygame.image.load("Car1.png")
    car1 = pygame.transform.scale(car1Raw, (70, 130))
    
    car2X = 560
    car2Y = -20
    car2Raw = pygame.image.load("Car2.png")
    car2 = pygame.transform.scale(car2Raw, (70, 150))
    
    car3X = 190
    car3Y = -20
    car3Raw = pygame.image.load("Car3.png")
    car3 = pygame.transform.scale(car3Raw, (70, 150))
    car3 = pygame.transform.rotate(car3, 180)
    
    car4X = 300
    car4Y = -20
    car4Raw = pygame.image.load("Car4.png")
    car4 = pygame.transform.scale(car4Raw, (70, 150))
    car4 = pygame.transform.rotate(car4, 180)
    
    
    playerMid_X = playerX + 30
    playerMid_Y = playerY - 62.5
    car1Mid_X = car1X + 10
    car1Mid_X = car1Y - 10
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10
    
    def show_score(x, y):
        scorePrint = font.render('Score: ' + str(score), True, (0, 0, 0))
        screen.blit(scorePrint, (x, y))
    
    timeout = time.time() + 15
    
    while True:
        screen.blit(background, (0, 0))
        show_score(10, 10)
        screen.blit(player, (playerX, playerY))
        screen.blit(car2, (car2X, car2Y))
        screen.blit(car4, (car4X, car4Y))
    
        timeLeft = round(timeout - time.time(), 1)
        if timeLeft <= 10:
            screen.blit(car1, (car1X, car1Y))
            car1Y = car1Y + speed1
        if time.time() > timeout:
            screen.blit(car3, (car3X, car3Y))
            car3Y = car3Y + speed3
    
        car2Y = car2Y + speed2
        car4Y = car4Y + speed4
    
        pygame.display.flip()
        time.sleep(10 / 1000)
    
        if car1Y >= 550:
            speed1 = random.randrange(4, 8)
            car1Y = -50
            score = score + 1
        if car2Y >= 550:
            speed2 = random.randrange(6, 10)
            car2Y = -50
            score = score + 1
        if car3Y >= 550:
            speed3 = random.randrange(8, 14)
            car3Y = -50
            score = score + 1
        if car4Y >= 550:
            speed4 = random.randrange(8, 12)
            car4Y = -50
            score = score + 1
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:  # check for key presses
                if event.key == pygame.K_LEFT:  # left arrow turns left
                    pressed_left = True
                elif event.key == pygame.K_RIGHT:  # right arrow turns right
                    pressed_right = True
            elif event.type == pygame.KEYUP:  # check for key releases
                if event.key == pygame.K_LEFT:  # left arrow turns left
                    pressed_left = False
                elif event.key == pygame.K_RIGHT:  # right arrow turns right
                    pressed_right = False
    
        if pressed_left == True:
            playerX = playerX - 5
        if pressed_right == True:
            playerX = playerX + 5
    
        if playerX >= 605:
            playerX = 605
        if playerX <= 135:
            playerX = 135
    
        playerMid_X = playerX + 30
        playerMid_Y = playerY - 62.5
        car1Mid_X = car1X + 35
        car1Mid_Y = car1Y - 65
        car2Mid_X = car2X + 35
        car2Mid_Y = car2Y - 75
        car3Mid_X = car3X + 35
        car3Mid_Y = car3Y - 75
        car4Mid_X = car4X + 35
        car4Mid_Y = car4Y - 75
    
        diff1 = abs(playerMid_X - car1Mid_X)
        diff2 = abs(playerMid_Y - car1Mid_Y)
        if (diff1 <= 45) and (diff2 <= 125):
            print('Final Score:', score)
            time.sleep(5)
            break
        diff3 = abs(playerMid_X - car2Mid_X)
        diff4 = abs(playerMid_Y - car2Mid_Y)
        if (diff3 <= 55) and (diff4 <=150):
            print('Final Score:', score)
            time.sleep(5)
            break
        diff5 = abs(playerMid_X - car3Mid_X)
        diff6 = abs(playerMid_Y - car3Mid_Y)
        if (diff5 <= 55) and (diff6 <= 150):
            print('Final Score:', score)
            time.sleep(5)
            break
        diff7 = abs(playerMid_X - car4Mid_X)
        diff8 = abs(playerMid_Y - car4Mid_Y)
        if (diff7 <= 55) and (diff8 <= 150):
            print('Final Score:', score)
            time.sleep(5)
            break
    
        pygame.display.flip()
        pygame.display.update()
#print Snake code here
def initSnake():
        import pygame
        import time
        import random
        
        snake_speed = 15
        
        # Window size
        window_x = 720
        window_y = 480
        
        # defining colors
        black = pygame.Color(0, 0, 0)
        white = pygame.Color(255, 255, 255)
        red = pygame.Color(255, 0, 0)
        green = pygame.Color(0, 255, 0)
        blue = pygame.Color(0, 0, 255)
        
        # Initialising pygame
        pygame.init()
        
        # Initialise game window
        pygame.display.set_caption('Snake')
        game_window = pygame.display.set_mode((window_x, window_y))
        
        # FPS (frames per second) controller
        fps = pygame.time.Clock()
        
        # defining snake default position
        snake_position = [100, 50]
        
        # defining first 4 blocks of snake body
        snake_body = [[100, 50],
                    [90, 50],
                    [80, 50],
                    [70, 50]
                    ]
        # fruit position
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                        random.randrange(1, (window_y//10)) * 10]
        
        fruit_spawn = True
        
        # setting default snake direction towards
        # right
        direction = 'RIGHT'
        change_to = direction
        
        # initial score
        score = 0
        
        # displaying Score function
        def show_score(choice, color, font, size):
        
            # creating font object score_font
            score_font = pygame.font.SysFont(font, size)
            
            # create the display surface object
            # score_surface
            score_surface = score_font.render('Score : ' + str(score), True, color)
            
            # create a rectangular object for the text
            # surface object
            score_rect = score_surface.get_rect()
            
            # displaying text
            game_window.blit(score_surface, score_rect)
        
        # game over function
        def game_over():
        
            # creating font object my_font
            my_font = pygame.font.SysFont('times new roman', 50)
            
            # creating a text surface on which text
            # will be drawn
            game_over_surface = my_font.render(
                'Your Score is : ' + str(score), True, red)
            
            # create a rectangular object for the text
            # surface object
            game_over_rect = game_over_surface.get_rect()
            
            # setting position of the text
            game_over_rect.midtop = (window_x/2, window_y/4)
            
            # blit will draw the text on screen
            game_window.blit(game_over_surface, game_over_rect)
            pygame.display.flip()
            
            # after 2 seconds we will quit the program
            time.sleep(2)
            
            # deactivating pygame library
            pygame.quit()
            
            # quit the program
            quit()
        
        
        # Main Function
        while True:
            
            # handling key events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
        
            # If two keys pressed simultaneously
            # we don't want snake to move into two
            # directions simultaneously
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'
        
            # Moving the snake
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10
        
            # Snake body growing mechanism
            # if fruits and snakes collide then scores
            # will be incremented by 10
            snake_body.insert(0, list(snake_position))
            if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                score += 10
                fruit_spawn = False
            else:
                snake_body.pop()
                
            if not fruit_spawn:
                fruit_position = [random.randrange(1, (window_x//10)) * 10,
                                random.randrange(1, (window_y//10)) * 10]
                
            fruit_spawn = True
            game_window.fill(black)
            
            for pos in snake_body:
                pygame.draw.rect(game_window, green,
                                pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(game_window, white, pygame.Rect(
                fruit_position[0], fruit_position[1], 10, 10))
        
            # Game Over conditions
            if snake_position[0] < 0 or snake_position[0] > window_x-10:
                game_over()
            if snake_position[1] < 0 or snake_position[1] > window_y-10:
                game_over()
        
            # Touching the snake body
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over()
        
            # displaying score countinuously
            show_score(1, white, 'times new roman', 20)
        
            # Refresh game screen
            pygame.display.update()
        
            # Frame Per Second /Refresh Rate
            fps.tick(snake_speed)
#print Chess code here
def initChess():
        from chess1.game import Game

        if __name__=="__main__":
            game = Game()
            game.start_game()
#print Checkers code here
def initCheckers():
    import pygame
    from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
    from checkers.cgame import Game
    
    
    FPS = 60
    
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Checkers')
    
    def get_row_col_from_mouse(pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col
    
    def main():
        run = True
        clock = pygame.time.Clock()
        game = Game(WIN)
    
        while run:
            clock.tick(FPS)
    
            if game.winner() != None:
                print(game.winner())
                run = False
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
    
            game.update()
        
        pygame.quit()
    
    main()
#print Coin Dash code here
def initSudoku():
        import pygame
        import requests
        
        WIDTH = 550
        background_color = (251, 247, 245)
        original_grid_element_color = (52, 31, 151)
        buffer = 5
        
        response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
        grid = response.json()['board']
        grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
        
        
        def insert(win, position):
            i, j = position[1], position[0]
            myfont = pygame.font.SysFont('Comic Sans MS', 35)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN:
                        if (grid_original[i - 1][j - 1] != 0):
                            return
                        if (event.key == 48):  # checking with 0
                            grid[i - 1][j - 1] = event.key - 48
                            pygame.draw.rect(win, background_color, (
                            position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                            pygame.display.update()
                            return
                        if (0 < event.key - 48 < 10):  # We are checking for valid input
                            pygame.draw.rect(win, background_color, (
                            position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                            value = myfont.render(str(event.key - 48), True, (0, 0, 0))
                            win.blit(value, (position[0] * 50 + 15, position[1] * 50))
                            grid[i - 1][j - 1] = event.key - 48
                            pygame.display.update()
                            return
                        return
        
        
        def main():
            pygame.init()
            win = pygame.display.set_mode((WIDTH, WIDTH))
            pygame.display.set_caption("Sudoku")
            win.fill(background_color)
            myfont = pygame.font.SysFont('Comic Sans MS', 35)
        
            for i in range(0, 10):
                if (i % 3 == 0):
                    pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
                    pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        
                pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
                pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
            pygame.display.update()
        
            for i in range(0, len(grid[0])):
                for j in range(0, len(grid[0])):
                    if (0 < grid[i][j] < 10):
                        value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                        win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
            pygame.display.update()
        
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        pos = pygame.mouse.get_pos()
                        insert(win, (pos[0] // 50, pos[1] // 50))
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
        
        
        main()
#prinst Connect4 code here
def initConnect4():
        from classes.connectgame import Game
    
        game = Game()
        game.game_loop()
#print Coin Dash code here
def initCoinDash():
    import pygame
    import random
    import time
    pygame.init()
    
    # Setting up the screen/play area
    width, height = 800, 600
    backgroundColor = 225, 0, 0
    screen = pygame.display.set_mode((width, height))
    backgroundRaw = pygame.image.load("CDbackground.png")
    background = pygame.transform.scale(backgroundRaw, (800, 600))
    
    # Sets the name of the window
    pygame.display.set_caption('Coin Runner')
    
    # Initializing all variables for later use
    playerX = 370
    playerY = 270
    coinX = 0
    coinY = 0
    bombX = 0
    bombY = 0
    
    pressed_left = False
    pressed_right = False
    pressed_down = False
    pressed_up = False
    
    coinGrab = False
    bombGrab = False
    coinGrab2 = False
    bombGrab2 = False
    
    start = True
    score = 0
    
    
    coin2Mid_X = coinX + 10
    coin2Mid_Y = coinY - 10
    bombMid_X = bombX + 10
    bombMid_Y = bombY - 10
    bomb2Mid_X = bombX + 10
    bomb2Mid_Y = bombY - 10
    
    playerRaw = pygame.image.load("player.png")
    player = pygame.transform.scale(playerRaw, (60, 60))
    
    coinRaw = pygame.image.load("coin.png")
    coin = pygame.transform.scale(coinRaw, (20, 20))
    coin2Raw = pygame.image.load("coin.png")
    coin2 = pygame.transform.scale(coinRaw, (20, 20))
    
    bombRaw = pygame.image.load("bomb.png")
    bomb = pygame.transform.scale(bombRaw, (20, 20))
    bomb2Raw = pygame.image.load("bomb.png")
    bomb2 = pygame.transform.scale(bombRaw, (20, 20))
    
    timeout = time.time() + 30  # seconds
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10
    
    def show_score(x, y):
        scorePrint = font.render('Score: ' + str(score), True, (0, 0, 0))
        screen.blit(scorePrint, (x, y))
    def show_time(x, y):
        timeLeft = round(timeout - time.time(), 1)
        timePrint = font.render('Time Left: ' + str(timeLeft), True, (0, 0, 0))
        screen.blit(timePrint, (x, y))
    
    while True:
    
        screen.blit(background, (0, 0))
        show_score(10, 10)
        show_time(550, 10)
    
        if start == True:
            coinX = random.randrange(50, 750, 10)
            coinY = random.randrange(50, 550, 10)
            coinX2 = random.randrange(50, 750, 10)
            coinY2 = random.randrange(50, 550, 10)
            bombX = random.randrange(50, 750, 10)
            bombY = random.randrange(50, 550, 10)
            bombX2 = random.randrange(50, 750, 10)
            bombY2 = random.randrange(50, 550, 10)
            start = False
    
        if coinGrab == True:
            coinX = random.randrange(50, 750, 10)
            coinY = random.randrange(50, 550, 10)
            bombX = random.randrange(50, 750, 10)
            bombY = random.randrange(50, 550, 10)
            score = score + 1
            coinGrab = False
            print("""
              Grabbed coin || Score:""", score)
    
        if coinGrab2 == True:
            coinX2 = random.randrange(50, 750, 10)
            coinY2 = random.randrange(50, 550, 10)
            bombX2 = random.randrange(50, 750, 10)
            bombY2 = random.randrange(50, 550, 10)
            score = score + 1
            coinGrab2 = False
            print("""
              Grabbed coin || Score:""", score)
    
        if bombGrab == True:
            bombX = random.randrange(50, 750, 10)
            bombY = random.randrange(50, 550, 10)
            bombX2 = random.randrange(50, 750, 10)
            bombY2 = random.randrange(50, 550, 10)
            coinX = random.randrange(50, 750, 10)
            coinY = random.randrange(50, 550, 10)
            coinX2 = random.randrange(50, 750, 10)
            coinY2 = random.randrange(50, 550, 10)
            score = score - 2
            bombGrab = False
            print("""
              Grabbed bomb || Score:""", score)
    
        if bombGrab2 == True:
            bombX2 = random.randrange(50, 750, 10)
            bombY2 = random.randrange(50, 550, 10)
            bombX = random.randrange(50, 750, 10)
            bombY = random.randrange(50, 550, 10)
            coinX = random.randrange(50, 750, 10)
            coinY = random.randrange(50, 550, 10)
            coinX2 = random.randrange(50, 750, 10)
            coinY2 = random.randrange(50, 550, 10)
            score = score - 2
            bombGrab2 = False
            print("""
              Grabbed bomb || Score:""", score)
    
        if score < 0:
            print("""
              Uh oh. You lost all your coins. Better luck next time :(""")
            time.sleep(2)
            pygame.quit()
            break
    
        if time.time() > timeout:
            print("""
              Time is up. Your collected""", score, """coins""")
            time.sleep(2)
            pygame.quit()
            break
    
        # Puts the coins, bombs, and player on the screen over the background
        screen.blit(coin, (coinX, coinY))
        screen.blit(bomb, (bombX, bombY))
        screen.blit(coin2, (coinX2, coinY2))
        screen.blit(bomb2, (bombX2, bombY2))
        screen.blit(player, (playerX, playerY))
    
        pygame.display.flip()
        time.sleep(10 / 1000)
    
        # Allows for keys to be held down to move the player faster
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:  # check for key presses
                if event.key == pygame.K_LEFT:  # left arrow turns left
                    pressed_left = True
                elif event.key == pygame.K_RIGHT:  # right arrow turns right
                    pressed_right = True
                elif event.key == pygame.K_UP:  # up arrow goes up
                    pressed_up = True
                elif event.key == pygame.K_DOWN:  # down arrow goes down
                    pressed_down = True
            elif event.type == pygame.KEYUP:  # check for key releases
                if event.key == pygame.K_LEFT:  # left arrow turns left
                    pressed_left = False
                elif event.key == pygame.K_RIGHT:  # right arrow turns right
                    pressed_right = False
                elif event.key == pygame.K_UP:  # up arrow goes up
                    pressed_up = False
                elif event.key == pygame.K_DOWN:  # down arrow goes down
                    pressed_down = False
        if pressed_left == True:
            playerX = playerX - 10
        if pressed_right == True:
            playerX = playerX + 10
        if pressed_up == True:
            playerY = playerY - 10
        if pressed_down == True:
            playerY = playerY + 10
    
        # Sets borders for the player
        if playerY >= 540:
            playerY = 530
        if playerY <= 0:
            playerY = 10
        if playerX >= 740:
            playerX = 730
        if playerX <= 0:
            playerX = 10  
    
        # Finds the mid point of the player
        playerMid_X = playerX + 30
        playerMid_Y = playerY + 20
    
        # Finds the mid point of the coins
        coinMid_X = coinX + 10
        coinMid_Y = coinY - 10
        coin2Mid_X = coinX2 + 10
        coin2Mid_Y = coinY2 - 10
    
        # Finds the mid point of the bombs
        bombMid_X = bombX + 10
        bombMid_Y = bombY - 10
        bomb2Mid_X = bombX2 + 10
        bomb2Mid_Y = bombY2 - 10
    
        # Creates a circular hitbox around the player creating collisions with the coins or bombs
        diff1 = abs(playerMid_X - coinMid_X)
        diff2 = abs(playerMid_Y - coinMid_Y)
        if (diff1 <= 30) and (diff2 <= 30):
            coinGrab = True
    
        diff3 = abs(playerMid_X - bombMid_X)
        diff4 = abs(playerMid_Y - bombMid_Y)
        if (diff3 <= 30) and (diff4 <= 30):
            bombGrab = True
    
        diff5 = abs(playerMid_X - coin2Mid_X)
        diff6 = abs(playerMid_Y - coin2Mid_Y)
        if (diff5 <= 30) and (diff6 <= 30):
            coinGrab2 = True
    
        diff7 = abs(playerMid_X - bomb2Mid_X)
        diff8 = abs(playerMid_Y - bomb2Mid_Y)
        if (diff7 <= 30) and (diff8 <= 30):
            bombGrab2 = True
    
        pygame.display.flip()
        pygame.display.update()
#print Space Invaders code here
def initSpaceInvaders():
    import math
    import random
    import pygame
    from pygame import mixer

    # Intialize the pygame
    pygame.init()

    # Defines Screen Borders
    screen = pygame.display.set_mode((800, 600))

    # Creates the background borders and sizes the image to the window dimensions
    backgroundRaw = pygame.image.load('SIbackground.png')
    background = pygame.transform.scale(backgroundRaw, (800,600))

    # Creates the background music
    mixer.music.load("background.mp3")
    mixer.music.play(-1)

    # Window title and icon
    pygame.display.set_caption("No Mans Space")
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)

    # Creates the player image and defines the dimensions of the character
    playerRaw = pygame.image.load('player_space.png')
    playerImg = pygame.transform.scale(playerRaw, (100, 100))
    playerX = 370
    playerY = 480
    playerX_change = 0

    # Creates the variables for 6 enemies at the same time
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 6

    enemyRaw = pygame.image.load('enemy.png')
    enemy = pygame.transform.scale(enemyRaw, (60, 60))

    for i in range(num_of_enemies):
        enemyImg.append(enemy)
        enemyX.append(random.randint(0, 730))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(random.randint(2, 4))
        enemyY_change.append(25)

    # Defines the laser image
    laserRaw = pygame.image.load('laser.png')
    laserImg = pygame.transform.scale(laserRaw, (30, 40))
    laserX = 0
    laserY = 480
    laserX_change = 0
    laserY_change = 10
    laser_state = "ready"

    # Initializing the score
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    # Coordinates for the score to show on the screen
    textX = 350
    testY = 10

    # Creates the font for the game over text
    over_font = pygame.font.Font('freesansbold.ttf', 64)


    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))


    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (200, 250))


    def player(x, y):
        screen.blit(playerImg, (x, y))


    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))


    def fire_laser(x, y):
        global laser_state
        laser_state = "fire"
        screen.blit(laserImg, (x + 16, y + 10))


    def isCollision(enemyX, enemyY, laserX, laserY):
        distance = math.sqrt(math.pow(enemyX - laserX, 2) + (math.pow(enemyY - laserY, 2)))
        if distance < 27:
            return True
        else:
            return False

            # Game Loop
    running = True
    while running:

    # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -4
                if event.key == pygame.K_RIGHT:
                    playerX_change = 4
                if event.key == pygame.K_SPACE:
                    if laser_state == "ready":
                        print('part 1')
                        laserSound = mixer.Sound("laser.wav")
                        laserSound.play()
                        # Get the current x cordinate of the spaceship
                        laserX = playerX
                        fire_laser(laserX, laserY)
                        print('part 2')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Creates borders for the player
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Defining how enemy moves and how the game is lost
        for i in range(num_of_enemies):

            # If the enemy drops to a certain level the player looses and game stops
            if enemyY[i] > 450:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            # Makes the enemies bounce off the wall and move down a "level"
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = random.randint(2, 4)
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = random.randint(-4, -2)
                enemyY[i] += enemyY_change[i]

            # Setting up collisions between the laser and enemy
            collision = isCollision(enemyX[i], enemyY[i], laserX, laserY)
            if collision:
                print('collision')
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                laserY = 480
                laser_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        # Reseting the laser to original placement
        if laserY <= 0:
            laserY = 480
            laser_state = "ready"
            print('part 3')

        if laser_state == "fire":
            print('part 4')
            fire_laser(laserX, laserY)
            laserY -= laserY_change

        # Calling funtions
        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()




def start():

	btn1 = Button(root,
                  image=chess,
                  fg='#ffffff',
                  height=48,
                  width=130,
                  bd=0,
                  command=initChess)
	btn1.place(x=115, y=54)


	btn2 = Button(root,
				  image=connect4,
                  fg='#ffffff',
                  height=48,
                  width=130,
                  bd=0,
                  command=initConnect4)
	btn2.place(x=115, y=112)


	btn3 = Button(root,
                  image=checkers,
                  fg='#ffffff',
                  height=48,
                  width=130,
                  bd=0,
                  command=initCheckers)
	btn3.place(x=115, y=171)


	btn4 = Button(root,
                  image=sudoku,
                  fg='#ffffff',
                  height=48,
                  width=130,
                  bd=0,
                  command=initSudoku)
	btn4.place(x=250, y=54)


	btn5 = Button(root,
                  image=trafficfun,
                  fg='#ffffff',
                  height=48,
                  width=130,
                  bd=0,
                  command=initTrafficFun)
	btn5.place(x=250, y=112)


	btn6 = Button(root,
                  image=CDash,
                  fg='#ffffff',
                  height=48,
                  width=130,
                  bd=0,
                  command=initCoinDash)
	btn6.place(x=250, y=171)

	btn7 = Button(root,
                  image=snake,
                  fg='#ffffff',
                  height=48,
                  width=130,
                  bd=0,
                  command=initSnake)
	btn7.place(x=115, y=236)

	btn8 = Button(root,
                  image=spaceinvaders,
                  fg='#ffffff',
                  height=48,
                  width=130,
                  bd=0,
                  command=initSpaceInvaders)
	btn8.place(x=250, y=236)



btn12 = Button(root,
              text='start',
              fg='#ffffff',
              height=2,
              width=13,
              bd=0,
              command=start)
btn12.place(x=115, y=54)

root.mainloop()