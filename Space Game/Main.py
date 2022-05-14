#This is a personal project of a basic multiplayer arcade space game I made while learning the Pygame library.
import pygame, random
pygame.font.init()
pygame.mixer.init()


WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Game ")

White = (255,255,255)
Black = (0, 0, 0)
redColor = (255,0,0)
yellowColor = (255,255,0)
border = pygame.Rect(445, 0, 10, 600)

#bulletHitSound = pygame.mixer.Sound('assets/gun+1.mp3')
#bulletFireSound = pygame.mixer.Sound('assets/gun+silencer.mp3')

healthFont = pygame.font.SysFont('comicsans', 40)
winnerFont = pygame.font.SysFont('comicsans', 100)

FPS = 60
vel = 5
bulVel = 7
maxBullets = 6
maxAsts = 15
yellowHit = pygame.USEREVENT + 1
redHit = pygame.USEREVENT + 2
astSpawnEvent = pygame.USEREVENT + 3 
astVel = 1

YellowSpaceship = pygame.image.load('assets/spaceship_yellow.png')
YellowSpaceship = pygame.transform.rotate(\
    pygame.transform.scale(YellowSpaceship, (40,30)),90)

RedSpaceship = pygame.image.load('assets/spaceship_red.png')
RedSpaceship = pygame.transform.rotate(\
    pygame.transform.scale(RedSpaceship, (40,30)), 270)

asteroid = pygame.transform.scale(\
    pygame.image.load('assets/asteroid.png'), (50,35))

spaceBackground = pygame.transform.scale(\
    pygame.image.load('assets/space.png'), (WIDTH,HEIGHT))

def draw_window(red,yellow, redBullets, yellowBullets, redHealth, yellowHealth, asteroids):
    screen.blit(spaceBackground,(0,0))

    pygame.draw.rect(screen, Black, border)
    redHealthText = healthFont.render(f"Lives: {redHealth}", 1, White)
    yellowHealthText = healthFont.render(f"Lives: {yellowHealth}", 1, White)
    screen.blit(redHealthText, (WIDTH - redHealthText.get_width() - 10, 10))
    screen.blit(yellowHealthText, (10, 10))
    screen.blit(YellowSpaceship, (yellow.x, yellow.y))
    screen.blit(RedSpaceship,(red.x, red.y))

    for rock in asteroids:
        screen.blit(asteroid, (rock.x,rock.y))

    

    for bullet in redBullets:
        pygame.draw.rect(screen, redColor, bullet)

    for bullet in yellowBullets:
        pygame.draw.rect(screen, yellowColor, bullet)
    
    pygame.display.update()

def yellowControls(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - vel > 0:
        yellow.x -= vel
    if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < border.x:
        yellow.x += vel
    if keys_pressed[pygame.K_w] and yellow.y - vel > 0:
        yellow.y -= vel
    if keys_pressed[pygame.K_s] and yellow.y + vel + yellow.width < HEIGHT:
        yellow.y += vel

def redControls(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - vel > border.x + border.width:
        red.x -= vel
    if keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < WIDTH:
        red.x += vel
    if keys_pressed[pygame.K_UP] and red.y - vel > 0:
        red.y -= vel
    if keys_pressed[pygame.K_DOWN] and red.y + vel + red.width < HEIGHT:
        red.y += vel

def bulletHandle(yellowBullets, redBullets, yellow, red):
    for bullet in yellowBullets:
            bullet.x += bulVel
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(redHit))
                yellowBullets.remove(bullet)
            if bullet.x > WIDTH:
                yellowBullets.remove(bullet)

    for bullet in redBullets:
            bullet.x -= bulVel
            if yellow.colliderect(bullet):
                pygame.event.post(pygame.event.Event(yellowHit))
                redBullets.remove(bullet)
            if bullet.x < 0:
                redBullets.remove(bullet)

def astHandle(asteroids, yellow, red, redBullets, yellowBullets):
    for rock in asteroids:
        
        rock.y += astVel
        if red.colliderect(rock):
            pygame.event.post(pygame.event.Event(redHit))
            asteroids.remove(rock)
        if yellow.colliderect(rock):
            pygame.event.post(pygame.event.Event(yellowHit))
            asteroids.remove(rock)
        for bullet in redBullets:
            if bullet.colliderect(rock):
                asteroids.remove(rock)
                redBullets.remove(bullet)
        for bullet in yellowBullets:
            if bullet.colliderect(rock):
                asteroids.remove(rock)
                yellowBullets.remove(bullet)
        if rock.y > 600:
            asteroids.remove(rock)

        #print(asteroids)
        
def winner(text):
    winText = winnerFont.render(text,1,White)
    screen.blit(winText,(WIDTH//2 - winText.get_width()/2, \
             HEIGHT //2 - winText.get_height()/2))
   
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(840,300, 40,30)
    yellow = pygame.Rect(30,300, 40,30)

    #astSpawn = random.randint(10,WIDTH)
    #astRect = pygame.Rect(10, 100, 50, 35)
    

    redBullets = []
    yellowBullets = []
    asteroids = []

    redHealth = 6
    yellowHealth = 6
    clock = pygame.time.Clock()
    pygame.time.set_timer(astSpawnEvent, 1000)

    while True: 
        clock.tick(FPS)
        astSpawn = random.randint(10,WIDTH)
        #astRect = pygame.Rect(astSpawn, 0, 50, 35)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                #bulletFireSound.play()
                if event.key == pygame.K_v and len(yellowBullets) < maxBullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2,10,5) # in place of a bullet pixel art
                    yellowBullets.append(bullet)

                if event.key == pygame.K_m and len(redBullets) < maxBullets:
                    bullet = pygame.Rect(red.x, red.y + red.height//2,10,5) # in place of a bullet pixel art
                    redBullets.append(bullet)

            if event.type == redHit:
               # bulletHitSound.play()
                redHealth -= 1
            if event.type == yellowHit:
                yellowHealth -=1 
                #bulletHitSound.play()
            
            if event.type == astSpawnEvent and len(asteroids) < maxAsts or len(asteroids) < 3:
                rock = pygame.Rect(astSpawn,0,50,35)
                
                asteroids.append(rock)
                print(f"{rock} is rock, length {len(asteroids)}")

                

        winText = ""    
        if redHealth <= 0:
            winText =  "Yellow wins!"
        if yellowHealth <= 0:
            winText = "Red Wins!"

        if winText != "":
            winner(winText)
            break

        bulletHandle(yellowBullets, redBullets, yellow, red)
        astHandle(asteroids, yellow, red, yellowBullets, redBullets)
        keys_pressed = pygame.key.get_pressed()

        yellowControls(keys_pressed, yellow)
        redControls(keys_pressed, red)
        draw_window(red, yellow, redBullets, yellowBullets, redHealth, yellowHealth, asteroids,)

    main()  



main()
