import pygame
import os
from Player import Player
from bullet import Bullet
import time
import sys
import random

pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption("Red Man and Blue Man: Everthing is fair in Love and Wardle")
global lives1
lives1 = 3
global lives2
lives2 = 3
def player_1_shoot_check(b):
    if (b.y-bulletwidth//2) < (hitbox2[1] + hitbox2[3]) and (b.y + bulletwidth//2) > hitbox2[1]:
        if b.direction == "r":
            hitbox_adjustment = 20
        else:
            hitbox_adjustment = -20
        if (b.x + bulletwidth//2)> hitbox2[0] + hitbox_adjustment and (b.x -bulletwidth//2) < (hitbox2[0]+ hitbox2[2]) + hitbox_adjustment:
            player2.hit()
            global lives2
            if b.type == "n":
                lives2-=1
            else:
                lives2=0
            if lives2==0:
                setting()
                time.sleep(3)
                sys.exit(0)
            bullets.pop(bullets.index(b))
            #print('here')
                    
def player_2_shoot_check(b):
    global lives1 
    if (b.y-bulletheight2//2) < (hitbox[1] + hitbox[3]) and (b.y+ bulletheight2//2)> hitbox[1]:
        if b.direction == "r":
            hitbox_adjustment = 20
        else:
            hitbox_adjustment = -20
        if (b.x + bulletwidth2//2)> hitbox[0] + hitbox_adjustment and (b.x - bulletheight2//2) < (hitbox[0]+ hitbox[2]) + hitbox_adjustment:
            player1.hit()
            if b.type == "n":
                lives1-=1 
            else:
                lives1=0

            if lives1==0:
                setting()
                time.sleep(3)
                sys.exit(0)
            
            bullets2.pop(bullets2.index(b))

WIDTH, HEIGHT=1700, 1000
PLAYER_WIDTH = 35
PLAYER_HEIGHT = 75
bulletwidth, bulletheight= 20, 20
bulletwidth2, bulletheight2= 20, 20
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
PLAYER_1_Image=pygame.image.load(os.path.join('Player one.png'))
PLAYER_1=pygame.transform.scale(PLAYER_1_Image, (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_2_Image=pygame.image.load(os.path.join('Player two.png'))
PLAYER_2=pygame.transform.scale(PLAYER_2_Image, (PLAYER_WIDTH, PLAYER_HEIGHT))
GROUND_IMAGE=pygame.image.load(os.path.join('floor.png'))
GROUND=pygame.transform.scale(GROUND_IMAGE, (1700, 600))
Instakill=pygame.image.load(os.path.join('homing_missle.png'))
flipped_player_1=pygame.image.load(os.path.join('Flipped_player_1.png'))
flipped_player_1=pygame.transform.scale(flipped_player_1, (PLAYER_WIDTH, PLAYER_HEIGHT))
flipped_player_2=pygame.image.load(os.path.join('Player two_001.png'))
flipped_player_2=pygame.transform.scale(flipped_player_2, (PLAYER_WIDTH, PLAYER_HEIGHT))
flipped_homing_missle=pygame.image.load(os.path.join('flipped_homing_missle.png'))
flipped_homing_missle=pygame.transform.scale(flipped_homing_missle, (bulletwidth, bulletheight))


FPS = 60
PLAYER_1_X = 1600
PLAYER_1_Y = 850
PLAYER_2_X = 100
PLAYER_2_Y = 850
player1 = Player(PLAYER_1, PLAYER_1_X, PLAYER_1_Y, PLAYER_WIDTH, PLAYER_HEIGHT, WIN)
player2 = Player(PLAYER_2, PLAYER_2_X, PLAYER_2_Y, PLAYER_WIDTH, PLAYER_HEIGHT, WIN)
bullets = []
bullets2 = []
font = pygame.font.SysFont('comicsans', 20, True, True)
endfont=pygame.font.SysFont('comicsans', 80, True, True)

def setting():
    WIN.fill((0, 170, 255))
    endfont=pygame.font.SysFont('comicsans', 80, True, True)
    text1 = font.render('Remaining lives for Red Man: ' + str(lives2), 1, (0,0,0))
    text2 = font.render('Remaining lives for Blue : ' + str(lives1), 1, (0,0,0))
    WIN.blit(text1, (200, 10))
    WIN.blit(text2, (1200,10))
    WIN.blit(PLAYER_1, (PLAYER_1_X, PLAYER_1_Y))
    WIN.blit(PLAYER_2, (PLAYER_2_X, PLAYER_2_Y))
    WIN.blit(GROUND, (0,400))
    if lives1==0:
        text4 = endfont.render(('The winner is...Red Man'), 1, (0,0,0))
        WIN.blit(text4, (300, 200))
    if lives2==0:
        text3 = endfont.render(('The winner is...Blue Man'), 1, (0,0,0))
        WIN.blit(text3, (300, 200))

    for b in bullets:
        if b.type == "n":
            bulletwidth, bulletheight = 10,10
            bullet = pygame.image.load(os.path.join('bullet.png'))
            bullet =pygame.transform.scale(bullet, (bulletwidth, bulletheight))
            WIN.blit(bullet, (b.x, b.y))
        elif b.type == "i" and b.direction == "r":
            bulletwidth, bulletheight = 20, 20
            bullet = pygame.image.load(os.path.join("homing_missle.png"))
            bullet= pygame.transform.scale(bullet, (bulletwidth,bulletheight))
            WIN.blit(bullet, (b.x, b.y))

        elif b.type == "i" and b.direction == "l":
            bulletwidth, bulletheight = 20, 20
            bullet = flipped_homing_missle
            bullet= pygame.transform.scale(bullet, (bulletwidth,bulletheight))
            WIN.blit(bullet, (b.x, b.y))


    for b in bullets2:
        if b.type == "n":
            bulletwidth2, bulletheight2 = 10, 10
            bullet = pygame.image.load(os.path.join('bullet.png'))
            bullet = pygame.transform.scale(bullet, (bulletwidth2, bulletheight2))
            WIN.blit(bullet, (b.x, b.y))
        elif b.type == "i" and b.direction == "r":
            bulletwidth2, bulletheight2 = 20, 20
            bullet = pygame.image.load(os.path.join("homing_missle.png"))
            bullet= pygame.transform.scale(bullet, (bulletwidth2,bulletheight2))
            WIN.blit(bullet, (b.x, b.y))

        elif b.type == "i" and b.direction == "l":
            bulletwidth2, bulletheight2 = 20, 20
            bullet = flipped_homing_missle
            bullet= pygame.transform.scale(bullet, (bulletwidth2,bulletheight2))
            WIN.blit(bullet, (b.x, b.y))
    
    pygame.draw.rect(WIN, (255, 255, 255), (PLAYER_1_X, PLAYER_1_Y -8, PLAYER_WIDTH, 4), 2)
    pygame.draw.rect(WIN, (255, 255, 255), (PLAYER_2_X, PLAYER_2_Y -8,  PLAYER_WIDTH, 4), 2)
    pygame.draw.rect(WIN, (0, 255, 0), (PLAYER_1_X, PLAYER_1_Y -8, (PLAYER_WIDTH/3) * lives1, 4), 0)
    pygame.draw.rect(WIN, (0, 255, 0), (PLAYER_2_X, PLAYER_2_Y -8,  (PLAYER_WIDTH/3) * lives2, 4), 0)

    # print(lives1)

    pygame.display.update()
clock=pygame.time.Clock()
run= True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
        if event.type == pygame.KEYDOWN:
            if len(bullets) == 0:
                rint = random.randint(1, 101)
                type = "n"
                if 1 <= rint <= 10:
                    type = "i"
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(PLAYER_1_X + PLAYER_WIDTH//2, PLAYER_1_Y+20,  "r", type))
                if event.key == pygame.K_SLASH:
                    bullets.append(Bullet(PLAYER_1_X + PLAYER_WIDTH//2, PLAYER_1_Y+20,  "l", type))
            if len(bullets2)==0:
                if event.key == pygame.K_e:
                    bullets2.append(Bullet(PLAYER_2_X + PLAYER_WIDTH//2, PLAYER_2_Y+20,  "r", type))
                if event.key == pygame.K_q:
                    bullets2.append(Bullet(PLAYER_2_X + PLAYER_WIDTH//2, PLAYER_2_Y+20,  "l", type))
            
    temp = player1.x
    player1.movement_right(WIDTH-35)    
    PLAYER_1_X = player1.x
    player1.movement_left()
    PLAYER_1_X = player1.x
    
    player2.movement_right_2(WIDTH-35)
    PLAYER_2_X = player2.x
    player2.movement_left_2()
    PLAYER_2_X = player2.x
    

    for b in bullets:
        if b.direction == "r":    
            b.update_positive()
            player_1_shoot_check(b)       
        else:
            b.update_negative()
            player_1_shoot_check(b)
            #player_2_shoot_check(b)
        if b.x > WIDTH or b.x < 0:
            #print("hello")
            bullets.remove(b)
    for b2 in bullets2:
        if b2.direction == "r":    
            b2.update_positive()
            player_2_shoot_check(b2)
        else:
            b2.update_negative()
            player_2_shoot_check(b2)
        if b2.x > WIDTH or b2.x < 0:
            #print("hello")
            bullets2.remove(b2)
            
            

    hitbox = (PLAYER_1_X, PLAYER_1_Y, 35, 75)
    hitbox2 = (PLAYER_2_X, PLAYER_2_Y, 35, 75)


    PLAYER_1_Y = player1.jump()
    PLAYER_1_Y = player1.gravity()
    PLAYER_2_Y = player2.jump2()
    PLAYER_2_Y = player2.gravity()
    setting()
pygame.quit()
