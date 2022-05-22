import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, player, x, y, w, h, win):
        self.player = player
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.win = win
        self.isJump = False
        self.jumpCount = 10
        self.c = 0
        
    def jump(self):
        JUMP_COUNT = 20
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:
            if (not self.isJump) and self.y == 850:
                self.isJump = True
        if self.c <= JUMP_COUNT and self.isJump:
                self.c += 1
                print(self.c)
                self.y -= 7
        else:
            self.isJump = False
            if self.y == 850:
                self.c = 0
        
        return self.y

    def jump2(self):
        JUMP_COUNT = 20
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w]:
            if (not self.isJump) and self.y == 850:
                self.isJump = True
        if self.c <= JUMP_COUNT and self.isJump:
                self.c += 1
                print(self.c)
                self.y -= 7
        else:
            self.isJump = False
            if self.y == 850:
                self.c = 0
        
        return self.y
    
    def gravity(self):
        if self.y < 850 and not self.isJump:
            self.y += 7
        return self.y
    
    def hit(self):
        print('hit')

        return self.y
    def movement_left(self):
        userInput = pygame.key.get_pressed()
        vel_x = 5
        
        if userInput[pygame.K_LEFT] and self.x > 0:
            self.x -= vel_x

    def movement_right(self, WIDTH):
        userInput = pygame.key.get_pressed()
        vel_x = 5
        
        if userInput[pygame.K_RIGHT] and self.x < WIDTH:
            self.x += vel_x
    
    
    
    def movement_left_2(self):
        userInput = pygame.key.get_pressed()
        vel_x = 5
        
        if userInput[pygame.K_a] and self.x > 0:
            self.x -= vel_x

    def movement_right_2(self, WIDTH):
        userInput = pygame.key.get_pressed()
        vel_x = 5
        
        if userInput[pygame.K_d] and self.x < WIDTH:
            self.x += vel_x
    
    #drawFrameAxes

    # for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_SPACE and self.y == 850:
    #             isJump = True
    #     if self.y == 0:
    #         isJump = False
