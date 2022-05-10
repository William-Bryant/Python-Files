#This is a personal project of a remake of the popular mobile game Flappy Bird using the Pygame library
import pygame,random

pygame.init()
Width = 400
Height = 710
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('Flappy Bird Remake')
clock = pygame.time.Clock()

background = pygame.transform.scale(\
    pygame.image.load('assets/sprites/background-day.png'),(400,710))
bird = pygame.transform.rotate(\
    pygame.transform.scale(\
    pygame.image.load('assets/sprites/bluebird-upflap.png'), (50,40)), 45)
birdUpFlap = pygame.transform.rotate(\
    pygame.transform.scale(\
    pygame.image.load('assets/sprites/bluebird-upflap.png'), (50,40)), 45)
birdDownFlap = pygame.transform.rotate(\
    pygame.transform.scale(\
    pygame.image.load('assets/sprites/bluebird-downflap.png'), (50,40)), 315)
btmPipe =  pygame.transform.scale(\
    pygame.image.load('assets/sprites/pipe-green.png'), (80,560))
topPipe = pygame.transform.scale(\
    pygame.transform.rotate(btmPipe, 180), (80,560))
groundImg = pygame.transform.scale(\
    pygame.image.load('assets/sprites/base.png'),(Width,200))
gameOver = pygame.transform.scale(\
    pygame.image.load('assets/sprites/gameover.png'),(200,50))

#misc rectangles
gameOverRect = pygame.Rect(Width/2-100,Height/2-25,200,50)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = bird.convert_alpha()
       # self.image.set_colorkey((0,0,0)) #makes transparents background
        self.rect = self.image.get_rect()
        self.radius = 1
        #pygame.draw.circle(self.image, (255,0,0), self.rect.center, self.radius)
        self.rect.center = (100, Height /2)
        self.jump = False
        self.midJump = False
        self.gravity = 3
        self.jumpHeight = 14
        self.velocity = self.jumpHeight
        self.fallSpeed = 12
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        
        if self.jump == False:
            self.image = birdDownFlap.convert()
            self.rect.y += self.fallSpeed          
        if self.jump == True:
            self.gravity = 1
            self.image = birdUpFlap.convert()
            self.rect.y -= self.velocity
            self.velocity -= self.gravity
            if self.velocity < -self.jumpHeight:
                self.jump = False
                self.velocity = self.jumpHeight
        
        if self.rect.bottom > 640:
            self.fallSpeed = 0
            
class BtmPipe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = btmPipe.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(250,610)
        self.rect.x = 400
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 3

    def update(self): 
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill
       
class TopPipe(pygame.sprite.Sprite,):
    def __init__(self, btmHeight):
        pygame.sprite.Sprite.__init__(self)
        self.image = topPipe.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = btmHeight -760
        self.rect.x = 400
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 3

    def update(self): 
        self.rect.x -= self.speed
        if self.rect.right < 0:
            
            self.kill

class Ground(pygame.sprite.Sprite,):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = groundImg.convert()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 640
        self.mask = pygame.mask.from_surface(self.image)
        pygame.draw.rect(self.image,(255,0,0), self.rect)

#main loop
def main():
    allSprites = pygame.sprite.Group()
    obsts = pygame.sprite.Group()

    player = Player()
    allSprites.add(player)

    bPipe1 = BtmPipe()
    allSprites.add(bPipe1)
    obsts.add(bPipe1)

    tPipe1 = TopPipe(bPipe1.rect.y)
    allSprites.add(tPipe1)
    obsts.add(tPipe1)

    ground = Ground()
    allSprites.add(ground)
    obsts.add(ground)

    counter = 0
    font = pygame.font.Font('assets/font.ttf', 50)
    text = font.render(str(counter), True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (200,75)
    game = True
    
    spawnPipe = pygame.USEREVENT + 1
    dropBird = pygame.USEREVENT + 2
 
    pygame.time.set_timer(spawnPipe, 2000)
    flight = True
    while game == True:
        
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                False
            elif flight == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        player.fallSpeed == 12
                        main()
            elif event.type == spawnPipe and flight == True:
                    allSprites.remove (ground)
                    obsts.remove(ground)

                    btmPipe = BtmPipe()
                    allSprites.add(btmPipe)
                    obsts.add(btmPipe)

                    tPipe = TopPipe(btmPipe.rect.y)
                    allSprites.add(tPipe)
                    obsts.add(tPipe)

                    allSprites.add(ground)
                    obsts.add(ground)

                    counter += 1 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and flight == True:
                    if player.jump == True:
                        player.velocity = player.jumpHeight
                    else:
                        player.jump = True
        try: 
            if btmPipe.rect.x == 59:
                    counter += .5
   
        except:
            if bPipe1.rect.x == 59:
                counter +=1    

        allSprites.update()
        screen.blit(background,(0,0))
        allSprites.draw(screen)

        text = font.render(str(int(counter)), True, (255,255,255))
        screen.blit(text, textRect)

        for i in obsts:
            
            if pygame.sprite.collide_mask(i,player) or player.rect.y == 576:
                     
                    try:
                        btmPipe.speed, bPipe1.speed, tPipe.speed, tPipe1.speed = 0,0,0,0
                    except: 
                        bPipe1.speed, tPipe1.speed = 0,0
                    pygame.time.set_timer(dropBird, 500)
                    player.fallSpeed = 15
                    flight = False
                    
        if flight == False:
            screen.blit(gameOver,(gameOverRect.x,gameOverRect.y))
            
        if player.rect.bottom > 630:
            player.fallSpeed = 0
            try:
                btmPipe.speed, bPipe1.speed, tPipe.speed, tPipe1.speed = 0,0,0,0
            except: 
                bPipe1.speed, tPipe1.speed = 0,0
            pygame.time.set_timer(dropBird, 500)
            flight = False
                     
        pygame.display.flip()
    
    main()
main()
    