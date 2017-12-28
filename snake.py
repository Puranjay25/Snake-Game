import pygame
import sys
import time
import random

pygame.init()
score=0
y=45

direction='RIGHT'
changeto=direction

display_screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption("Snake Game")

fps=pygame.time.Clock()

snakepos=[350,250]
snake=[[350,250],[340,250],[330,250]]
snakewidth=10
snakeheight=10

foodpos=[random.randrange(1,70)*10,random.randrange(1,50)*10]
foodspawn=True
foodwidth=10
foodheight=10

red=pygame.Color(255,0,0)
black=pygame.Color(0,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)
white=pygame.Color(255,255,255)
purple=pygame.Color(128,0,128)
pink=pygame.Color(255,20,147)
dark_blue=pygame.Color(0,0,139)

def select_rectangle(y_coordinate):
    pygame.draw.rect(display_screen,dark_blue,pygame.Rect(280,y_coordinate,10,10))
    pygame.display.flip()

def start_menu():
    main_font=pygame.font.SysFont('BAZOOKA',25)
    start_display=main_font.render('Start Game',True,pink)
    start_shape=start_display.get_rect()
    start_shape.midtop=(350,40)
    display_screen.blit(start_display,start_shape)
    quit_display=main_font.render('Quit Game',True,pink)
    quit_shape=quit_display.get_rect()
    quit_shape.midtop=(350,100)
    display_screen.blit(quit_display,quit_shape)
    pygame.display.flip()
    
def gameover_message():
    font=pygame.font.SysFont('Arial',50)
    display=font.render('GAME OVER!',True,blue)
    area=display.get_rect()
    area.midtop=(500,20)
    display_screen.blit(display,area)
    showscore(0)
    pygame.display.flip()
    
def showscore(status=1):
    font1=pygame.font.SysFont('Arial',30)
    display1=font1.render('Score: {0}'.format(score),True,purple)
    area1=display1.get_rect()
    if status==1:
        area1.midtop=(60,20)
    else:
        area1.midtop=(500,70)
    display_screen.blit(display1,area1)
    
while 1:
    sound=pygame.mixer.Sound("Button-click-sound.mp3")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changeto='LEFT'
            if event.key==pygame.K_RIGHT:
                changeto='RIGHT'
            if event.key==pygame.K_UP:
                changeto='UP'
            if event.key==pygame.K_DOWN:
                changeto='DOWN'
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    display_screen.fill(white)            
    
    #CHANGE SNAKE DIRECTION
    if changeto=='RIGHT' and not direction=='LEFT':
        direction='RIGHT'
    if changeto=='LEFT' and not direction=='RIGHT':
        direction='LEFT'
    if changeto=='UP' and not direction=='DOWN':
        direction='UP'
    if changeto=='DOWN' and not direction=='UP':
        direction='DOWN'
    
    #MOVE SNAKE
    if direction=='LEFT':
        snakepos[0]-=10
    if direction=='RIGHT':
        snakepos[0]+=10
    if direction=='UP':
        snakepos[1]-=10
    if direction=='DOWN':
        snakepos[1]+=10

    #SNAKE MOVEMENT
    snake.insert(0,list(snakepos))
    if snakepos[0]==foodpos[0] and snakepos[1]==foodpos[1]:
        foodspawn=False
        sound.set_volume(1)
        sound.play()
        score=score+1
    else:
        snake.pop()

    #DRAW SNAKE
    for pos in snake:
        pygame.draw.rect(display_screen,red,pygame.Rect(pos[0],pos[1],snakewidth,snakeheight))

    #DRAW FOOD
    pygame.draw.rect(display_screen,green,pygame.Rect(foodpos[0],foodpos[1],foodwidth,foodheight))

    #FOOD MOVEMENT
    if foodspawn==False:
        foodpos=[random.randrange(1,70)*10,random.randrange(1,50)*10]
        foodspawn=True

    #GAME OVER CONDITION
    if snakepos[0]<0 or snakepos[0]>1000:
        gameover_message()
        time.sleep(5)
        pygame.quit()
    if snakepos[1]<0 or snakepos[1]>800:
        gameover_message()
        time.sleep(5)
        pygame.quit()
    for pos in snake[1:]:
        if pos[0]==snakepos[0] and pos[1]==snakepos[1]:
            gameover_message()
            time.sleep(5)
            pygame.quit()
            
    showscore(1)

    pygame.display.flip()

    fps.tick(16)
