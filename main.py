import pygame
import random
import math

# init
pygame.init()

# screen size
size = height , width = 300, 550
screen = pygame.display.set_mode(size)

# Title
pygame.display.set_caption('Dor dor')

# Icon game
icon = pygame.image.load('C:/Users/erik/Downloads/tiger32.png')
pygame.display.set_icon(icon)

diamond_ring = pygame.image.load('C:/Users/erik/Downloads/diamond-ring.png')


# background
background = pygame.image.load('C:/Users/erik/Downloads/background_grass.jpg')

# player
def player(x, y):
    # img_player = pygame.image.load('C:/Users/erik/Downloads/tiger32.png')
    screen.blit(icon, (x, y))

x_player = 185
y_player = 510
x_playerPoint = 0

# ring
def ring(x, y):
    screen.blit(diamond_ring, (x, y))

xRing = random.randint(20, 265)
yRing = random.randint(10, 20)
yRingPoint = 3

# collision
def collision(x_player, y_player, xRing, yRing):
    distance = math.sqrt(math.pow(x_player - xRing, 2)) + (math.pow(y_player - yRing,2))
    # rumus jarak
    # (x1,y1);(x2,y2)
    # jarak = akar dari (x2 - x1)**2 + (y2 - y1)**2
    if distance < 20:
        return True
    else:
        return False

clock = pygame.time.Clock()

# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 16)

def show_score(x, y):
    score_number = font.render('score: ' + str(score), True, (255,255,255))
    screen.blit(score_number, (x, y))

# def end_game(x, y):
#     your_score = font.render('Your Score is '+ str(score) True, (255,255,255))
#     screen.blit
   

xScore = 10
yScore = 10

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_playerPoint -= 6
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_playerPoint += 6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_playerPoint = 0
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_playerPoint = 0

    # moving
    if x_player >= 270:
       x_player = 263
    if x_player <= 0:
       x_player = 7

    # movement player
    x_player += x_playerPoint
   
    # movement ring
    yRing += yRingPoint
    if yRing >= 540:
        xRing = random.randint(20, 265)
        yRing = random.randint(10, 20)
        score += 1

    # show player
    player(x_player, y_player)

    # show ring
    ring(xRing, yRing)

    # collision
    crush = collision(x_player, y_player, xRing, yRing)
    if crush:
        show_score(150, 275)
        break

    # score
    show_score(xScore, yScore)

    clock.tick(60)

    pygame.display.update()

print("your score is : " + str(score))
# show_score(150, 275)
pygame.quit()
